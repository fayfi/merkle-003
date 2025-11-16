"""
Minimal Merkle Tree implementation using SHA-256.
- Build tree from leaves (any str/bytes convertible)
- Generate inclusion proof for a leaf by index
- Verify proof against a given root
"""
from __future__ import annotations
import hashlib
from typing import Iterable, List, Dict, Any


def _to_bytes(x: Any) -> bytes:
    if isinstance(x, bytes):
        return x
    if isinstance(x, str):
        return x.encode("utf-8")
    return str(x).encode("utf-8")


def _hash(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()


class MerkleTree:
    def __init__(self, leaves: Iterable[Any]):
        leaves_list = list(leaves)
        if not leaves_list:
            raise ValueError("MerkleTree requires at least one leaf")
        # Level 0: hashed leaves
        level0 = [_hash(_to_bytes(x)) for x in leaves_list]
        self._levels: List[List[bytes]] = [level0]
        # Build upper levels
        while len(self._levels[-1]) > 1:
            prev = self._levels[-1]
            nxt: List[bytes] = []
            for i in range(0, len(prev), 2):
                left = prev[i]
                right = prev[i + 1] if i + 1 < len(prev) else left  # duplicate last if odd
                nxt.append(_hash(left + right))
            self._levels.append(nxt)

    @property
    def leaf_count(self) -> int:
        return len(self._levels[0])

    @property
    def root(self) -> bytes:
        return self._levels[-1][0]

    @property
    def root_hex(self) -> str:
        return self.root.hex()

    def get_proof(self, index: int) -> List[Dict[str, str]]:
        """Return proof as [{'hash': hex, 'position': 'left'|'right'}, ...]."""
        if index < 0 or index >= self.leaf_count:
            raise IndexError("leaf index out of range")
        proof: List[Dict[str, str]] = []
        idx = index
        for lvl in range(len(self._levels) - 1):
            level = self._levels[lvl]
            is_right = (idx % 2 == 1)
            sibling_idx = idx - 1 if is_right else idx + 1
            if sibling_idx >= len(level):
                sibling_idx = idx  # odd length: sibling is itself (duplicated)
            position = "left" if is_right else "right"
            proof.append({"hash": level[sibling_idx].hex(), "position": position})
            idx //= 2
        return proof

    @staticmethod
    def verify_proof(leaf: Any, proof: List[Dict[str, str]], root_hex: str) -> bool:
        node = _hash(_to_bytes(leaf))
        for p in proof:
            sib = bytes.fromhex(p["hash"])
            pos = p["position"]
            if pos == "left":
                node = _hash(sib + node)
            else:
                node = _hash(node + sib)
        return node.hex() == root_hex


def verify_proof(leaf: Any, proof: List[Dict[str, str]], root_hex: str) -> bool:
    """Verify a single leaf's inclusion proof."""
    return MerkleTree.verify_proof(leaf, proof, root_hex)
