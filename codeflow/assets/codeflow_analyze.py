"""Local codebase analyzer - produces CodeFlow-compatible JSON report.

Usage: python3 codeflow_analyze.py /path/to/project > report.json
"""
import ast
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

IGNORE_DIRS = {
    '__pycache__', '.git', '.venv', 'venv', 'node_modules',
    '.egg-info', '.tox', '.mypy_cache', '.pytest_cache',
    'dist', 'build', '.idea', '.vscode', 'static', 'migrations',
}

CODE_EXTENSIONS = {
    '.py', '.js', '.jsx', '.ts', '.tsx', '.java', '.go', '.rb',
    '.php', '.vue', '.svelte', '.rs', '.c', '.h', '.cpp', '.hpp',
    '.cs', '.swift', '.kt', '.kts',
}

HARD_LIMIT = 2000


def should_ignore(name: str) -> bool:
    return name in IGNORE_DIRS or name.startswith('.') or name.endswith('.egg-info')


def is_code(path: str) -> bool:
    return Path(path).suffix in CODE_EXTENSIONS


def detect_layer(path: str) -> str:
    parts = path.lower().split('/')
    if any(p in ('views', 'templates', 'static', 'js') for p in parts):
        return 'UI'
    if any(p in ('models', 'orm') for p in parts):
        return 'Data'
    if any(p in ('controllers', 'routes', 'api') for p in parts):
        return 'API'
    if any(p in ('tests', 'test', 'spec') for p in parts):
        return 'Tests'
    if any(p in ('utils', 'helpers', 'lib', 'common') for p in parts):
        return 'Utils'
    if any(p in ('services', 'core', 'engine') for p in parts):
        return 'Services'
    return 'Other'


def extract_python_functions(content: str, filepath: str) -> list[dict]:
    """Extract functions and classes from Python using AST."""
    results = []
    try:
        tree = ast.parse(content, filename=filepath)
    except SyntaxError:
        return results

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            results.append({
                'name': node.name,
                'type': 'function',
                'line': node.lineno,
                'endLine': getattr(node, 'end_lineno', node.lineno),
                'decorators': [d.attr if isinstance(d, ast.Attribute) else
                              (d.id if isinstance(d, ast.Name) else str(d))
                              for d in node.decorator_list],
            })
        elif isinstance(node, ast.ClassDef):
            results.append({
                'name': node.name,
                'type': 'class',
                'line': node.lineno,
                'endLine': getattr(node, 'end_lineno', node.lineno),
                'bases': [b.id if isinstance(b, ast.Name) else
                         (b.attr if isinstance(b, ast.Attribute) else str(b))
                         for b in node.bases],
            })
    return results


def extract_python_imports(content: str, filepath: str) -> list[str]:
    """Extract import paths for dependency analysis."""
    imports = []
    try:
        tree = ast.parse(content, filename=filepath)
    except SyntaxError:
        return imports

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)
    return imports


def scan_security(content: str, filepath: str) -> list[dict]:
    """Basic security issue detection."""
    issues = []
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        # Hardcoded secrets
        if any(kw in stripped.lower() for kw in ['password = "', 'secret = "', 'api_key = "', 'token = "']):
            if not stripped.startswith('#'):
                issues.append({
                    'file': filepath, 'line': i, 'type': 'hardcoded_secret',
                    'severity': 'high', 'description': 'Possible hardcoded secret',
                })
        # SQL injection risk
        if 'execute(' in stripped and ('+' in stripped or '%' in stripped or '.format(' in stripped):
            if 'cursor' in stripped.lower() or 'execute' in stripped:
                issues.append({
                    'file': filepath, 'line': i, 'type': 'sql_injection',
                    'severity': 'high', 'description': 'Potential SQL injection - string concatenation in query',
                })
        # eval usage
        if 'eval(' in stripped and not stripped.startswith('#'):
            issues.append({
                'file': filepath, 'line': i, 'type': 'eval_usage',
                'severity': 'medium', 'description': 'eval() usage detected',
            })
    return issues


