from typing import Iterable

Token = str|int


class Solution:
    def calculate(self, s: str) -> int:
        tokens = self.reverse_polish(self.tokenize(s))
        stack = []
        for token in tokens:
            if isinstance(token, int):
                stack.append(token)
            else:
                b, a = stack.pop(), stack.pop()
                if token == '+': stack.append(a + b)
                elif token == '-': stack.append(a - b)
                elif token == '*': stack.append(a * b)
                elif token == '/': stack.append(a // b)

        return stack[0]

    def tokenize(self, expr: str) -> Iterable[Token]:
        n = len(expr)
        left = 0
        for i, c in enumerate(expr):
            if c.isdigit():
                continue
            if left < i:
                yield int(expr[left:i]) # A number.
            if c != ' ':
                yield c # An operator.
            left = i + 1

        if left < n:
            yield int(expr[left:]) # The last number.

    def reverse_polish(self, tokens: Iterable[Token]) -> Iterable[Token]:
        ops = []
        levels= {'+': 1, '-': 1, '*': 2, '/': 2}
        for token in tokens:
            if isinstance(token, int):
                yield token
            else:
                p = levels[token]
                while ops and levels[ops[-1]] >= p:
                    yield ops.pop()
                ops.append(token)

        while ops:
            yield ops.pop()
