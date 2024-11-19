import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('n, expected', [
    (0b00000010100101000001111010011100, 964176192),
    (0b11111111111111111111111111111101, 3221225471),
])
class Test:
    def test_solution(self, n, expected):
        sol = Solution()
        assert sol.reverseBits(n) == expected

    def test_solution2(self, n, expected):
        sol = Solution2()
        assert sol.reverseBits(n) == expected

