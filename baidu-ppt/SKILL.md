---
name: baidu-ppt
description: |
  百度智能 PPT 生成工具，集成百度智能云千帆 AI PPT API。

  触发场景：
  - 用户需要根据主题或大纲生成 PPT
  - 用户需要生成演示文稿
  - 用户明确提及"生成PPT"、"智能PPT"、"AI PPT"
---

# 百度智能 PPT

基于百度千帆 AI PPT API 生成专业演示文稿，支持大纲生成、模板选择、PPT导出。

## 快速开始

```bash
# 列出可用模板
python scripts/baidu_ppt.py --list-themes

# 生成大纲
python scripts/baidu_ppt.py outline "人工智能发展趋势" --pages 10

# 生成 PPT
python scripts/baidu_ppt.py generate "人工智能发展趋势" \
  --title "AI发展趋势报告" \
  --style-id 0 \
  --tpl-id 102322 \
  --output report.pptx
```

## 环境配置

设置环境变量：

```bash
export BAIDU_API_KEY="your-api-key"
```

API Key 从 [百度智能云千帆平台](https://qianfan.baidubce.com) 获取。

## 命令参数

### outline - 生成大纲

| 参数 | 说明 |
|------|------|
| `query` | 主题描述 |
| `--pages` | 页数范围 (1-10, 11-20, 21-30, 31-40) |
| `--layout` | 布局: 1(简约) 或 2(专业) |
| `--resource` | 资源文件URL |
| `--gen-mode` | 模式: 1(智能润色) 或 2(严格依从) |

### generate - 生成PPT

| 参数 | 说明 |
|------|------|
| `query` | 主题描述 |
| `--title` | PPT标题 |
| `--style-id` | 样式ID |
| `--tpl-id` | 模板ID |
| `--chat-id` | 会话ID (从outline获取) |
| `--query-id` | 查询ID (从outline获取) |
| `--outline` | 大纲内容 (Markdown格式) |
| `--output` | 保存到文件 |

### 其他命令

| 命令 | 说明 |
|------|------|
| `--list-themes` | 列出可用模板 |
| `--download <url>` | 下载PPT文件 |

## 使用示例

### 完整工作流

```bash
# 1. 查看模板
python scripts/baidu_ppt.py --list-themes

# 2. 生成大纲
python scripts/baidu_ppt.py outline "人工智能发展趋势" --pages 10

# 3. 使用返回的 chat_id/query_id/outline 生成 PPT
python scripts/baidu_ppt.py generate "人工智能发展趋势" \
  --title "AI发展趋势报告" \
  --style-id 0 \
  --tpl-id 102322 \
  --chat-id 237216140951210 \
  --query-id 283210412321210 \
  --outline "# 人工智能发展趋势\n* 核心技术演进\n  * 机器学习算法突破\n..." \
  --output ai_report.pptx
```

## API 参考

详细参数说明见 [references/api.md](references/api.md)。

## 注意事项

- 生成大纲后需保存返回的 `chat_id` 和 `query_id`
- PPT 生成使用 SSE 流式响应，耗时较长
- 支持 1-40 页的 PPT 生成
