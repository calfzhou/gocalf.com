import pytest

from solution import Solution


@pytest.mark.parametrize('limit, queries, expected', [
    (4, [[1,4],[2,5],[1,3],[3,4]], [1,2,2,3]),
    (4, [[0,1],[1,2],[2,2],[3,4],[4,5]], [1,2,2,3,4]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, limit, queries, expected):
    assert sol.queryResults(limit, queries) == expected
