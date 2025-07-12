import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([2,1,3,4,5,2], 7),
    ([2,3,5,1,3,2], 5),
])
class Test:
    def test_solution(self, nums, expected):
        sol = Solution()
        assert sol.findScore(nums) == expected
