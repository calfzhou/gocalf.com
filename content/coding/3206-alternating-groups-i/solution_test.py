import pytest

from solution import Solution


@pytest.mark.parametrize('colors, expected', [
    ([1,1,1], 0),
    ([0,1,0,0,1], 3),
])
class Test:
    def test_solution(self, colors, expected):
        sol = Solution()
        assert sol.numberOfAlternatingGroups(colors) == expected
