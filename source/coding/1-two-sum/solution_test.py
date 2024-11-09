import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('nums, target, expected', [
    ([2,7,11,15], 9, [0, 1]),
    ([3,2,4], 6, [1, 2]),
    ([3,3], 6, [0, 1]),
])
class Test:
    def test_solution(self, nums, target, expected):
        sol = Solution()
        result = sol.twoSum(nums, target)
        assert sorted(result) == sorted(expected)

    def test_solution2(self, nums, target, expected):
        sol = Solution2()
        result = sol.twoSum(nums, target)
        assert sorted(result) == sorted(expected)
