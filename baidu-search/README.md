# Baidu Search Skill

百度 AI 搜索技能，集成百度智能云千帆 AI Search API，用于搜索中文互联网实时信息。

## 功能特性

- **多类型搜索**: 支持网页、视频、图片、阿拉丁搜索
- **站点过滤**: 限定或屏蔽特定站点
- **时效过滤**: 按时间范围筛选结果
- **结构化输出**: 返回标题、URL、摘要、日期等

## 环境要求

- Python 3.8+
- 百度智能云千帆 API Key

## 安装

### 方式 1: 通过 Marketplace 安装

```bash
claude plugin install baidu-search@cc-atlas-skills
```

### 方式 2: 本地安装

```bash
# 克隆仓库
git clone https://github.com/Atlas-SZ/CC-Atlas-Skills.git

# 创建软链接
ln -sf "$(pwd)/baidu-search" ~/.claude/skills/baidu-search
```

## 配置

设置环境变量：

```bash
# 添加到 ~/.zshrc 或 ~/.bashrc
export BAIDU_API_KEY="your-api-key"
```

获取 API Key:
1. 访问 [百度智能云千帆平台](https://qianfan.baidubce.com)
2. 开通 AI Search 服务
3. 创建应用获取 API Key

## 使用方法

### 在 Claude Code 中使用

```
/baidu-search
> 帮我搜索今日北京天气
```

### 命令行直接调用

```bash
# 基础搜索
python scripts/baidu_search.py "北京天气预报"

# 限定站点
python scripts/baidu_search.py "Python教程" --site runoob.com

# 时效过滤
python scripts/baidu_search.py "今日新闻" --recency week

# 多类型搜索
python scripts/baidu_search.py "猫咪" --type web --type image --top-k 5

# 输出 JSON
python scripts/baidu_search.py "AI发展趋势" --json --output results.json
```

## 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `query` | 搜索查询词 | (必填) |
| `--api-key` | API Key | 环境变量 `BAIDU_API_KEY` |
| `--edition` | 搜索版本: standard/lite | standard |
| `--top-k` | 返回结果数量 | 10 |
| `--site` | 限定站点 | - |
| `--block` | 屏蔽站点 | - |
| `--safe` | 开启安全搜索 | false |
| `--recency` | 时效: week/month/semiyear/year | - |
| `--type` | 类型: web/video/image/aladdin | web |
| `--json` | 输出原始 JSON | false |
| `--output` | 保存到文件 | - |

## 计费说明

- 每日免费额度: 100 次
- 按量后付费支持
- 每账号每日上限: 100,000 次

## 注意事项

- Query 长度限制 72 字符（中文按 2 字符计）
- 站点过滤为付费功能（限时免费）
- 阿拉丁结果不支持站点/时效过滤

## License

MIT License
