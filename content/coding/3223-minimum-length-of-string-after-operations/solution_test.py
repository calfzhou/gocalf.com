import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ("abaacbcbb", 5),
    ("aa", 2),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, s, expected):
    assert sol.minimumLength(s) == expected
