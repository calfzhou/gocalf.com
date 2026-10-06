import pytest

from solution import Solution


@pytest.mark.parametrize('pairs, expected', [
    ([[1,2],[2,3]], 1),
    ([[1,2],[2,3],[1,3]], 2),
    ([[1,2],[2,3],[2,4],[1,5]], 0),

    ([[3,4],[2,3],[4,5],[2,4],[2,5],[1,5],[1,4]], 0),
])
class Test:
    def test_solution(self, pairs, expected):
        sol = Solution()
        assert sol.checkWays(pairs) == expected
