import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('s, expected', [
    ("e + 8 - a + 5", ['e', '+', 8, '-', 'a', '+', 5]),
    ("e - 8 + temperature - pressure", ['e', '-', 8, '+', 'temperature', '-', 'pressure']),
    ("(e + 8) * (e - 8)", ['(', 'e', '+', 8, ')', '*', '(', 'e', '-', 8, ')']),

    ('8 + 2 - 3 * 4', [8, '+', 2, '-', 3, '*', 4]),
    ("7 - 7", [7, '-', 7]),
    ("a * b * c + b * a * c * 4", ['a', '*', 'b', '*', 'c', '+', 'b', '*', 'a', '*', 'c', '*', 4]),
    ('0', [0]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_tokenize(sol, s, expected):
    assert list(sol.tokenize(s)) == expected


@pytest.mark.parametrize('s, evalvars, evalints, expected', [
    ("e + 8 - a + 5", ["e"], [1], [1, 8, '+', 'a', '-', 5, '+']),
    ("e - 8 + temperature - pressure", ["e", "temperature"], [1, 12], [1, 8, '-', 12, '+', 'pressure', '-']),
    ("(e + 8) * (e - 8)", [], [], ['e', 8, '+', 'e', 8, '-', '*']),

    ('8 + 2 - 3 * 4', [], [], [8, 2, '+', 3, 4, '*', '-']),
    ("7 - 7", [], [], [7, 7, '-']),
    ("a * b * c + b * a * c * 4", [], [], ['a', 'b', '*', 'c', '*', 'b', 'a', '*', 'c', '*', 4, '*', '+']),
    ('0', [], [], [0]),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_reverse_polish(sol, s, evalvars, evalints, expected):
    tokens = sol.tokenize(s)
    vars = {k: v for k, v in zip(evalvars, evalints)}
    assert list(sol.reverse_polish(tokens, vars)) == expected
