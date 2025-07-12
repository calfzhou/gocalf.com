class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for c in columnTitle:
            d = ord(c) - 64
            num = num * 26 + d

        return num
