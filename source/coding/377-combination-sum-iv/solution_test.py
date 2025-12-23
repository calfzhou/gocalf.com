import pytest

from solution import Solution


@pytest.mark.parametrize('nums, target, expected', [
    ([1,2,3], 4, 7),
    ([9], 3, 0),
])
class Test:
    def test_solution(self, nums, target, expected):
        sol = Solution()
        assert sol.combinationSum4(nums, target) == expected
