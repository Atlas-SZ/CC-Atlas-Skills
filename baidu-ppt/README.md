# Baidu PPT Skill

百度智能 PPT 生成技能，集成百度智能云千帆 AI PPT API，基于大纲自动生成专业演示文稿。

## 功能特性

- **大纲生成**: 基于主题自动生成结构化大纲
- **PPT生成**: 基于大纲生成完整演示文稿
- **模板选择**: 多种风格模板可选
- **资源上传**: 支持文档/图片作为素材

## 环境要求

- Python 3.8+
- 百度智能云千帆 API Key

## 安装

### 方式 1: 通过 Marketplace 安装

```bash
claude plugin install baidu-ppt@cc-atlas-skills
```

### 方式 2: 本地安装

```bash
# 克隆仓库
git clone https://github.com/Atlas-SZ/CC-Atlas-Skills.git

# 创建软链接
ln -sf "$(pwd)/baidu-ppt" ~/.claude/skills/baidu-ppt
```

## 配置

设置环境变量：

```bash
# 添加到 ~/.zshrc 或 ~/.bashrc
export BAIDU_API_KEY="your-api-key"
```

获取 API Key:
1. 访问 [百度智能云千帆平台](https://qianfan.baidubce.com)
2. 开通 AI PPT 服务
3. 创建应用获取 API Key

## 使用方法

### 在 Claude Code 中使用

```
/baidu-ppt
> 帮我生成一个关于人工智能发展趋势的PPT
```

### 命令行使用

```bash
# 1. 查看可用模板
python scripts/baidu_ppt.py --list-themes

# 2. 生成大纲
python scripts/baidu_ppt.py outline "人工智能发展趋势" --pages 10

# 3. 生成 PPT (使用步骤2返回的 chat_id/query_id)
python scripts/baidu_ppt.py generate "人工智能发展趋势" \
  --title "AI发展趋势报告" \
  --style-id 0 \
  --tpl-id 102322 \
  --chat-id <从步骤2获取> \
  --query-id <从步骤2获取> \
  --outline-file outline.md \
  --output report.pptx
```

### 一键生成

如果已有大纲文件，```bash
# 直接生成 PPT
python scripts/baidu_ppt.py generate "主题" \
  --title "标题" \
  --tpl-id 102322 \
  --chat-id xxx \
  --query-id xxx \
  --outline-file outline.md \
  --output output.pptx
```

## 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `query` | 主题描述 | (必填) |
| `--title` | PPT标题 | (生成时必填) |
| `--pages` | 页数范围 | 1-10 |
| `--layout` | 布局: 1(简约)/2(专业) | 2 |
| `--style-id` | 样式ID | 0 |
| `--tpl-id` | 模板ID | (生成时必填) |
| `--gen-mode` | 模式: 1(智能润色)/2(严格依从) | 1 |

## 计费说明

- 每日免费额度: 100 次
- 按量后付费支持

## 注意事项

- 生成大纲后需保存 `chat_id` 和 `query_id`
- PPT 生成使用 SSE 流式响应
耗时较长
- 支持 1-40 页的 PPT 生成

## License

MIT License
