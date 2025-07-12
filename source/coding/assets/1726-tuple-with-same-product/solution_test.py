import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([2,3,4,6], 8),
    ([1,2,4,5,10], 16),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    assert sol.tupleSameProduct(nums) == expected
