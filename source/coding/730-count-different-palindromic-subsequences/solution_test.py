import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ("bccb", 6),
    ("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba", 104860361),

    ("a", 1),
    ("ab", 2),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, s, expected):
    assert sol.countPalindromicSubsequences(s) == expected
