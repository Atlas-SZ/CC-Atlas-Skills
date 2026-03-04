#!/usr/bin/env python3
"""
百度智能 PPT 生成脚本
集成百度智能云千帆 AI PPT API
"""
from __future__ import annotations

import argparse
import json
import os
import urllib.request
import urllib.error
from typing import Any


class BaiduPPTClient:
    """百度 PPT API 客户端"""

    BASE_URL = "https://qianfan.baidubce.com/v2/tools/ai_ppt"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

    def _request(self, endpoint: str, data: dict) -> dict:
        """发送请求"""
        url = f"{self.BASE_URL}/{endpoint}"
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=body,
            headers=self.headers,
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8") if e.fp else ""
            return {"error": True, "status_code": e.code, "message": error_body}
        except urllib.error.URLError as e:
            return {"error": True, "message": f"网络错误: {e.reason}"}

    def _request_sse(self, endpoint: str, data: dict) -> dict:
        """发送 SSE 请求并收集所有响应"""
        url = f"{self.BASE_URL}/{endpoint}"
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=body,
            headers=self.headers,
            method="POST",
        )

        result: dict[str, Any] = {}
        outline_parts: list[str] = []
        try:
            with urllib.request.urlopen(req, timeout=300) as response:
                content = response.read().decode("utf-8")
                # 解析 SSE 格式
                for line in content.split("\n"):
                    if line.startswith("data:"):
                        json_str = line[5:].strip()
                        if json_str:
                            try:
                                event_data = json.loads(json_str)
                                # 累积 outline 内容
                                if event_data.get("outline"):
                                    outline_parts.append(event_data["outline"])
                                # 更新其他字段
                                for key, value in event_data.items():
                                    if key != "outline" and value:
                                        result[key] = value
                                # 检查是否结束
                                if event_data.get("is_end"):
                                    break
                            except json.JSONDecodeError:
                                continue
            # 合并所有 outline 部分
            result["outline"] = "".join(outline_parts)
            return result
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8") if e.fp else ""
            return {"error": True, "status_code": e.code, "message": error_body}
        except urllib.error.URLError as e:
            return {"error": True, "message": f"网络错误: {e.reason}"}

    def get_themes(self) -> dict:
        """获取可用的 PPT 模板"""
        return self._request("get_ppt_theme", {})

    def generate_outline(
        self,
        query: str,
        page_range: str | None = None,
        layout: int | None = None,
        language_option: str | None = None,
        gen_mode: int | None = None,
        resource_url: str | None = None,
    ) -> dict:
        """生成 PPT 大纲"""
        data: dict[str, Any] = {"query": query}
        if page_range:
            data["page_range"] = page_range
        if layout is not None:
            data["layout"] = layout
        if language_option:
            data["language_option"] = language_option
        if gen_mode is not None:
            data["gen_mode"] = gen_mode
        if resource_url:
            data["resource_url"] = resource_url
        return self._request_sse("generate_outline", data)

    def generate_ppt(
        self,
        query: str,
        title: str,
        outline: str,
        chat_id: int,
        query_id: int,
        style_id: int = 0,
        tpl_id: int = 0,
        resource_url: str | None = None,
        custom_tpl_url: str | None = None,
        gen_mode: int = 1,
        ai_info: bool = False,
    ) -> dict:
        """基于大纲生成 PPT"""
        data = {
            "query": query,
            "title": title,
            "outline": outline,
            "chat_id": chat_id,
            "query_id": query_id,
            "style_id": style_id,
            "tpl_id": tpl_id,
            "gen_mode": gen_mode,
            "ai_info": ai_info,
        }
        if resource_url:
            data["resource_url"] = resource_url
        if custom_tpl_url:
            data["custom_tpl_url"] = custom_tpl_url
        return self._request_sse("generate_ppt_by_outline", data)

    def download_pptx(self, url: str, output_path: str) -> bool:
        """下载 PPT 文件"""
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=60) as response:
                with open(output_path, "wb") as f:
                    f.write(response.read())
            return True
        except Exception as e:
            print(f"下载失败: {e}")
            return False


