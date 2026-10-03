import pytest

from solution import Solution


@pytest.mark.parametrize('board, word, expected', [
    (
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        "ABCCED",
        True
    ),
    (
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        "SEE",
        True
    ),
    (
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        "ABCB",
        False
    ),

    (
        [['x', 'A', 'D'], ['A', 'B', 'C']],
        'ABCDA',
        True
    ),
    (
        [['x', 'A', 'D'], ['x', 'B', 'C']],
        'ABCDA',
        False
    ),
])
class Test:
    def test_solution(self, board, word, expected):
        sol = Solution()
        assert sol.exist(board, word) == expected
