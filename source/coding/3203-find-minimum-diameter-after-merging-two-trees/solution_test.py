import pytest

from solution import Solution


@pytest.mark.parametrize('edges1, edges2, expected', [
    ([[0,1],[0,2],[0,3]], [[0,1]], 3),
    ([[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], 5),

    ([], [], 1),
    ([[0,1],[2,0],[3,2],[3,6],[8,7],[4,8],[5,4],[3,5],[3,9]], [[0,1],[0,2],[0,3]], 7),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, edges1, edges2, expected):
    assert sol.minimumDiameterAfterMerge(edges1, edges2) == expected
