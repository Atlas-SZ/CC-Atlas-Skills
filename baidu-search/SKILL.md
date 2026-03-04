---
name: baidu-search
description: |
  百度 AI 搜索工具，集成百度智能云千帆 AI Search API。
  用于搜索中文互联网实时信息，返回标题、URL、内容摘要等结构化结果。

  触发场景：
  - 用户需要搜索中文内容或中国网站信息
  - 需要实时新闻、天气、资讯等时效性信息
  - 需要限定站点搜索（如仅搜索百度百科、天气网等）
  - 用户明确提及"百度搜索"、"搜索中文内容"、"在中国网站上找"
---

# 百度搜索

通过百度千帆 AI Search API 执行网页、视频、图片搜索。

## 快速开始

```bash
# 基础搜索
python scripts/baidu_search.py "北京天气预报"

# 限定站点
python scripts/baidu_search.py "Python教程" --site runoob.com

# 时效过滤
python scripts/baidu_search.py "今日新闻" --recency week

# 输出 JSON
python scripts/baidu_search.py "AI发展趋势" --json
```

## 环境配置

设置环境变量：

```bash
export BAIDU_API_KEY="your-api-key"
```

API Key 从 [百度智能云千帆平台](https://qianfan.baidubce.com) 获取。

## 命令参数

| 参数 | 说明 |
|------|------|
| `query` | 搜索查询词 |
| `--api-key` | API Key (优先于环境变量) |
| `--edition` | `standard`(完整) 或 `lite`(快速) |
| `--top-k` | 返回结果数量，默认10 |
| `--site` | 限定站点 (可多次使用) |
| `--block` | 屏蔽站点 (可多次使用) |
| `--safe` | 开启安全搜索 |
| `--recency` | 时效: week/month/semiyear/year |
| `--type` | 类型: web/video/image/aladdin |
| `--json` | 输出原始 JSON |
| `--output` | 保存到文件 |

## 使用示例

### 基础网页搜索

```bash
python scripts/baidu_search.py "北京有哪些旅游景区"
```

### 多类型搜索

```bash
python scripts/baidu_search.py "猫咪" --type web --type image --top-k 5
```

### 限定站点 + 时效

```bash
python scripts/baidu_search.py "今日天气" --site weather.com.cn --recency week
```

### 快速模式

```bash
python scripts/baidu_search.py "新闻" --edition lite --top-k 5
```

## API 参考

详细参数说明见 [references/api.md](references/api.md)。

## 注意事项

- Query 长度限制 72 字符（中文按 2 字符计）
- 每日免费额度 100 次
- 站点过滤为付费功能（限时免费）
- 阿拉丁结果不支持站点/时效过滤
