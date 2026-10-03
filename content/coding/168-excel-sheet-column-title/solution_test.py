import pytest

from solution import Solution


@pytest.mark.parametrize('columnNumber, expected', [
    (1, "A"),
    (28, "AB"),
    (701, "ZY"),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, columnNumber, expected):
    assert sol.convertToTitle(columnNumber) == expected
