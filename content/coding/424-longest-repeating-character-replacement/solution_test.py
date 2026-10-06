import pytest

from solution import Solution


@pytest.mark.parametrize('s, k, expected', [
    ('ABAB', 2, 4),
    ('AABABBA', 1, 4),
])
class Test:
    def test_solution(self, s, k, expected):
        sol = Solution()
        assert sol.characterReplacement(s, k) == expected
