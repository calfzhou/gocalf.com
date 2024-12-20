class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        signs = [1]
        sign = 1
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                if num > 0:
                    res += num * sign
                    num = 0

                if c == '+': sign = signs[-1]
                elif c == '-': sign = -signs[-1]
                elif c == '(':
                    signs.append(sign)
                elif c == ')':
                    sign = signs.pop()

        if num > 0:
            res += num * sign

        return res
