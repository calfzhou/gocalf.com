from math import trunc


class Solution:
    def calculate(self, s: str) -> int:
        vals = []
        num = 0
        prev_op = '+' # Default to `+`, means the 1st number is positive.
        n = len(s)
        for i in range(n + 1):
            c = s[i] if i < n else '='
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == ' ':
                continue
            else:
                if prev_op == '+':
                    vals.append(num)
                elif prev_op == '-':
                    vals.append(-num)
                elif prev_op == '*':
                    vals.append(vals.pop() * num)
                else:
                    vals.append(trunc(vals.pop() / num))

                prev_op = c
                num = 0

        return sum(vals)
