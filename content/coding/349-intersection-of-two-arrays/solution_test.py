import pytest

from solution import Solution


@pytest.mark.parametrize('nums1, nums2, expected', [
    ([1,2,2,1], [2,2], [2]),
    ([4,9,5], [9,4,9,8,4], [9,4]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums1, nums2, expected):
    res = sol.intersection(nums1, nums2)
    assert sorted(res) == sorted(expected)
