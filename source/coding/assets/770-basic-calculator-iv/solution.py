from itertools import chain, product
from typing import Iterable

Token = str|int


class Term:
    def __init__(self, k: int, vars: Iterable[str]) -> None:
        self.k = k
        self.vars = tuple(sorted(vars))

    @property
    def degree(self) -> int:
        return len(self.vars)

    def __str__(self) -> str:
        return '*'.join((str(self.k), *self.vars))


def polynomial(token: Token) -> list[Term]:
    if token == 0:
        return []
    elif isinstance(token, int):
        return [Term(token, [])]
    else:
        return [Term(1, [token])]


def merge_terms(terms: Iterable[Term]) -> list[Term]:
    res = []
    for t in sorted(terms, key=lambda t: (-t.degree, t.vars)):
        if res and res[-1].vars == t.vars:
            res[-1].k += t.k
            if res[-1].k == 0: res.pop()
        else:
            res.append(t)

    return res


def p_add(a: Iterable[Term], b: Iterable[Term]) -> list[Term]:
    return merge_terms(chain(a, b))


def p_sub(a: Iterable[Term], b: Iterable[Term]) -> list[Term]:
    return merge_terms(chain(a, (Term(-y.k, y.vars) for y in b)))


def p_mul(a: Iterable[Term], b: Iterable[Term]) -> list[Term]:
    return merge_terms(Term(x.k * y.k, chain(x.vars, y.vars)) for x, y in product(a, b))


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
        return [str(term) for term in res]

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
