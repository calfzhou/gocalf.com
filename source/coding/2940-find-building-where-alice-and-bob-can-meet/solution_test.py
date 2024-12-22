import pytest

from solution import Solution


@pytest.mark.parametrize('heights, queries, expected', [
    ([6,4,8,5,2,7], [[0,1],[0,3],[2,4],[3,4],[2,2]], [2,5,-1,5,2]),
    ([5,3,8,2,6,1,4,6], [[0,7],[3,5],[5,2],[3,0],[1,6]], [7,6,-1,4,6]),

    (
        [1,2,1,2,1,2],
        [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5]],
        [0,1,3,3,5,5,1,1,-1,-1,-1,-1,3,-1,2,3,5,5,3,-1,3,3,-1,-1,5,-1,5,-1,4,5,5,-1,5,-1,5,5]
    ),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, heights, queries, expected):
    assert sol.leftmostBuildingQueries(heights.copy(), queries.copy()) == expected
