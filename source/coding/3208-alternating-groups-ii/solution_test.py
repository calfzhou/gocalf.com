import pytest

from solution import Solution


@pytest.mark.parametrize('colors, k, expected', [
    ([0,1,0,1,0], 3, 3),
    ([0,1,0,0,1,0,1], 6, 2),
    ([1,1,0,1], 4, 0),
])
class Test:
    def test_solution(self, colors, k, expected):
        sol = Solution()
        assert sol.numberOfAlternatingGroups(colors, k) == expected
