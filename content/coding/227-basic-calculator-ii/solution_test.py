import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('s, expected', [
    ("3+2*2", 7),
    (" 3/2 ", 1),
    (" 3+5 / 2 ", 5),

    ("14-3/2", 13),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, s, expected):
    assert sol.calculate(s) == expected
