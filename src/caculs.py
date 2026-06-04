# filepath: /simple-calculator/simple-calculator/src/caculs.py
import ast
import operator
import math

# Simple, safe expression evaluator for a calculator REPL.

_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

_ALLOWED_UNARY = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

_ALLOWED_NAMES = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "log10": math.log10,
    "pi": math.pi,
    "e": math.e,
    "abs": abs,
    "round": round,
}

def _eval(node):
    if isinstance(node, ast.Expression):
        return _eval(node.body)
    if isinstance(node, ast.Constant):  # Python 3.8+
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Unsupported constant")
    if isinstance(node, ast.Num):  # older AST node
        return node.n
    if isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_OPERATORS:
            raise ValueError(f"Operator {op_type} not allowed")
        left = _eval(node.left)
        right = _eval(node.right)
        return _ALLOWED_OPERATORS[op_type](left, right)
    if isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_UNARY:
            raise ValueError(f"Unary operator {op_type} not allowed")
        operand = _eval(node.operand)
        return _ALLOWED_UNARY[op_type](operand)
    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError("Only simple function calls allowed")
        func_name = node.func.id
        if func_name not in _ALLOWED_NAMES:
            raise ValueError(f"Function '{func_name}' not allowed")
        func = _ALLOWED_NAMES[func_name]
        args = [_eval(arg) for arg in node.args]
        return func(*args)
    if isinstance(node, ast.Name):
        if node.id in _ALLOWED_NAMES:
            return _ALLOWED_NAMES[node.id]
        raise ValueError(f"Name '{node.id}' is not allowed")
    raise ValueError(f"Unsupported expression: {ast.dump(node)}")

def safe_eval_expr(expr: str):
    parsed = ast.parse(expr, mode="eval")
    return _eval(parsed)

def repl():
    print("Simple calculator. Type 'exit' or 'quit' to leave.")
    try:
        while True:
            try:
                s = input("calc> ").strip()
            except EOFError:
                print()
                break
            if not s:
                continue
            if s.lower() in ("exit", "quit"):
                break
            try:
                result = safe_eval_expr(s)
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                print(result)
            except Exception as e:
                print("Error:", e)
    except KeyboardInterrupt:
        print("\nExiting.")

if __name__ == "__main__":
    repl()
