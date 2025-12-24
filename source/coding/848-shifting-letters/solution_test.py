import pytest

from solution import Solution


@pytest.mark.parametrize('s, shifts, expected', [
    ("abc", [3,5,9], "rpl"),
    ("aaa", [1,2,3], "gfd"),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, s, shifts, expected):
    assert sol.shiftingLetters(s, shifts.copy()) == expected
