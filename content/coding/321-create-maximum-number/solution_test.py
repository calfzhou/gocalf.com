import pytest

from solution import Solution


@pytest.mark.parametrize('nums1, nums2, k, expected', [
    ([3,4,6,5], [9,1,2,5,8,3], 5, [9,8,6,5,3]),
    ([6,7], [6,0,4], 5, [6,7,6,0,4]),
    ([3,9], [8,9], 3, [9,8,9]),

    ([6,7,5], [4,8,1], 3, [8,7,5]),
    ([8, 9], [3, 9], 3, [9, 8, 9]),
    ([7,6,1,9,3,2,3,1,1], [4,0,9,9,0,5,5,4,7], 9, [9,9,9,7,3,2,3,1,1]),

    ([2,5,6,4,4,0], [7,3,8,0,6,5,7,6,2], 15, [7,3,8,2,5,6,4,4,0,6,5,7,6,2,0]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums1, nums2, k, expected):
    assert sol.maxNumber(nums1, nums2, k) == expected
