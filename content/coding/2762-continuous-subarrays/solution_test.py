import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([5,4,2,4], 8),
    ([1,2,3], 6),
])
class Test:
    def test_solution(self, nums, expected):
        sol = Solution()
        assert sol.continuousSubarrays(nums) == expected
