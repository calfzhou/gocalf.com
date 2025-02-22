import pytest

from solution import Solution


@pytest.mark.parametrize('words, expected', [
    (["aba","aabb","abcd","bac","aabc"], 2),
    (["aabb","ab","ba"], 3),
    (["nba","cba","dba"], 0),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, words, expected):
    assert sol.similarPairs(words) == expected
