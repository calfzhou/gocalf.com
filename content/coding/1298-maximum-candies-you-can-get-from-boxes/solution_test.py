import pytest

from solution import Solution


@pytest.mark.parametrize('status, candies, keys, containedBoxes, initialBoxes, expected', [
    ([1,0,1,0], [7,5,4,100], [[],[],[1],[]], [[1,2],[3],[],[]], [0], 16),
    ([1,0,0,0,0,0], [1,1,1,1,1,1], [[1,2,3,4,5],[],[],[],[],[]], [[1,2,3,4,5],[],[],[],[],[]], [0], 6),

    ([1,1,1], [100,1,100], [[],[0,2],[]], [[],[],[]], [1], 1),
    ([1,0,0,0,0,0], [1,1,1,1,1,1], [[1,2,3,4,5],[0,2,3,4],[0,1,3,5],[0,1,2],[],[]], [[1,2,3,4,5],[],[],[],[],[]], [0], 6),

    ([1,0,0], [1,1,1], [[],[2],[1]], [[],[],[]], [0,1], 1),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, status, candies, keys, containedBoxes, initialBoxes, expected):
    assert sol.maxCandies(status.copy(), candies, keys, containedBoxes, initialBoxes.copy()) == expected
