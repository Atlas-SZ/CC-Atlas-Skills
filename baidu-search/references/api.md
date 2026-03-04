# 百度 AI Search API 参考

## 端点

```
POST https://qianfan.baidubce.com/v2/ai_search/web_search
```

## 认证

Header: `Authorization: Bearer <API Key>`

从百度智能云千帆平台获取 API Key。

## 请求参数

### Body 参数

| 参数 | 类型 | 必须 | 说明 |
|------|------|------|------|
| `messages` | array | 是 | 搜索输入，单轮对话格式 |
| `search_source` | string | 否 | 固定值 `baidu_search_v2` |
| `edition` | string | 否 | `standard`(完整) 或 `lite`(快速) |
| `resource_type_filter` | array | 否 | 资源类型配置 |
| `search_filter` | object | 否 | 搜索过滤条件 |
| `block_websites` | array | 否 | 屏蔽站点列表 (最多20个) |
| `safe_search` | boolean | 否 | 安全搜索开关 |
| `search_recency_filter` | string | 否 | 时效过滤 |

### resource_type_filter

```json
[
  {"type": "web", "top_k": 20},      // 网页，最大50
  {"type": "video", "top_k": 0},     // 视频，最大10
  {"type": "image", "top_k": 0},     // 图片，最大30
  {"type": "aladdin", "top_k": 0}    // 阿拉丁，最大5
]
```

### search_recency_filter 枚举

| 值 | 含义 |
|----|------|
| `week` | 最近7天 |
| `month` | 最近30天 |
| `semiyear` | 最近180天 |
| `year` | 最近365天 |

### search_filter.match

```json
{
  "match": {
    "site": ["www.weather.com.cn", "baike.baidu.com"]
  }
}
```

## 响应结构

```json
{
  "request_id": "string",
  "references": [
    {
      "id": 1,
      "title": "网页标题",
      "url": "https://...",
      "content": "内容摘要...",
      "date": "2025-01-01",
      "website": "站点名称",
      "type": "web",
      "rerank_score": 0.95,
      "authority_score": 0.88
    }
  ]
}
```

## 错误码

| 码 | 说明 |
|----|------|
| 400 | 请求参数错误 |
| 500 | 服务端错误 |
| 501 | 模型服务超时 |
| 502 | 流式输出超时 |

## 计费

- 每日免费额度: 100次
- 按量后付费支持
- 每账号每日上限: 100,000次
