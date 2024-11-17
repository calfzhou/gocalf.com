import pytest

from solution import Solution

@pytest.mark.parametrize('nums, expected', [
    ([10,9,2,5,3,7,101,18], 4),
    ([0,1,0,3,2,3], 4),
    ([7,7,7,7,7,7,7], 1),
])
class Test:
    def test_solution(self, nums, expected):
        sol = Solution()
        assert sol.lengthOfLIS(nums) == expected
