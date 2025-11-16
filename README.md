# Merkle Tree 默克尔树

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

> 一个轻量级的 Python 默克尔树实现，用于区块链数据完整性校验与密码学证明生成。

## 📖 简介

默克尔树（Merkle Tree）是一种哈希二叉树结构，广泛应用于区块链、分布式系统与数据校验场景。本项目提供：

- **高效构建**：从任意数据列表构建完整默克尔树
- **证明生成**：为指定叶子节点生成包含证明（Inclusion Proof）
- **快速验证**：使用 O(log n) 复杂度验证叶子是否属于树根
- **简洁 API**：开箱即用，无第三方依赖（仅标准库）

## 🚀 快速开始

### 环境要求
- Python 3.7+
- 无需额外依赖

### 安装与运行

1. 克隆仓库
```bash
git clone https://github.com/你的账户/merkle-tree003.git
cd merkle-tree003
```

2. 运行示例
```bash
# 使用默认数据（a, b, c, d, e），验证索引 2 的叶子
python examples/demo.py

# 自定义叶子数据，验证索引 1
python examples/demo.py apple banana cherry 1
```

### 基本用法

```python
from src.merkle.tree import MerkleTree, verify_proof

# 构建树
leaves = ["transaction1", "transaction2", "transaction3", "transaction4"]
tree = MerkleTree(leaves)

# 获取根哈希
root = tree.root_hex
print(f"Root: {root}")

# 生成证明（证明索引 2 的叶子存在）
proof = tree.get_proof(2)
print(f"Proof: {proof}")

# 验证证明
is_valid = verify_proof(leaves[2], proof, root)
print(f"Valid: {is_valid}")  # True
```

## 📂 项目结构

```
merkle-tree003/
├── src/
│   └── merkle/
│       ├── __init__.py       # 模块导出
│       └── tree.py           # 核心实现：MerkleTree 类与验证函数
├── examples/
│   └── demo.py               # 命令行示例程序
├── LICENSE                   # MIT 许可证
└── README.md                 # 项目说明文档
```

## 🔧 核心 API

### `MerkleTree`
- **`__init__(leaves)`**：从叶子列表构建树
- **`root`**：返回根哈希（bytes）
- **`root_hex`**：返回根哈希的十六进制字符串
- **`leaf_count`**：叶子数量
- **`get_proof(index)`**：生成指定索引叶子的证明
- **`verify_proof(leaf, proof, root_hex)`**：静态方法，验证证明

### `verify_proof(leaf, proof, root_hex)`
独立函数，验证给定叶子、证明与根哈希的有效性。

## 🎯 应用场景

- **区块链**：比特币 SPV 轻客户端、以太坊状态证明
- **分布式存储**：IPFS、Git 对象校验
- **审计与合规**：可信时间戳、日志完整性验证
- **教学演示**：密码学、数据结构课程实验

## 🤝 贡献指南

欢迎提交 Issue 与 Pull Request！参与流程：

1. Fork 本仓库
2. 创建功能分支：`git checkout -b feature/your-feature`
3. 提交代码：`git commit -m "feat: add your feature"`
4. 推送分支：`git push origin feature/your-feature`
5. 提交 Pull Request

### 开发建议
- 遵循 PEP 8 代码风格
- 为新功能添加单元测试
- 更新相关文档

## 📜 许可证

本项目采用 [MIT License](LICENSE) 开源。


## 🎓 致谢

本项目为成都信息工程大学开源文化课程大作业，感谢老师与同学的支持与反馈。

---

**Star ⭐ 本项目以支持开源学习！**
