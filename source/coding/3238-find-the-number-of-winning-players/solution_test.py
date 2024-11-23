import pytest

from solution import Solution


@pytest.mark.parametrize('n, pick, expected', [
    (4, [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]], 2),
    (5, [[1,1],[1,2],[1,3],[1,4]], 0),
    (5, [[1,1],[2,4],[2,4],[2,4]], 1),
])
class Test:
    def test_solution(self, n, pick, expected):
        sol = Solution()
        assert sol.winningPlayerCount(n, pick) == expected
