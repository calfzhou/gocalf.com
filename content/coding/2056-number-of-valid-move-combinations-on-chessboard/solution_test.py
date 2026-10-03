import pytest

from solution import Solution


@pytest.mark.parametrize('pieces, positions, expected', [
    (["rook"], [[1,1]], 15),
    (["queen"], [[1,1]], 22),
    (["bishop"], [[4,3]], 12),
    (["rook","rook"], [[1,1],[8,8]], 223),
    (["queen","bishop"], [[5,7],[3,4]], 281),
])
class Test:
    def test_solution(self, pieces, positions, expected):
        sol = Solution()
        assert sol.countCombinations(pieces, positions) == expected
