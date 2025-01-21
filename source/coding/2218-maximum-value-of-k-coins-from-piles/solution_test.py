import pytest

from solution import Solution


@pytest.mark.parametrize('piles, k, expected', [
    ([[1,100,3],[7,8,9]], 2, 101),
    ([[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], 7, 706),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, piles, k, expected):
    assert sol.maxValueOfCoins(piles.copy(), k) == expected
