import os
import sys
from typing import List

# Ensure 'src' is on import path for local runs
CURRENT_DIR = os.path.dirname(__file__)
SRC_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "src"))
if SRC_PATH not in sys.path:
    sys.path.append(SRC_PATH)

from merkle.tree import MerkleTree, verify_proof


def run_demo(leaves: List[str], leaf_index: int) -> None:
    tree = MerkleTree(leaves)
    root_hex = tree.root_hex
    proof = tree.get_proof(leaf_index)
    ok = verify_proof(leaves[leaf_index], proof, root_hex)

    print("Leaves:", leaves)
    print("Leaf index:", leaf_index, "value:", leaves[leaf_index])
    print("Root:", root_hex)
    print("Proof:", proof)
    print("Verify:", ok)


if __name__ == "__main__":
    # Minimal demo: customize leaves via CLI args
    args = sys.argv[1:]
    if args:
        # last arg can be index, others are leaves
        try:
            leaf_index = int(args[-1])
            leaves = args[:-1]
        except ValueError:
            # default index 0 when no integer provided
            leaves = args
            leaf_index = 0
    else:
        leaves = ["a", "b", "c", "d", "e"]
        leaf_index = 2

    if not leaves:
        print("Please provide at least one leaf.")
        sys.exit(1)
    if leaf_index < 0 or leaf_index >= len(leaves):
        print(f"Leaf index {leaf_index} out of range for {len(leaves)} leaves.")
        sys.exit(1)

    run_demo(leaves, leaf_index)
