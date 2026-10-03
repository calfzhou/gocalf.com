import pytest

from solution import Solution


@pytest.mark.parametrize('n, edges, expected', [
    (3, [[0,1],[1,2]], 0),
    (4, [[0,2],[1,3],[1,2]], -1),
])
class Test:
    def test_solution(self, n, edges, expected):
        sol = Solution()
        assert sol.findChampion(n, edges) == expected
