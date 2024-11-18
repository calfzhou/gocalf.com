import pytest

from solution import Solution


@pytest.mark.parametrize('edges, expected', [
    ([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], 7),
    ([[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]], 6),
    ([[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]], 12),
])
class Test:
    def test_solution(self, edges, expected):
        sol = Solution()
        assert sol.countGoodNodes(edges) == expected