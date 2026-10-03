class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        a = 97
        for i in range(len(s) - 2, -1, -1):
            shifts[i] += shifts[i + 1]

        return ''.join(chr(a + (ord(c) - a + k) % 26) for c, k in zip(s, shifts))
