import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([2,3,2], 3),
    ([1,2,3,1], 4),
    ([1,2,3], 3),

    ([1], 1),
])
class Test:
    def test_solution(self, nums, expected):
        sol = Solution()
        assert sol.rob(nums) == expected
