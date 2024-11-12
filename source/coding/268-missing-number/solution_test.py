import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([3,0,1], 2),
    ([0,1], 2),
    ([9,6,4,2,3,5,7,0,1], 8),
])
class Test:
    def test_solution(self, nums, expected):
        sol = Solution()
        assert sol.missingNumber(nums) == expected
