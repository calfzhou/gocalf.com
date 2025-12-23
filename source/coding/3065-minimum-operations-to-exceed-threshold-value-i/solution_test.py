import pytest

from solution import Solution


@pytest.mark.parametrize('nums, k, expected', [
    ([2,11,10,1,3], 10, 3),
    ([1,1,2,4,9], 1, 0),
    ([1,1,2,4,9], 9 ,4),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, k, expected):
    assert sol.minOperations(nums, k) == expected
