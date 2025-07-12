import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('nums, k, expected', [
    ([4,6,1,2], 2, 3),
    ([1,1,1,1], 10, 4),
])
class Test:
    def test_solution(self, nums, k, expected):
        sol = Solution()
        assert sol.maximumBeauty(nums.copy(), k) == expected

    def test_solution2(self, nums, k, expected):
        sol = Solution2()
        assert sol.maximumBeauty(nums.copy(), k) == expected
