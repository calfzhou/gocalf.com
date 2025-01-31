import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    (["h","e","l","l","o"], ["o","l","l","e","h"]),
    (["H","a","n","n","a","h"], ["h","a","n","n","a","H"]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, s, expected):
    s = s.copy()
    sol.reverseString(s)
    assert s == expected
