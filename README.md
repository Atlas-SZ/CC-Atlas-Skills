# CC-Atlas-Skills

Claude Code Skills 集合仓库。

## 项目简介

这是一个 Claude Code 的 skills 集合仓库，提供高质量的开发技能包。

## 快速安装

### 方式 1：通过 GitHub 安装（推荐）

推送到 GitHub 后，用户可以：

```bash
# 1. 添加 marketplace
claude plugin marketplace add Atlas-SZ/CC-Atlas-Skills

# 2. 安装 django skill
claude plugin install django@cc-atlas-skills

# 3. 验证安装
claude plugin list
```

### 方式 2：手动软链接安装

```bash
# 克隆仓库
git clone https://github.com/Atlas-SZ/CC-Atlas-Skills.git
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

---

### excalidraw-diagram

**描述**：从文本内容生成 Excalidraw 图表（Obsidian 格式）

**功能**：
- 🎨 流程图生成 - 支持复杂流程和决策路径
- 🧠 思维导图 - 放射状结构，清晰层级
- 📊 层级图 - 组织架构、分类结构
- 🔗 关系图 - 实体关系、网络连接
- 📈 对比图 - 方案对比、优劣分析
- ⏱️ 时间线图 - 项目进度、历史演进
- 📐 矩阵图 - 多维度分析
- 🎯 自由布局 - 灵活的空间组织

**特点**：
- 自动生成 Obsidian 兼容的 .md 文件
- 智能布局算法确保图表清晰易读
- 支持中英文内容
- 一键保存到工作目录

**安装**：
```bash
# GitHub 安装
claude plugin install excalidraw-diagram@cc-atlas-skills

# 或手动安装
ln -sf "$(pwd)/excalidraw-diagram" ~/.claude/skills/excalidraw-diagram
```

**使用**：`/excalidraw-diagram` 或在对话中提及"画图"、"流程图"、"思维导图"等关键词

---

### mermaid-visualizer

**描述**：将文本内容转换为专业的 Mermaid 图表

**功能**：
- 📊 流程图 - Process Flow（垂直/水平布局）
- 🔄 循环流程 - Circular Flow（迭代、反馈系统）
- ⚖️ 对比图 - Comparison（方案对比）
- 🧠 思维导图 - Mindmap（层级结构）
- 📞 时序图 - Sequence Diagram（交互流程）
- 🔀 状态图 - State Diagram（状态转换）

**特点**：
- 内置语法错误预防机制（列表冲突、subgraph 命名、空格问题）
- 适配 Obsidian 和 GitHub 渲染环境
- 多种配色风格（Minimal, Professional, Colorful）
- 智能选择最佳可视化方案

**安装**：
```bash
# GitHub 安装
claude plugin install mermaid-visualizer@cc-atlas-skills

# 或手动安装
ln -sf "$(pwd)/mermaid-visualizer" ~/.claude/skills/mermaid-visualizer
```

**使用**：`/mermaid-visualizer` 或在对话中提及"Mermaid 图表"、"流程图"等关键词

---

### obsidian-canvas-creator

**描述**：从文本内容创建 Obsidian Canvas 文件

**功能**：
- 🌟 MindMap 布局 - 放射状思维导图，清晰层级关系
- 🎨 Freeform 布局 - 自由空间组织，灵活连接
- 🔗 智能连接 - 自动建立节点关系
- 📐 布局算法 - 自动计算最佳节点位置
- 💾 Canvas 格式 - 完整的 JSON Canvas 规范支持

**特点**：
- 支持两种布局模式（MindMap 和 Freeform）
- 自动生成 .canvas 格式文件
- 智能布局算法避免节点重叠
- 完全兼容 Obsidian Canvas 插件

**安装**：
```bash
# GitHub 安装
claude plugin install obsidian-canvas-creator@cc-atlas-skills

# 或手动安装
ln -sf "$(pwd)/obsidian-canvas-creator" ~/.claude/skills/obsidian-canvas-creator
```

**使用**：`/obsidian-canvas-creator` 或在对话中提及"Canvas"、"画布"、"空间布局"等关键词

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
git remote add origin https://github.com/Atlas-SZ/CC-Atlas-Skills.git
git push -u origin main
```

### 2. 用户安装

推送到 GitHub 后，用户可以通过以下方式安装：

```bash
# GitHub 短链接（推荐）
claude plugin marketplace add Atlas-SZ/CC-Atlas-Skills

# 完整 HTTPS URL
claude plugin marketplace add https://github.com/Atlas-SZ/CC-Atlas-Skills

# SSH URL
claude plugin marketplace add git@github.com:Atlas-SZ/CC-Atlas-Skills.git
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

- GitHub: https://github.com/Atlas-SZ/CC-Atlas-Skills
- 问题反馈: https://github.com/Atlas-SZ/CC-Atlas-Skills/issues
