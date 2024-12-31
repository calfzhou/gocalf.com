import pytest

from solution import Solution


@pytest.mark.parametrize('date, expected', [
    ("2080-02-29", "100000100000-10-11101"),
    ("1900-01-01", "11101101100-1-1"),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, date, expected):
    assert sol.convertDateToBinary(date) == expected
