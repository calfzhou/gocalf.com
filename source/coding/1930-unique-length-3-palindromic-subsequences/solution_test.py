import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ("aabca", 3),
    ("adc", 0),
    ("bbcbaba", 4),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, s, expected):
    assert sol.countPalindromicSubsequence(s) == expected
