import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('expression, evalvars, evalints, expected', [
    ("e + 8 - a + 5", ["e"], [1], ["-1*a","14"]),
    ("e - 8 + temperature - pressure", ["e", "temperature"], [1, 12], ["-1*pressure","5"]),
    ("(e + 8) * (e - 8)", [], [], ["1*e*e","-64"]),

    ('8 + 2 - 3 * 4', [], [], ['-2']),
    ("7 - 7", [], [], []),
    ("a * b * c + b * a * c * 4", [], [], ["5*a*b*c"]),
    ('0', [], [], []),
    (
        "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))", [], [],
        ["-1*a*a*b*b","2*a*a*b*c","-1*a*a*c*c","1*a*b*b*b","-1*a*b*b*c","-1*a*b*c*c","1*a*c*c*c","-1*b*b*b*c","2*b*b*c*c","-1*b*c*c*c","2*a*a*b","-2*a*a*c","-2*a*b*b","2*a*c*c","1*b*b*b","-1*b*b*c","1*b*c*c","-1*c*c*c","-1*a*a","1*a*b","1*a*c","-1*b*c"]
    ),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, expression, evalvars, evalints, expected):
    assert sol.basicCalculatorIV(expression, evalvars, evalints) == expected
