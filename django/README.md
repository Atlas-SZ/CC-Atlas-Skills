# Django Skill

Django/DRF 开发最佳实践技能包。

## 功能

涵盖 Django 开发的核心技能：

- **模型设计** (`model-design.md`) - 数据模型设计规范
- **DRF API** (`drf-api.md`) - Django REST Framework API 开发
- **ORM 优化** (`orm-optimization.md`) - 查询优化与性能调优
- **安全** (`security.md`) - 安全最佳实践
- **Admin 配置** (`admin-config.md`) - Django Admin 定制
- **导入导出** (`import-export.md`) - 数据导入导出
- **测试** (`testing.md`) - 测试策略与工具
- **部署** (`deployment.md`) - 生产环境部署
- **代码生成** (`code-generation.md`) - 代码生成工具
- **约束** (`constraints.md`) - 开发约束与规范
- **检查清单** (`checklist.md`) - 质量检查清单

## 使用方法

在 Claude Code 中调用：

```bash
/django
```

或在对话中自动触发（当检测到 Django 相关任务时）。

## 目录结构

```
django/
├── SKILL.md              # 主入口文件
├── README.md             # 本文件
├── *.md                  # 各功能模块文档
├── scripts/              # 辅助脚本
│   └── create-app.sh     # Django app 创建脚本
├── examples/             # 示例代码
│   ├── viewset-example.py      # ViewSet 标准示例
│   ├── serializer-example.py   # Serializer 标准示例
│   └── filters-example.py      # FilterSet 标准示例
└── workflows/            # 工作流定义
    └── new-feature.md    # 新功能开发工作流
```

## 安装

```bash
# 从项目根目录
cd CC-Atlas-Skills
ln -sf "$(pwd)/django" ~/.claude/skills/django

# 验证
ls -l ~/.claude/skills/django
```

## 快速开始

### 1. 创建 Django 项目

```bash
# 创建项目
django-admin startproject myproject
cd myproject

# 安装依赖
uv add djangorestframework django-filter djangorestframework-simplejwt

# 创建 app（使用辅助脚本）
./path/to/django/scripts/create-app.sh users
```

### 2. 参考示例代码

- `examples/viewset-example.py` - ViewSet 标准写法
- `examples/serializer-example.py` - Serializer 标准写法
- `examples/filters-example.py` - FilterSet 标准写法

### 3. 遵循工作流

参考 `workflows/new-feature.md` 进行新功能开发。

## 适用场景

- 开发 Django 项目或 DRF API
- 遇到性能/安全问题时
- 需要代码生成或模板时
- 设计数据模型时

## 依赖

- Python 3.10+
- Django 5.x
- Django REST Framework 3.x

## 更新日期

2026-01-11
