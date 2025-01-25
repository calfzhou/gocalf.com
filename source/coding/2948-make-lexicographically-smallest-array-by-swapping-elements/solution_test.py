import pytest

from solution import Solution


@pytest.mark.parametrize('nums, limit, expected', [
    ([1,5,3,9,8], 2, [1,3,5,8,9]),
    ([1,7,6,18,2,1], 3, [1,6,7,18,1,2]),
    ([1,7,28,19,10], 3, [1,7,28,19,10]),

    ([1,60,34,84,62,56,39,76,49,38], 4, [1,56,34,84,60,62,38,76,49,39]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, limit, expected):
    assert sol.lexicographicallySmallestArray(nums.copy(), limit) == expected
