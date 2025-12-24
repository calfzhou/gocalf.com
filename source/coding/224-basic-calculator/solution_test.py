import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('s, expected', [
    ("1 + 1", 2),
    (" 2-1 + 2 ", 3),
    ("(1+(4+5+2)-3)+(6+8)", 23),

    ("1-(     -2)", 3),
    ("-(2 + 3)", -5),
    ("- (3 + (4 + 5))", -12),

    ("-7", -7),
    ('-3 + 5', 2),
    ('3 + -5', -2),
    ('3 + -(-5)', 8),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, s, expected):
    assert sol.calculate(s) == expected
