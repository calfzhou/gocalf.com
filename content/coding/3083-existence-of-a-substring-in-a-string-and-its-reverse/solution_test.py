import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ("leetcode", True),
    ("abcba", True),
    ("abcd", False),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, s, expected):
    assert sol.isSubstringPresent(s) == expected
