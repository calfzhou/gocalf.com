import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ('abc', 3),
    ('aaa', 6),
])
class Test:
    def test_solution(self, s, expected):
        sol = Solution()
        assert sol.countSubstrings(s) == expected
