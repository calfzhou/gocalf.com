import pytest

from solution import Solution


@pytest.mark.parametrize('s, k, expected', [
    ("abcdefg", 2, "bacdfeg"),
    ("abcd", 2, "bacd"),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, s, k, expected):
    assert sol.reverseStr(s, k) == expected
