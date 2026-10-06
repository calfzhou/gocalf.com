import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('start, target, expected', [
    ("_L__R__R_", "L______RR", True),
    ("R_L_", "__LR", False),
    ("_R", "R_", False),

    ("RL_", "_RL", False),
])
class Test:
    def test_solution(self, start, target, expected):
        sol = Solution()
        assert sol.canChange(start, target) == expected

    def test_solution2(self, start, target, expected):
        sol = Solution2()
        assert sol.canChange(start, target) == expected
