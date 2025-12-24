import pytest

from solution import Solution
from solution2 import Solution as Solution2
from solution3 import Solution as Solution3


@pytest.mark.parametrize('n, expected', [
    (1, 10),
    (2, 20),
    (3131, 136006598),
])
class Test:
    def test_solution(self, n, expected):
        sol = Solution()
        assert sol.knightDialer(n) == expected

    def test_solution2(self, n, expected):
        sol = Solution2()
        assert sol.knightDialer(n) == expected

    def test_solution3(self, n, expected):
        sol = Solution3()
        assert sol.knightDialer(n) == expected
