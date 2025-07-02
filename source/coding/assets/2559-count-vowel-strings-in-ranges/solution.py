from itertools import accumulate


class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowels = set('aeiou')
        dp = [0] + list(accumulate(1 if w[0] in vowels and w[-1] in vowels else 0 for w in words))
        return [dp[r+1] - dp[l] for l, r in queries]
