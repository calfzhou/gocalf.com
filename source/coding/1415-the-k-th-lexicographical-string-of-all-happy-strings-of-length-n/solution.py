class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        base = 1 << (n - 1) # 2 ** (n - 1)
        b, k = divmod(k - 1, base)
        if b >= 3:
            return ""

        chars = 'abc'
        candidates = ((1, 2), (0, 2), (0, 1))
        d = b
        parts = [chars[d]]
        while base > 1:
            base >>= 1
            b, k = divmod(k, base)
            d = candidates[d][b]
            parts.append(chars[d])

        return ''.join(parts)
