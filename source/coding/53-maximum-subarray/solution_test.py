import pytest

from solution import Solution
from solution2 import Solution as Solution2
from solution3 import Solution as Solution3


@pytest.mark.parametrize('nums, expected', [
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
    ([1], 1),
    ([5,4,-1,7,8], 23),
])
class Test:
    def test_solution(self, nums, expected):
        sol = Solution()
        assert sol.maxSubArray(nums) == expected

    def test_solution2(self, nums, expected):
        sol = Solution2()
        assert sol.maxSubArray(nums) == expected

    def test_solution3(self, nums, expected):
        sol = Solution3()
        assert sol.maxSubArray(nums) == expected
