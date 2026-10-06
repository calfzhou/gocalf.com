import pytest

from solution import Solution


@pytest.mark.parametrize('obstacleGrid, expected', [
    ([[0,0,0],[0,1,0],[0,0,0]], 2),
    ([[0,1],[0,0]], 1),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, obstacleGrid, expected):
    assert sol.uniquePathsWithObstacles(obstacleGrid) == expected