def analyze_project(root: str) -> dict:
    root_path = Path(root).resolve()
    project_name = root_path.name

    # Collect files
    files = []
    for dirpath, dirnames, filenames in os.walk(root_path):
        dirnames[:] = [d for d in dirnames if not should_ignore(d)]
        for f in filenames:
            full = Path(dirpath) / f
            rel = str(full.relative_to(root_path))
            if is_code(f):
                files.append((rel, full))
            if len(files) >= HARD_LIMIT:
                break
        if len(files) >= HARD_LIMIT:
            break

    # Language breakdown
    lang_count = defaultdict(int)
    for rel, _ in files:
        ext = Path(rel).suffix
        lang_map = {'.py': 'Python', '.js': 'JavaScript', '.ts': 'TypeScript',
                    '.java': 'Java', '.go': 'Go', '.rb': 'Ruby', '.php': 'PHP',
                    '.vue': 'Vue', '.rs': 'Rust', '.c': 'C', '.cpp': 'C++',
                    '.cs': 'C#', '.swift': 'Swift', '.kt': 'Kotlin'}
        lang_count[lang_map.get(ext, 'Other')] += 1

    # Analyze files
    analyzed = []
    all_imports = {}
    all_security = []
    total_functions = 0
    total_classes = 0

    for idx, (rel, full) in enumerate(files):
        try:
            content = full.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            continue

        lines = content.split('\n')
        layer = detect_layer(rel)
        functions = []

        if rel.endswith('.py'):
            functions = extract_python_functions(content, rel)
            imports = extract_python_imports(content, rel)
            all_imports[rel] = imports
            sec = scan_security(content, rel)
            all_security.extend(sec)

        fn_count = sum(1 for f in functions if f['type'] == 'function')
        cls_count = sum(1 for f in functions if f['type'] == 'class')
        total_functions += fn_count
        total_classes += cls_count

        analyzed.append({
            'path': rel,
            'language': Path(rel).suffix.lstrip('.'),
            'functions': [f['name'] for f in functions],
            'functionDetails': functions,
            'imports': all_imports.get(rel, []),
            'lines': len(lines),
            'layer': layer,
            'isCode': True,
        })

    # Dependency analysis
    dependencies = defaultdict(list)
    for rel, imports in all_imports.items():
        module_root = rel.split('/')[0].replace('_', '')
        for imp in imports:
            imp_root = imp.split('.')[0].replace('_', '')
            if imp_root != module_root and imp_root:
                for other_rel in all_imports:
                    other_root = other_rel.split('/')[0].replace('_', '')
                    if other_root == imp_root and other_rel != rel:
                        if other_rel not in dependencies[rel]:
                            dependencies[rel].append(other_rel)

    # Module coupling
    module_deps = defaultdict(set)
    for rel, deps in dependencies.items():
        mod = rel.split('/')[0]
        for dep in deps:
            dep_mod = dep.split('/')[0]
            if dep_mod != mod:
                module_deps[mod].add(dep_mod)

    # Circular dependencies
    circular = []
    for mod, deps in module_deps.items():
        for dep in deps:
            if mod in module_deps.get(dep, set()):
                pair = tuple(sorted([mod, dep]))
                if pair not in circular:
                    circular.append(pair)

    # Health score
    code_files = [f for f in analyzed if f['isCode']]
    avg_lines = sum(f['lines'] for f in code_files) / max(len(code_files), 1) if code_files else 0
    coupling_score = min(len(module_deps) / max(len(set(f['path'].split('/')[0] for f in analyzed)), 1), 1.0)

    security_deduction = min(len(all_security) * 5, 30)
    circular_deduction = min(len(circular) * 5, 20)
    coupling_deduction = int(coupling_score * 20)
    score = max(100 - security_deduction - circular_deduction - coupling_deduction, 0)

    if score >= 90: grade = 'A'
    elif score >= 80: grade = 'B'
    elif score >= 70: grade = 'C'
    elif score >= 60: grade = 'D'
    else: grade = 'F'

    return {
        'metadata': {
            'repository': project_name,
            'analyzedAt': __import__('datetime').datetime.now().isoformat(),
            'totalFiles': len(analyzed),
            'totalFunctions': total_functions,
            'totalClasses': total_classes,
            'languages': dict(lang_count),
        },
        'healthScore': {
            'grade': grade,
            'score': score,
            'deadCodePercent': 0,
            'circularDependencies': len(circular),
            'couplingIndex': round(coupling_score, 2),
            'securityIssues': len(all_security),
        },
        'files': analyzed,
        'dependencies': dict(dependencies),
        'moduleDependencies': {k: list(v) for k, v in module_deps.items()},
        'circularDependencies': circular,
        'securityIssues': all_security,
        'modules': sorted(list(set(f['path'].split('/')[0] for f in analyzed))),
    }


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 codeflow_analyze.py /path/to/project", file=sys.stderr)
        sys.exit(1)
    root = sys.argv[1]
    if not os.path.isdir(root):
        print(f"Error: {root} is not a directory", file=sys.stderr)
        sys.exit(1)
    result = analyze_project(root)
    print(json.dumps(result, indent=2, ensure_ascii=False))
