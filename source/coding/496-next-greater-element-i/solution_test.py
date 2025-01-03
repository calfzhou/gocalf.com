import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('nums1, nums2, expected', [
    ([4,1,2], [1,3,4,2], [-1,3,-1]),
    ([2,4], [1,2,3,4], [3,-1]),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
class Test:
    def test_solution(self, sol, nums1, nums2, expected):
        assert sol.nextGreaterElement(nums1.copy(), nums2) == expected
