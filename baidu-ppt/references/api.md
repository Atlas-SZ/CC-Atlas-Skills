# 百度智能 PPT API 参考

## 端点

| 接口 | URL |
|------|------|
| 获取模板 | `POST /v2/tools/ai_ppt/get_ppt_theme` |
| 生成大纲 | `POST /v2/tools/ai_ppt/generate_outline` |
| 生成PPT | `POST /v2/tools/ai_ppt/generate_ppt_by_outline` |

## 认证

Header: `Authorization: Bearer <API Key>`

## 获取模板

### 响应结构

```json
{
  "errno": 0,
  "data": {
    "ppt_themes": [
      {
        "style_id": 0,
        "tpl_id": 102322,
        "style_name_list": ["简约商务"],
        "color_list": ["#2A73E8", "#03B668"],
        "main_img_url": "..."
      }
    ]
  }
}
```

## 生成大纲

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `query` | string | 是 | 主题描述 |
| `page_range` | string | 否 | 页数范围: 1-10, 11-20, 21-30, 31-40 |
| `layout` | int | 否 | 布局: 1(简约) 或 2(专业) |
| `language_option` | string | 否 | 语言: default |
| `gen_mode` | int | 否 | 模式: 1(智能润色) 或 2(严格依从) |
| `resource_url` | string | 否 | 资源文件URL |

### 响应结构 (SSE)

```json
{
  "chat_id": 237216140951210,
  "query_id": 283210412321210,
  "outline": "# 标题\n* 章节1\n  * 内容...",
  "is_end": false,
  "status": "大纲生成中"
}
```

## 生成 PPT

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `query` | string | 是 | 主题描述 |
| `title` | string | 是 | PPT标题 |
| `outline` | string | 是 | 大纲内容 (Markdown) |
| `chat_id` | int | 是 | 会话ID (从大纲获取) |
| `query_id` | int | 是 | 查询ID (从大纲获取) |
| `style_id` | int | 是 | 样式ID |
| `tpl_id` | int | 是 | 模板ID |
| `resource_url` | string | 否 | 资源文件URL |
| `custom_tpl_url` | string | 否 | 自定义模板URL |
| `gen_mode` | int | 否 | 模式: 1(智能润色) 或 2(严格依从) |
| `ai_info` | bool | 否 | 是否显示AI生成信息 |

### 响应结构 (SSE)

```json
{
  "status": "PPT生成中",
  "page_count": 1,
  "bd_ppt_json": "...",
  "is_end": false
}
```

最终响应包含:

```json
{
  "status": "PPT导出结束",
  "data": {
    "pptx_url": "https://..."
  },
  "is_end": true
}
```

## 大纲格式 (Markdown)

```markdown
# 主标题
* 章节标题1
  * 子内容1
  * 子内容2
* 章节标题2
  * 子内容
```

## 计费

- 每日免费额度: 100 次
- 按量后付费支持
