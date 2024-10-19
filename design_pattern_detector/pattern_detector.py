import ast

def detect_singleton_pattern(tree):
    # Singleton pattern detection logic
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            methods = [n for n in node.body if isinstance(n, ast.FunctionDef)]
            for method in methods:
                if method.name == '__init__':
                    for stmt in method.body:
                        if isinstance(stmt, ast.Assign):
                            if isinstance(stmt.value, ast.Call) and isinstance(stmt.value.func, ast.Name):
                                if stmt.value.func.id == node.name:  # Recursive call to constructor
                                    return {
                                        'name': 'Singleton',
                                        'description': 'Singleton pattern detected in class ' + node.name
                                    }
    return None

def detect_factory_pattern(tree):
    # Factory pattern detection logic
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name.startswith('create_'):
            return {
                'name': 'Factory',
                'description': 'Factory pattern detected in method ' + node.name
            }
    return None

def detect_observer_pattern(tree):
    # Observer pattern detection logic
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            if 'subscribe' in [n.name for n in node.body if isinstance(n, ast.FunctionDef)]:
                return {
                    'name': 'Observer',
                    'description': 'Observer pattern detected in class ' + node.name
                }
    return None

def detect_design_patterns(code):
    tree = ast.parse(code)
    patterns = []

    # Detect Singleton
    singleton = detect_singleton_pattern(tree)
    if singleton:
        patterns.append(singleton)

    # Detect Factory
    factory = detect_factory_pattern(tree)
    if factory:
        patterns.append(factory)

    # Detect Observer
    observer = detect_observer_pattern(tree)
    if observer:
        patterns.append(observer)

    return patterns
