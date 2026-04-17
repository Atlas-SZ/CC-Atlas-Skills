# CodeFlow - 代码架构可视化分析

> 浏览器端代码架构智能分析工具。零安装、完全离线、单 HTML 文件。

## 功能

- **交互式依赖图** — D3.js 力导向图，点击节点高亮依赖链
- **爆炸半径分析** — 选择文件，精确显示修改影响范围
- **安全扫描** — 检测硬编码密钥、SQL 注入、eval 使用、调试语句
- **模式检测** — 识别 Singleton/Factory/Observer 等设计模式和反模式
- **健康评分** — A-F 评级（死代码/循环依赖/耦合度/安全问题）
- **代码所有权** — 基于 Git 历史显示每个文件的主要贡献者
- **活动热力图** — 按提交频率着色，识别活跃模块
- **导出报告** — 导出 JSON 供 Claude Code 消费，节省探索阶段 80-90% token

## 使用

### 方式 1: Claude Code Skill

在 Claude Code 中直接使用：

```
/codeflow
```

或自然语言触发："帮我分析这个项目的架构"

### 方式 2: 直接打开

```bash
# 本地打开（完全离线）
open codeflow/assets/index.html

# 拖入项目文件夹即可分析
```

### 方式 3: 在线使用

访问 https://codeflow-five.vercel.app/ ，粘贴 GitHub 链接。

## 支持的语言

JavaScript, TypeScript, Python, Java, Go, Ruby, PHP, Vue, Svelte, Rust, C/C++, C#, Swift, Kotlin 等 30+ 种语言。

## 隐私

- 100% 浏览器端运行
- 本地文件夹分析完全离线
- GitHub Token 仅存于浏览器内存
- 代码不上传到任何服务器

## 技术原理

- **Tree-sitter WASM** — VS Code 同款语法解析引擎，真正理解代码结构
- **D3.js** — 力导向图可视化
- **React 18** — 界面渲染
- **Batching & Yielding** — 防止 UI 冻结的异步处理

## 致谢

基于 [CodeFlow](https://github.com/braedonsaunders/codeflow) by Braedon Saunders。

## License

MIT License
