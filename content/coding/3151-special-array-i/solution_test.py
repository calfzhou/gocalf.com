import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([1], True),
    ([2,1,4], True),
    ([4,3,1,6], False),
])
class Test:
    def test_solution(self,nums, expected):
        sol = Solution()
        assert sol.isArraySpecial(nums) == expected
