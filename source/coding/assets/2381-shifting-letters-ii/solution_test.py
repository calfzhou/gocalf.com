import pytest

from solution import Solution


@pytest.mark.parametrize('s, shifts, expected', [
    ("abc", [[0,1,0],[1,2,1],[0,2,1]], "ace"),
    ("dztz", [[0,0,0],[1,1,1]], "catz"),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, s, shifts, expected):
    assert sol.shiftingLetters(s, shifts) == expected
