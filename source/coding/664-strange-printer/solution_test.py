import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('s, expected', [
    ("aaabbb", 2),
    ("aba", 2),

    ("baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa", 19),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, s, expected):
    assert sol.strangePrinter(s) == expected
