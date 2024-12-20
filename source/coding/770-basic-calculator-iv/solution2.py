from collections import defaultdict
from itertools import product
from typing import Iterable

Token = str|int
Polynomial = dict[tuple[str], int]


def polynomial(token: Token) -> Polynomial:
    if token == 0:
        return defaultdict(int)
    elif isinstance(token, int):
        return defaultdict(int, {tuple(): token})
    else:
        return defaultdict(int, {(token,): 1})


def p_add(a: Polynomial, b: Polynomial) -> Polynomial:
    for vals, k in b.items():
        a[vals] += k

    return a


def p_sub(a: Polynomial, b: Polynomial) -> Polynomial:
    for vals, k in b.items():
        a[vals] -= k

    return a


def p_mul(a: Polynomial, b: Polynomial) -> Polynomial:
    res: Polynomial = defaultdict(int)
    for x, y in product(a, b):
        vars = tuple(sorted(x + y))
        k = a[x] * b[y]
        res[vars] += k

    return res


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: list[str], evalints: list[int]) -> list[str]:
        vars = {k: v for k, v in zip(evalvars, evalints)}
        tokens = self.reverse_polish(self.tokenize(expression), vars)
        ops = { '+': p_add, '-': p_sub, '*': p_mul }
        stack = []
        for token in tokens:
            if token in ops:
                b, a = stack.pop(), stack.pop()
                stack.append(ops[token](a, b))
            else:
                stack.append(polynomial(token))

        res = stack[0]
        terms = sorted(res.items(), key=lambda t: (-len(t[0]), t[0]))
        return ['*'.join((str(k), *vars)) for vars, k in terms if k != 0]

    def tokenize(self, expr: str) -> Iterable[Token]:
        n = len(expr)
        left = 0
        for i in range(n + 1):
            c = expr[i] if i < n else ' '
            if c.isdigit() or c.isalpha():
                continue
            if left < i:
                if expr[left].isdigit():
                    yield int(expr[left:i]) # A number.
                else:
                    yield expr[left:i] # A variable.
            if c != ' ':
                yield c # An operator.
            left = i + 1

    def reverse_polish(self, tokens: Iterable[Token], vars: dict[str, int]) -> Iterable[Token]:
        ops = []
        levels= {'(': -2, ')': -1, '+': 1, '-': 1, '*': 2}
        for token in tokens:
            if isinstance(token, int):
                yield token
            elif token[0].isalpha():
                yield vars.get(token, token)
            elif token == '(':
                ops.append(token)
            else:
                p = levels[token]
                while ops and levels[ops[-1]] >= p:
                    yield ops.pop()
                if token == ')':
                    ops.pop() # `(`
                else:
                    ops.append(token)

        while ops:
            yield ops.pop()
