from itertools import groupby

MOD = 10**9 + 7
MAX = 10**5

dp3 = [0] * MAX
dp4 = [0] * MAX
dp3[-1] = 1
dp4[-1] = 1
for n in range(MAX):
    dp3[n] = (dp3[n-1] + dp3[n-2] + dp3[n-3]) % MOD
    dp4[n] = (dp4[n-1] + dp4[n-2] + dp4[n-3] + dp4[n-4]) % MOD


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        total = 1
        for k, g in groupby(pressedKeys):
            n = sum(1 for _ in g) - 1
            total *= dp4[n] if k == '7' or k == '9' else dp3[n]
            total %= MOD

        return total
