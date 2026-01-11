# CC-Atlas-Skills

Claude Code Skills 集合仓库。

## 项目简介

这是一个 Claude Code 的 skills 集合仓库，提供高质量的开发技能包。

## 快速安装

### 方式 1：通过 GitHub 安装（推荐）

推送到 GitHub 后，用户可以：

```bash
# 1. 添加 marketplace（替换为你的 GitHub 用户名）
claude plugin marketplace add your-username/CC-Atlas-Skills

# 2. 安装 django skill
claude plugin install django@cc-atlas-skills

# 3. 验证安装
claude plugin list
```

### 方式 2：手动软链接安装

```bash
# 克隆仓库
git clone https://github.com/your-username/CC-Atlas-Skills.git
cd CC-Atlas-Skills

# 安装单个 skill
ln -sf "$(pwd)/django" ~/.claude/skills/django

# 验证
ls -l ~/.claude/skills/django
```

## 使用 Skills

在 Claude Code 中：

```bash
# 调用 django skill
/django

# 或在对话中自动触发
"我需要创建一个 Django API..."
```

## 可用 Skills

### django

**描述**：Django/DRF 开发最佳实践技能包

**功能**：
- 📐 模型设计规范 - 字段选择、关系设计、索引优化
- 🚀 DRF API 开发 - ViewSet、Serializer、Filter 标准模式
- ⚡ ORM 优化 - N+1 问题、查询优化、性能调优
- 🔒 安全最佳实践 - 认证、权限、OWASP 防护
- ⚙️ Django Admin 定制 - 自定义界面、权限控制
- 📦 数据导入导出 - Excel/CSV 导入导出方案
- ✅ 测试策略 - 单元测试、集成测试、覆盖率
- 🚢 生产部署 - Docker、Gunicorn、Nginx 配置
- 🤖 代码生成 - App 创建、API 生成脚本
- 📋 质量检查清单 - 代码审查要点

**安装**：
```bash
# GitHub 安装
claude plugin install django@cc-atlas-skills

# 或手动安装
ln -sf "$(pwd)/django" ~/.claude/skills/django
```

**使用**：`/django`

**详细文档**：[django/README.md](django/README.md)

## 项目结构

```
CC-Atlas-Skills/
├── .claude-plugin/
│   └── marketplace.json      # Marketplace 配置
├── django/                   # Django skill
│   ├── SKILL.md              # Skill 主入口
│   ├── skill.json            # Skill 元数据
│   ├── README.md             # Skill 文档
│   ├── *.md                  # 功能模块文档
│   ├── scripts/              # 辅助脚本
│   │   └── create-app.sh
│   ├── examples/             # 示例代码
│   │   ├── viewset-example.py
│   │   ├── serializer-example.py
│   │   └── filters-example.py
│   └── workflows/            # 工作流
│       └── new-feature.md
├── .gitignore
└── README.md                 # 本文件
```

## 卸载 Skill

```bash
# 通过 plugin 卸载
claude plugin uninstall django

# 或手动删除软链接
rm ~/.claude/skills/django
```

## 更新 Skill

```bash
# 更新 marketplace
claude plugin marketplace update cc-atlas-skills

# 更新特定 skill
claude plugin update django
```

## 开发新 Skill

### 1. 创建 Skill 目录

```bash
mkdir my-skill
cd my-skill
```

### 2. 创建必需文件

**SKILL.md** - Skill 主入口（必需）：
```markdown
---
name: my-skill
description: Skill 描述
---

# My Skill

## 使用场景
描述何时使用此 skill

## 核心功能
- 功能 1
- 功能 2

## 工作流程
1. 步骤 1
2. 步骤 2

## 示例
使用示例
```

**skill.json** - 元数据（可选，但推荐）：
```json
{
  "name": "my-skill",
  "version": "1.0.0",
  "description": "Skill 描述",
  "tags": ["tag1", "tag2"],
  "features": ["功能1", "功能2"]
}
```

**推荐目录结构**：
```
my-skill/
├── SKILL.md           # 必需
├── skill.json         # 推荐
├── README.md          # 推荐
├── scripts/           # 可选：辅助脚本
├── examples/          # 可选：示例代码
└── workflows/         # 可选：工作流定义
```

### 3. 添加到 Marketplace

编辑 `.claude-plugin/marketplace.json`，添加新 skill：

```json
{
  "name": "cc-atlas-skills",
  "owner": {
    "name": "CC-Atlas"
  },
  "plugins": [
    {
      "name": "my-skill",
      "version": "1.0.0",
      "description": "Skill 描述",
      "tags": ["tag1", "tag2"],
      "source": {
        "type": "directory",
        "path": "my-skill"
      }
    }
  ]
}
```

### 4. 测试

```bash
# 本地测试
ln -sf "$(pwd)/my-skill" ~/.claude/skills/my-skill

# 在 Claude Code 中使用
/my-skill
```

## 发布到 GitHub

### 1. 创建 GitHub 仓库

```bash
# 初始化 git（如果还没有）
git init
git add .
git commit -m "Initial commit"

# 关联远程仓库
git remote add origin https://github.com/your-username/CC-Atlas-Skills.git
git push -u origin main
```

### 2. 用户安装

推送到 GitHub 后，用户可以通过以下方式安装：

```bash
# GitHub 短链接（推荐）
claude plugin marketplace add your-username/CC-Atlas-Skills

# 完整 HTTPS URL
claude plugin marketplace add https://github.com/your-username/CC-Atlas-Skills

# SSH URL
claude plugin marketplace add git@github.com:your-username/CC-Atlas-Skills.git
```

然后安装 skill：
```bash
claude plugin install django@cc-atlas-skills
```

## 贡献

欢迎贡献新 skills！

1. Fork 本项目
2. 创建新 skill 目录
3. 按标准结构添加内容
4. 更新 `.claude-plugin/marketplace.json`
5. 提交 Pull Request

## 许可证

MIT License

## 更新日期

2026-01-11

## 链接

- GitHub: https://github.com/your-username/CC-Atlas-Skills
- 问题反馈: https://github.com/your-username/CC-Atlas-Skills/issues

---

**注意**：将 README 中的 `your-username` 替换为你的 GitHub 用户名后再推送到 GitHub。
