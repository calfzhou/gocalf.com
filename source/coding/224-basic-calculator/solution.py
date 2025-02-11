from typing import Iterable

Token = str|int


class Solution:
    def calculate(self, s: str) -> int:
        tokens = self.reverse_polish(self.tokenize(s))
        stack = []
        for token in tokens:
            if isinstance(token, int):
                stack.append(token)
            elif token == '+':
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
            elif token == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == 'n':
                a = stack.pop()
                stack.append(-a)

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
        levels= {'(': -2, ')': -1, '+': 1, '-': 1, 'n': 9}
        prev = ''
        for token in tokens:
            if isinstance(token, int):
                yield token
            elif token == '(':
                ops.append(token)
            else:
                if token == '-' and not(isinstance(prev, int) or prev == ')'): # Unary operation `-`.
                    token = 'n'
                p = levels[token]
                while ops and levels[ops[-1]] >= p:
                    yield ops.pop()
                if token == ')':
                    ops.pop() # `(`
                else:
                    ops.append(token)
            prev = token

        while ops:
            yield ops.pop()
