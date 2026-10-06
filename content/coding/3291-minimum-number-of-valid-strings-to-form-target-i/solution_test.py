import pytest

from solution import Solution
from solution_ac import Solution as SolutionAc


@pytest.mark.parametrize('words, target, expected', [
    (["abc","aaaaa","bcdef"], "aabcdabc", 3),
    (["abababab","ab"], "ababaababa", 2),
    (["abcdef"], "xyz", -1),

    (["caacbbbbbcaccbcbcccbcbbbcbcabbcaaacabbcbbccabcac","baccccb","aacabcca"], "aacaacbabb", 5),
    (["adaeabcabdcaabbeceeadeaebcdddeadcbceeeadddabdc","a"], "beeea", -1),
])
class Test:
    def test_solution(self, words, target, expected):
        sol = Solution()
        assert sol.minValidStrings(words, target) == expected

    def test_solution_ac(self, words, target, expected):
        sol = SolutionAc()
        assert sol.minValidStrings(words, target) == expected
