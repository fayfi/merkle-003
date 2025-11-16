# 开源文化课程大作业进度清单

> 本文档用于跟踪作业完成度与证据链接，便于随时检查与汇报。项目主题：默克尔树（Merkle Tree）。

## 任务状态（逐项勾选）
- [ ] 整理并本地运行默克尔树项目（确保示例可跑、输出根哈希与证明验证结果）
- [ ] 在 GitHub 创建仓库并推送（仓库命名：项目名_学号后两位）
- [ ] 选择并添加开源许可证（MIT / Apache-2.0 / GPL-3.0）
- [ ] 完成 README 基本内容（简介 / 安装与运行 / 使用示例 / 贡献指引 / 许可证）
- [ ] 分支管理演示：创建 feature 分支 → 合并 → 制造并解决冲突（保留合并记录）
- [ ] 邀请同学互动：Issue / Star / Watch（记录链接与截图）
- [ ] “华为五看三定”分析完成并发布（README 章节或新建 Issue）
- [ ] 可选加分：添加 1-3 个单元测试与 GitHub Actions CI
- [ ] 发布 v1.0.0 Release，并整理提交材料与截图

---

## 简要指引（必要时参考）

### 1. 初始化与推送（在本地项目根目录）
```bash
# 初始化并首推（示例）
git init
git add .
git commit -m "init: import merkle tree project"
git branch -M main
# 将下面的 URL 替换为你的 GitHub 仓库地址
git remote add origin https://github.com/<your-account>/merkle-tool_<学号后两位>.git
git push -u origin main
```

### 2. 分支管理演示
```bash
# 创建并开发功能分支
git checkout -b feature/proof-api
# ...在代码中增加/修改接口...
git commit -am "feat: add proof api"

# 回到主分支并制造冲突
git checkout main
# ...在同一文件同一行做不同修改...
git commit -am "chore: change demo line on main"

# 合并并解决冲突
git merge feature/proof-api
# 编辑冲突文件，保留正确逻辑
git add <冲突已解决的文件>
git commit
```

### 3. 许可证选择
- MIT：最宽松，适合课程作业与传播。
- Apache-2.0：宽松且包含专利授权条款。
- GPL-3.0：强 Copyleft，强调开源衍生必须开源。

> 在仓库根目录添加 `LICENSE` 文件，并在 `README` 中注明许可证名称。

### 4. 可选加分：测试与 CI
- 在 `tests/` 下添加基础单元测试：构建树、生成证明、验证证明。
- 在 `.github/workflows/ci.yml` 配置简单构建与测试流程（按项目语言选择官方模板）。

---

## 证据链接与截图记录（按项填充）
- 仓库首页链接：
- 许可证文件链接：
- README 链接：
- 分支合并与冲突解决记录（提交/PR 链接）：
- 同学互动：Issue/Star/Watch 链接：
- CI 状态链接：
- Release v1.0.0 链接：

> 建议粘贴具体 URL，并在必要处附简短说明或截图文件名。

---

## “五看三定”分析模板（可直接填写）
### 五看
1. 行业/趋势：
2. 市场/客户：
3. 竞争：
4. 自己：
5. 机会：

### 三定
1. 定战略控制点：
2. 定目标（SMART）：
3. 定策略：

---

## 更新方法
- 每完成一项，就将上面的复选框打勾，并在“证据链接与截图记录”段落补充链接/说明。
- 若分析或文档以 Issue 形式发布，请在此处贴对应 Issue 链接。
- 如需我补充 README 模板、测试样例或 CI 模板，请告知项目语言与运行方式。
