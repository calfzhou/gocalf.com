import pytest

from solution import Solution


@pytest.mark.parametrize('words, target, expected', [
    (["abc","aaaaa","bcdef"], "aabcdabc", 3),
    (["abababab","ab"], "ababaababa", 2),
    (["abcdef"], "xyz", -1),

    (["caacbbbbbcaccbcbcccbcbbbcbcabbcaaacabbcbbccabcac","baccccb","aacabcca"], "aacaacbabb", 5),
])
class Test:
    def test_solution(self, words, target, expected):
        sol = Solution()
        assert sol.minValidStrings(words, target) == expected
