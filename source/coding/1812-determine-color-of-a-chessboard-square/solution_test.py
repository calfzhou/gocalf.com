import pytest

from solution import Solution


@pytest.mark.parametrize('coordinates, expected', [
    ("a1", False),
    ("h3", True),
    ("c7", False),
])
class Test:
    def test_solution(self,coordinates, expected):
        sol = Solution()
        assert sol.squareIsWhite(coordinates) == expected
