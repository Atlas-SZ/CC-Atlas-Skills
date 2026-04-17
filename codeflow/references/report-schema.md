# CodeFlow 导出报告 JSON 结构

## 顶层结构

```json
{
  "metadata": {
    "repository": "owner/repo",
    "analyzedAt": "ISO8601 timestamp",
    "totalFiles": 150,
    "languages": { "Python": 120, "JavaScript": 30 }
  },
  "healthScore": {
    "grade": "B",
    "score": 78,
    "deadCodePercent": 5.2,
    "circularDependencies": 3,
    "couplingIndex": 0.42,
    "securityIssues": 2
  },
  "files": [
    {
      "path": "src/auth/login.py",
      "language": "Python",
      "functions": ["login", "validate_token", "refresh_session"],
      "dependencies": ["src/models/user.py", "src/utils/crypto.py"],
      "dependents": ["src/api/routes.py", "src/middleware/auth.py"],
      "changeFrequency": "high",
      "primaryContributor": "alice",
      "linesOfCode": 245
    }
  ],
  "securityIssues": [
    {
      "file": "src/config.py",
      "line": 15,
      "type": "hardcoded_secret",
      "severity": "critical",
      "description": "Hardcoded API key detected"
    }
  ],
  "patterns": {
    "detected": ["Factory", "Observer", "Singleton"],
    "antiPatterns": ["God Object: src/models/user.py", "High Coupling: src/api/routes.py"]
  },
  "duplicates": [],
  "suggestions": []
}
```

## 关键字段说明

### healthScore

| 字段 | 说明 |
|------|------|
| grade | A-F 评级，A 最好 |
| score | 0-100 分数 |
| deadCodePercent | 死代码占比 |
| circularDependencies | 循环依赖数量 |
| couplingIndex | 耦合度指数（0-1，越低越好） |
| securityIssues | 安全问题数量 |

### files[].dependencies

该文件 import/require 的其他文件列表。用于绘制依赖图和计算爆炸半径。

### files[].dependents

依赖该文件的其他文件列表。修改此文件时，这些文件可能受影响。

### securityIssues[].type

可选值: `hardcoded_secret`, `sql_injection`, `eval_usage`, `debug_statement`

### patterns.antiPatterns

常见反模式:
- **God Object**: 过大的类/文件，承担过多职责
- **High Coupling**: 依赖过多其他模块
- **Circular Dependency**: 循环引用

## Claude 消费建议

读取报告后，Claude 应提取：

1. **metadata** — 了解项目规模和技术栈
2. **healthScore** — 快速判断代码质量
3. **files** 中与当前任务相关的条目 — 精确定位修改点
4. **securityIssues** — 如果涉及安全相关修改
5. **patterns.antiPatterns** — 重构时优先关注的目标
