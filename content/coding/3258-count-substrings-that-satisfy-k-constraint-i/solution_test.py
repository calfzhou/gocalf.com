import pytest

from solution import Solution


@pytest.mark.parametrize('s, k, expected', [
    ('10101', 1, 12),
    ('1010101', 2, 25),
    ('11111', 1, 15),

    ('000011', 1, 18),
])
class Test:
    def test_solution(self, s, k, expected):
        sol = Solution()
        assert sol.countKConstraintSubstrings(s, k) == expected
