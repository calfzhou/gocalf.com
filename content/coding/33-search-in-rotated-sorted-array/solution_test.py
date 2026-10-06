import pytest

from solution import Solution


@pytest.mark.parametrize('nums, target, expected', [
    ([4,5,6,7,0,1,2], 0, 4),
    ([4,5,6,7,0,1,2], 3, -1),
    ([-1], 0, -1),
])
class Test:
    def test_solution(self, nums, target, expected):
        sol = Solution()
        assert sol.search(nums, target) == expected
