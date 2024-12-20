import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ("1 + 1", [1, '+', 1]),
    (" 2-1 + 2 ", [2, '-', 1, '+', 2]),
    ("(1+(4+5+2)-3)+(6+8)", ['(', 1, '+', '(', 4, '+', 5, '+', 2, ')', '-', 3, ')', '+', '(', 6, '+', 8, ')']),

    ("1-(     -2)", [1, '-', '(', '-', 2, ')']),
    ("-(2 + 3)", ['-', '(', 2, '+', 3, ')']),
    ("- (3 + (4 + 5))", ['-', '(', 3, '+', '(', 4, '+', 5, ')', ')']),

    ("-7", ['-', 7]),
    ('-3 + 5', ['-', 3, '+', 5]),
    ('3 + -5', [3, '+', '-', 5]),
    ('3 + -(-5)', [3, '+', '-', '(', '-', 5, ')']),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_tokenize(sol, s, expected):
    assert list(sol.tokenize(s)) == expected


@pytest.mark.parametrize('s, expected', [
    ("1 + 1", [1, 1, '+']),
    (" 2-1 + 2 ", [2, 1, '-', 2, '+']),
    ("(1+(4+5+2)-3)+(6+8)", [1, 4, 5, '+', 2, '+', '+', 3, '-', 6, 8, '+', '+']),

    ("1-(     -2)", [1, 2, 'n', '-']),
    ("-(2 + 3)", [2, 3, '+', 'n']),
    ("- (3 + (4 + 5))", [3, 4, 5, '+', '+', 'n']),

    ("-7", [7, 'n']),
    ('-3 + 5', [3, 'n', 5, '+']),
    ('3 + -5', [3, 5, 'n', '+']),
    ('3 + -(-5)', [3, 5, 'n', 'n', '+']),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_reverse_polish(sol, s, expected):
    tokens = sol.tokenize(s)
    assert list(sol.reverse_polish(tokens)) == expected
