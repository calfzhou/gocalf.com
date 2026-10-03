import pytest

from solution import Solution


@pytest.mark.parametrize('n, k, expected', [
    (13, 4, 2),
    (21, 21, 0),
    (14, 13, -1),
])
class Test:
    def test_solution(self, n, k, expected):
        sol = Solution()
        assert sol.minChanges(n, k) == expected
