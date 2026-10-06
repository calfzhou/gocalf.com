import pytest

from solution import Solution


@pytest.mark.parametrize('board, expected', [
    ([[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]], 2),
    ([[0,1],[1,0]], 0),
    ([[1,0],[1,0]], -1),

    ([[1,0],[0,1]], 0),
    ([[1,1,0],[0,0,1],[0,0,1]], 2),
])
class Test:
    def test_solution(self, board, expected):
        sol = Solution()
        assert sol.movesToChessboard(board) == expected
