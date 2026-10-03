import pytest

from solution import Solution


@pytest.mark.parametrize('n, commands, expected', [
    (2, ["RIGHT","DOWN"], 3),
    (3, ["DOWN","RIGHT","UP"], 1),
])
class Test:
    def test_solution(self, n, commands, expected):
        sol = Solution()
        assert sol.finalPositionOfSnake(n, commands) == expected
