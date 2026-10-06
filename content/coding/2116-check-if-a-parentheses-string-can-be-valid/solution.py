class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n & 1 or locked[0] == '1' and s[0] == ')' or locked[-1] == '1' and s[-1] == '(':
            return False

        open = 0
        empty = 0
        for i in range(n):
            if locked[i] == '0':
                empty += 1
            elif s[i] == '(':
                open += 1
            elif open:
                open -= 1
            elif empty:
                empty -= 1
            else:
                return False

        close = 0
        empty = 0
        for i in range(n - 1, -1, -1):
            if locked[i] == '0':
                empty += 1
            elif s[i] == ')':
                close += 1
            elif close:
                close -= 1
            elif empty:
                empty -= 1
            else:
                return False

        return True
