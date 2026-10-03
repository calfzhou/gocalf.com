import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([2,6,4,8,10,9,15], 5),
    ([1,2,3,4], 0),
    ([1], 0),

    ([2, 6, 4, 18, 1, 9, 15], 7),
    ([1, 2], 0),
    ([1, 3, 2, 2, 2], 4),
    ([1, 3, 2, 3, 3], 2),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    assert sol.findUnsortedSubarray(nums) == expected
