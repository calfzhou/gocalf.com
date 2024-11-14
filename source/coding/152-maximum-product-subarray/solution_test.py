import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([2,3,-2,4], 6),
    ([-2,0,-1], 0),

    ([5], 5),
    ([0], 0),
    ([-5], -5),
    ([-5, -2], 10),
    ([-5, 2], 2),
    ([-5, 0], 0),
])
class Test:
    def test_solution(self, nums, expected):
        sol = Solution()
        assert sol.maxProduct(nums) == expected
