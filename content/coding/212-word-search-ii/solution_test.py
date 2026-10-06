import pytest

from solution import Solution


@pytest.mark.parametrize('board, words, expected', [
    (
        [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
        ["oath","pea","eat","rain"],
        ["eat","oath"]
    ),
    (
        [["a","b"],["c","d"]],
        ["abcb"],
        []
    ),

    (
        [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
        ["oath","eat","an"],
        ["oath","eat","an"]
    ),
    (
        [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
        ["oath","eat","an","a"],
        ["oath","eat","an","a"]
    ),
])
class Test:
    def test_solution(self, board, words, expected):
        sol = Solution()
        result = sol.findWords(board, words)
        assert sorted(result) == sorted(expected)
