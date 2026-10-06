import copy
import pytest

from solution import Solution


@pytest.mark.parametrize('grid, k, expected', [
    ([[1,2,3],[4,5,6],[7,8,9]], 1, [[9,1,2],[3,4,5],[6,7,8]]),
    ([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4, [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]),
    ([[1,2,3],[4,5,6],[7,8,9]], 9, [[1,2,3],[4,5,6],[7,8,9]]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, grid, k, expected):
    assert sol.shiftGrid(copy.deepcopy(grid), k) == expected
