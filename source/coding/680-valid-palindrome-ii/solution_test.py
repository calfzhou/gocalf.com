import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ("aba", True),
    ("abca", True),
    ("abc", False),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, s, expected):
    assert sol.validPalindrome(s) == expected
