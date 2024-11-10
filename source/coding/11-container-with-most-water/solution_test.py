import pytest

from solution import Solution


@pytest.mark.parametrize('height, expected', [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1], 1),

    ([1,8,6,2,5,4,8,25,7], 49)
])
class Test:
    def test_solution(self, height, expected):
        sol = Solution()
        assert sol.maxArea(height) == expected
