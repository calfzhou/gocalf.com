import pytest

from solution import Solution


@pytest.mark.parametrize('isWater, expected', [
    ([[0,1],[0,0]], [[1,0],[2,1]]),
    ([[0,0,1],[1,0,0],[0,0,0]], [[1,1,0],[0,1,1],[1,2,2]]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, isWater, expected):
    assert sol.highestPeak(isWater) == expected
