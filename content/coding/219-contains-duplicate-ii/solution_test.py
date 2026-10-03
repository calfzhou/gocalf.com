import pytest

from solution import Solution


@pytest.mark.parametrize('nums, k, expected', [
    ([1,2,3,1], 3, True),
    ([1,0,1,1], 1, True),
    ([1,2,3,1,2,3], 2, False),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, k, expected):
    assert sol.containsNearbyDuplicate(nums, k) == expected
