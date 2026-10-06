import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ("abc", "abc"),
    ("cb34", ""),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, s, expected):
    assert sol.clearDigits(s) == expected