def format_themes(themes: list) -> str:
    """格式化模板列表"""
    lines = ["## 可用 PPT 模板\n"]
    for theme in themes:
        style_id = theme.get("style_id", "?")
        tpl_id = theme.get("tpl_id", "?")
        names = ", ".join(theme.get("style_name_list", []))
        colors = ", ".join(theme.get("color_list", []))
        lines.append(f"### 样式 {style_id}, 模板 {tpl_id}")
        lines.append(f"- 名称: {names}")
        lines.append(f"- 颜色: {colors}")
        lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="百度智能 PPT 生成")
    parser.add_argument("query", nargs="?", help="主题描述")
    parser.add_argument("--api-key", help="API Key")
    parser.add_argument("--list-themes", action="store_true", help="列出可用模板")

    # outline 命令参数
    parser.add_argument("--pages", default="1-10", help="页数范围")
    parser.add_argument("--layout", type=int, choices=[1, 2], default=2, help="布局模式")
    parser.add_argument("--resource", help="资源文件URL")
    parser.add_argument("--gen-mode", type=int, choices=[1, 2], default=1, help="生成模式")

    # generate 命令参数
    parser.add_argument("--title", help="PPT标题")
    parser.add_argument("--style-id", type=int, default=0, help="样式ID")
    parser.add_argument("--tpl-id", type=int, help="模板ID")
    parser.add_argument("--chat-id", type=int, help="会话ID")
    parser.add_argument("--query-id", type=int, help="查询ID")
    parser.add_argument("--outline-file", help="大纲文件路径")
    parser.add_argument("--output", "-o", help="输出文件路径")
    # 下载
    parser.add_argument("--download", help="下载PPT的URL")

    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("BAIDU_API_KEY")
    if not api_key:
        print("错误: API Key 未设置，请通过参数或环境变量 BAIDU_API_KEY 提供")
        return

    client = BaiduPPTClient(api_key)

    # 列出模板
    if args.list_themes:
        result = client.get_themes()
        if result.get("error"):
            print(f"获取模板失败: {result.get('message')}")
        else:
            themes = result.get("data", {}).get("ppt_themes", [])
            print(format_themes(themes))
        return

    # 下载
    if args.download:
        output = args.output or "output.pptx"
        if client.download_pptx(args.download, output):
            print(f"✓ PPT 已下载到: {output}")
        return

    if not args.query:
        print("错误: 请提供主题描述 (query)")
        return

    # 生成大纲
    if not args.title:
        print("## 生成大纲...")
        result = client.generate_outline(
            query=args.query,
            page_range=args.pages if args.pages != "1-10" else None,
            layout=args.layout if args.layout != 2 else None,
            gen_mode=args.gen_mode if args.gen_mode != 1 else None,
            resource_url=args.resource,
        )
        if result.get("error"):
            print(f"生成大纲失败: {result.get('message')}")
        else:
            print(f"\n会话ID: {result.get('chat_id')}")
            print(f"查询ID: {result.get('query_id')}")
            print(f"\n生成的大纲:\n{result.get('outline', '(无)')}")
        return

    # 生成 PPT
    if not args.tpl_id:
        print("错误: 请提供模板ID (--tpl-id)")
        return

    # 读取大纲
    outline = ""
    if args.outline_file:
        try:
            with open(args.outline_file, "r", encoding="utf-8") as f:
                outline = f.read()
        except FileNotFoundError:
            print(f"错误: 找不到大纲文件: {args.outline_file}")
            return

    if not args.chat_id or not args.query_id:
        print("错误: 生成PPT需要 --chat-id 和 --query-id (从大纲生成获取)")
        return

    print(f"## 生成 PPT: {args.title}...")
    result = client.generate_ppt(
        query=args.query,
        title=args.title,
        outline=outline,
        chat_id=args.chat_id,
        query_id=args.query_id,
        style_id=args.style_id,
        tpl_id=args.tpl_id,
        gen_mode=args.gen_mode,
        resource_url=args.resource,
    )

    if result.get("error"):
        print(f"生成PPT失败: {result.get('message')}")
        return

    pptx_url = result.get("data", {}).get("pptx_url", "")
    if pptx_url:
        print(f"\n✓ PPT 生成成功!")
        print(f"下载链接: {pptx_url}")
        if args.output:
            if client.download_pptx(pptx_url, args.output):
                print(f"✓ 已保存到: {args.output}")
    else:
        print(f"状态: {result.get('status')}")


if __name__ == "__main__":
    main()
