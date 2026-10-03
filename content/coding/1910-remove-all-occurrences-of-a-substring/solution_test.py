import pytest

from solution import Solution


@pytest.mark.parametrize('s, part, expected', [
    ("daabcbaabcbc", "abc", "dab"),
    ("axxxxyyyyb", "xy", "ab"),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, s, part, expected):
    assert sol.removeOccurrences(s, part) == expected
