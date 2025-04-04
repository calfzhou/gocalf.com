import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('edges, expected', [
    ([3,3,4,2,3], 3),
    ([2,-1,3,1], -1),

    ([3,4,0,2,-1,2], 3),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, edges, expected):
    assert sol.longestCycle(edges) == expected
