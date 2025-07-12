import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([2,3,1,1,4], True),
    ([3,2,1,0,4], False),
])
class Test:
    def test_solution(self, nums, expected):
        sol = Solution()
        assert sol.canJump(nums) == expected
