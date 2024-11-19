import pytest

from solution import Solution
from solution2 import Solution as Solution2
from solution3 import Solution as Solution3


@pytest.mark.parametrize('n, expected', [
    (11, 3),
    (128, 1),
    (2147483645, 30),
])
class Test:
    def test_solution(self, n, expected):
        sol = Solution()
        assert sol.hammingWeight(n) == expected

    def test_solution2(self, n, expected):
        sol = Solution2()
        assert sol.hammingWeight(n) == expected

    def test_solution3(self, n, expected):
        sol = Solution3()
        assert sol.hammingWeight(n) == expected
