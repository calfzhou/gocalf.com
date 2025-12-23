import pytest

from solution import Solution


@pytest.mark.parametrize('columnTitle, expected', [
    ("A", 1),
    ("AB", 28),
    ("ZY", 701),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, columnTitle, expected):
    assert sol.titleToNumber(columnTitle) == expected
