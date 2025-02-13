import pytest

from solution import Solution


@pytest.mark.parametrize('lowLimit, highLimit, expected', [
    (1, 10, 2),
    (5, 15, 2),
    (19, 28, 2),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, lowLimit, highLimit, expected):
    assert sol.countBalls(lowLimit, highLimit) == expected
