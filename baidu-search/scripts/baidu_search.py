#!/usr/bin/env python3
"""
百度 AI Search API 调用脚本
集成百度智能云千帆 AI Search，支持网页/视频/图片搜索
"""
from __future__ import annotations

import argparse
import json
import os
from typing import Any
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


def search(
    query: str,
    api_key: str | None = None,
    search_source: str = "baidu_search_v2",
    edition: str = "standard",
    resource_types: list[dict] | None = None,
    site_filter: list[str] | None = None,
    block_websites: list[str] | None = None,
    safe_search: bool = False,
    recency_filter: str | None = None,
    top_k: int = 10,
) -> dict[str, Any]:
    """
    执行百度搜索

    Args:
        query: 搜索查询词
        api_key: API Key，若不提供则从环境变量 BAIDU_API_KEY 获取
        search_source: 搜索引擎版本，默认 baidu_search_v2
        edition: 搜索版本，standard(完整) 或 lite(简化，更快)
        resource_types: 资源类型配置 [{"type": "web", "top_k": 10}]
        site_filter: 站点过滤，仅搜索指定站点
        block_websites: 屏蔽站点列表
        safe_search: 是否开启安全搜索
        recency_filter: 时效过滤 (week/month/semiyear/year)
        top_k: 默认网页返回数量

    Returns:
        API 响应字典
    """
    api_key = api_key or os.environ.get("BAIDU_API_KEY")
    if not api_key:
        raise ValueError("API Key 未设置，请通过参数或环境变量 BAIDU_API_KEY 提供")

    # 构建请求体
    if resource_types is None:
        resource_types = [{"type": "web", "top_k": top_k}]

    body: dict[str, Any] = {
        "messages": [{"content": query[:72], "role": "user"}],
        "search_source": search_source,
        "resource_type_filter": resource_types,
    }

    if edition != "standard":
        body["edition"] = edition

    if site_filter:
        body["search_filter"] = {"match": {"site": site_filter}}

    if block_websites:
        body["block_websites"] = block_websites

    if safe_search:
        body["safe_search"] = True

    if recency_filter:
        body["search_recency_filter"] = recency_filter

    # 发送请求
    url = "https://qianfan.baidubce.com/v2/ai_search/web_search"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    req = Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers=headers,
        method="POST",
    )

    try:
        with urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else ""
        return {
            "error": True,
            "status_code": e.code,
            "message": error_body or str(e),
        }
    except URLError as e:
        return {"error": True, "message": f"网络错误: {e.reason}"}


def format_results(response: dict[str, Any]) -> str:
    """格式化搜索结果为可读文本"""
    if response.get("error"):
        return f"搜索失败: {response.get('message', '未知错误')}"

    references = response.get("references", [])
    if not references:
        return "未找到相关结果"

    lines = []
    for ref in references:
        lines.append(f"## [{ref.get('id')}] {ref.get('title', '无标题')}")
        lines.append(f"**URL**: {ref.get('url', '')}")
        if ref.get("date"):
            lines.append(f"**日期**: {ref.get('date')}")
        if ref.get("website"):
            lines.append(f"**来源**: {ref.get('website')}")
        if ref.get("content"):
            lines.append(f"**摘要**: {ref.get('content')[:500]}...")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="百度 AI 搜索")
    parser.add_argument("query", help="搜索查询词")
    parser.add_argument("--api-key", help="API Key (或设置环境变量 BAIDU_API_KEY)")
    parser.add_argument("--edition", choices=["standard", "lite"], default="standard",
                        help="搜索版本: standard(完整) 或 lite(快速)")
    parser.add_argument("--top-k", type=int, default=10, help="返回结果数量")
    parser.add_argument("--site", action="append", help="限定站点 (可多次使用)")
    parser.add_argument("--block", action="append", help="屏蔽站点 (可多次使用)")
    parser.add_argument("--safe", action="store_true", help="开启安全搜索")
    parser.add_argument("--recency", choices=["week", "month", "semiyear", "year"],
                        help="时效过滤")
    parser.add_argument("--type", action="append",
                        choices=["web", "video", "image", "aladdin"],
                        help="搜索类型 (可多次使用，默认 web)")
    parser.add_argument("--json", action="store_true", help="输出原始 JSON")
    parser.add_argument("--output", "-o", help="输出文件路径")

    args = parser.parse_args()

    # 构建资源类型配置
    resource_types = None
    if args.type:
        resource_types = [{"type": t, "top_k": args.top_k} for t in args.type]

    response = search(
        query=args.query,
        api_key=args.api_key,
        edition=args.edition,
        resource_types=resource_types,
        site_filter=args.site,
        block_websites=args.block,
        safe_search=args.safe,
        recency_filter=args.recency,
        top_k=args.top_k,
    )

    # 格式化输出
    output = json.dumps(response, ensure_ascii=False, indent=2) if args.json else format_results(response)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"结果已保存到: {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
