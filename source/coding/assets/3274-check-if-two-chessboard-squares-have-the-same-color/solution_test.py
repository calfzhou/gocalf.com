import pytest

from solution import Solution


@pytest.mark.parametrize('coordinate, coordinate2, expected', [
    ("a1", "c3", True),
    ("a1", "h3", False),
])
class Test:
    def test_solution(self, coordinate, coordinate2, expected):
        sol = Solution()
        assert sol.checkTwoChessboards(coordinate, coordinate2) == expected
