import pytest

from solution import Solution


@pytest.mark.parametrize('words, pref, expected', [
    (["pay","attention","practice","attend"], "at", 2),
    (["leetcode","win","loops","success"], "code", 0),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, words, pref, expected):
    assert sol.prefixCount(words, pref) == expected
