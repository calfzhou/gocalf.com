import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ("aaaa", 2),
    ("abcdef", -1),
    ("abcaba", 1),

    ("biaei", -1),
    ("eccdnmcnkl", 1),
])
class Test:
    def test_solution(self, s, expected):
        sol = Solution()
        assert sol.maximumLength(s) == expected
