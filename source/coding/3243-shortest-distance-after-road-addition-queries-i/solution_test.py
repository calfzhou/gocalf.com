import pytest

from solution import Solution


@pytest.mark.parametrize('n, queries, expected', [
    (5, [[2,4],[0,2],[0,4]], [3,2,1]),
    (4, [[0,3],[0,2]], [1,1]),

    (6, [[1,4],[2,4]], [3,3],)
])
class Test:
    def test_solution(self, n, queries, expected):
        sol = Solution()
        assert sol.shortestDistanceAfterQueries(n, queries) == expected
