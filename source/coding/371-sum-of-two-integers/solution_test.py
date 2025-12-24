import pytest

from solution import Solution


@pytest.mark.parametrize('a, b, expected', [
    (1, 2, 3),
    (2, 3, 5),

    (100, 200, 300),
    (-100, -200, -300),
    (-100, 150, 50),
    (-200, 150, -50),

    (-1, 1, 0),
    (-1, 0, -1),
])
class Test:
    def test_solution(self, a, b, expected):
        sol = Solution()
        assert sol.getSum(a, b) == expected
