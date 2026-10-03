import pytest

from solution import Solution


@pytest.mark.parametrize('position, m, expected', [
    ([1,2,3,4,7], 3, 3),
    ([5,4,3,2,1,1000000000], 2, 999999999),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, position, m, expected):
    assert sol.maxDistance(position.copy(), m) == expected
