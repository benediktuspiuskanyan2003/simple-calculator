# calc_cli_safe.py
# Kalkulator CLI yang aman: mengevaluasi ekspresi matematika saja menggunakan AST

import ast
import operator
import math

# Operator yang diizinkan
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.FloorDiv: operator.floordiv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

# Fungsi-fungsi matematika yang diizinkan
MATH_FUNCS = {
    'sqrt': math.sqrt,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'log': math.log,      # natural log, log(x, base) juga bisa dipanggil via two-arg handling
    'log10': math.log10,
    'exp': math.exp,
    'abs': abs,
    'round': round,
    'floor': math.floor,
    'ceil': math.ceil,
    'factorial': math.factorial,
}

# Konstant: pi, e
CONSTS = {
    'pi': math.pi,
    'e': math.e,
}

class SafeEval(ast.NodeVisitor):
    def visit(self, node):
        if isinstance(node, ast.Expression):
            return self.visit(node.body)
        return super().visit(node)

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op_type = type(node.op)
        if op_type in OPERATORS:
            return OPERATORS[op_type](left, right)
        raise ValueError(f"Operator tidak diizinkan: {op_type}")

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        op_type = type(node.op)
        if op_type in OPERATORS:
            return OPERATORS[op_type](operand)
        raise ValueError(f"Unary operator tidak diizinkan: {op_type}")

    def visit_Num(self, node):  # Python <3.8
        return node.n

    def visit_Constant(self, node):  # Python 3.8+
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Konstanta non-numerik tidak diizinkan")

    def visit_Call(self, node):
        if not isinstance(node.func, ast.Name):
            raise ValueError("Hanya pemanggilan fungsi bernama yang diizinkan")
        fname = node.func.id
        if fname not in MATH_FUNCS:
            raise ValueError(f"Fungsi tidak diizinkan: {fname}")
        args = [self.visit(a) for a in node.args]
        return MATH_FUNCS[fname](*args)

    def visit_Name(self, node):
        if node.id in CONSTS:
            return CONSTS[node.id]
        raise ValueError(f"Nama variabel/fungsi tidak diizinkan: {node.id}")

    def generic_visit(self, node):
        raise ValueError(f"Ekspresi tidak diizinkan: {type(node).__name__}")

def safe_eval(expr: str):
    expr = expr.strip()
    if not expr:
        raise ValueError("Ekspresi kosong")
    tree = ast.parse(expr, mode='eval')
    evaluator = SafeEval()
    return evaluator.visit(tree)

def main():
    print("Kalkulator CLI (ketik 'exit' atau 'quit' untuk keluar)")
    print("Contoh: 2 + 3*4, (2+3)**2, sqrt(16), sin(pi/2)")
    while True:
        try:
            s = input(">> ")
        except (EOFError, KeyboardInterrupt):
            print("\nKeluar.")
            break
        if not s:
            continue
        if s.lower() in ('exit', 'quit'):
            print("Keluar.")
            break
        try:
            result = safe_eval(s)
            print("= ", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
