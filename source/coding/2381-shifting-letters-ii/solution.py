from string import ascii_lowercase


class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        shifts2 = [0] * (n + 1)
        for start, end, d in shifts:
            if d == 0: d = -1
            shifts2[start] += d
            shifts2[end+1] -= d

        chars = ascii_lowercase
        mapping = {c: i for i, c in enumerate(chars)}

        parts = list(s)
        k = 0
        for i, c in enumerate(parts):
            k += shifts2[i]
            parts[i] = chars[(mapping[c] + k) % 26]

        return ''.join(parts)
