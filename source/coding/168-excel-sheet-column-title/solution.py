from string import ascii_uppercase


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        parts = []
        while columnNumber > 0:
            columnNumber, remain = divmod(columnNumber - 1, 26)
            parts.append(ascii_uppercase[remain])

        parts.reverse()
        return ''.join(parts)
