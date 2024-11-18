import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
    ([1], 1),
    ([5,4,-1,7,8], 23),
])
class Test:
    def test_solution(self, nums, expected):
        sol = Solution()
        assert sol.maxSubArray(nums) == expected
