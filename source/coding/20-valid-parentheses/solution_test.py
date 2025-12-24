import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([])", True),

    ("((", False),
    ("))", False),
    ("((())", False),
])
class Test:
    def test_solution(self, s, expected):
        sol = Solution()
        assert sol.isValid(s) == expected
