import pytest

from solution import Solution


@pytest.mark.parametrize('nums1, nums2, x, expected', [
    ([1,2,3], [1,2,3], 4, 3),
    ([1,2,3], [3,3,3], 4, -1),

    ([8,2,3], [1,4,2], 13, 0),
    ([9,2,8,3,1,9,7,6], [0,3,4,1,3,4,2,1], 40, 8),
    ([6,6,8,7,1,7], [2,2,1,1,2,3], 27, 5),
    ([10,4,1,10,7,5,6,3,2,10], [4,0,4,0,3,4,3,0,0,3], 50, 9),
])
class Test:
    def test_solution(self, nums1, nums2, x, expected):
        sol = Solution()
        assert sol.minimumTime(nums1.copy(), nums2.copy(), x) == expected
