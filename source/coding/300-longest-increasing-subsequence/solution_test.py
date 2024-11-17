import pytest

from solution import Solution
from solution_nlogn import Solution as SolutionNlogn
from solution_nlogn_1 import Solution as SolutionNlogn1

@pytest.mark.parametrize('nums, expected', [
    ([10,9,2,5,3,7,101,18], 4),
    ([0,1,0,3,2,3], 4),
    ([7,7,7,7,7,7,7], 1),

    ([6,3,5,10,11,2,9,14,13,7,4,8,12], 5),
])
class Test:
    def test_solution(self, nums, expected):
        sol = Solution()
        assert sol.lengthOfLIS(nums) == expected

    def test_solution_nlogn(self, nums, expected):
        sol = SolutionNlogn()
        assert sol.lengthOfLIS(nums) == expected

    def test_solution_nlogn1(self, nums, expected):
        sol = SolutionNlogn1()
        assert sol.lengthOfLIS(nums) == expected
