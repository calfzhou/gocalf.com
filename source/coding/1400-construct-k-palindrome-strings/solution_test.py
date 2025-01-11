import pytest

from solution import Solution


@pytest.mark.parametrize('s, k, expected', [
    ("annabelle", 2, True),
    ("leetcode", 3, False),
    ("true", 4, True),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, s, k, expected):
    assert sol.canConstruct(s, k) == expected
