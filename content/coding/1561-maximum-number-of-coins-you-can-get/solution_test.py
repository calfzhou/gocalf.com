import pytest

from solution import Solution


@pytest.mark.parametrize('piles, expected', [
    ([2,4,1,2,7,8], 9),
    ([2,4,5], 4),
    ([9,8,7,6,5,1,2,3,4], 18),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, piles, expected):
    assert sol.maxCoins(piles.copy()) == expected
