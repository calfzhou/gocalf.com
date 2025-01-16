import pytest

from solution import Solution


@pytest.mark.parametrize('nums1, nums2, expected', [
    ([2,1,3], [10,2,5,0], 13),
    ([1,2], [3,4], 0),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums1, nums2, expected):
    assert sol.xorAllNums(nums1, nums2) == expected
