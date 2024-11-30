import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3,4,10], False),
    ([1,2,3,4,5,14], True),
    ([5,5,5,25], True),
])
class Test:
    def test_solution(self, nums, expected):
        sol = Solution()
        assert sol.canAliceWin(nums) == expected
