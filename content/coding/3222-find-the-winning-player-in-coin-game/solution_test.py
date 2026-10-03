import pytest

from solution import Solution


@pytest.mark.parametrize('x, y, expected', [
    (2, 7, 'Alice'),
    (4, 11, 'Bob'),
])
class Test:
    def test_solution(self, x, y, expected):
        sol = Solution()
        assert sol.winningPlayer(x, y) == expected
