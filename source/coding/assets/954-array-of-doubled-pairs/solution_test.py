import pytest

from solution import Solution


@pytest.mark.parametrize('arr, expected', [
    ([3,1,3,6], False),
    ([2,1,2,6], False),
    ([4,-2,2,-4], True),
])
class Test:
    def test_solution(self, arr, expected):
        sol = Solution()
        assert sol.canReorderDoubled(arr.copy()) == expected
