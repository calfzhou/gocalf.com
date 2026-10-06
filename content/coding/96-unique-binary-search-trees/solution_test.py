import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('n, expected', [
    (3, 5),
    (1, 1),

    (5, 42),
    (19, 1767263190),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, n, expected):
    assert sol.numTrees(n) == expected
