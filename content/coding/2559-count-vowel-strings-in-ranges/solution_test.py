import pytest

from solution import Solution


@pytest.mark.parametrize('words, queries, expected', [
    (["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]], [2,3,0]),
    (["a","e","i"], [[0,2],[0,1],[2,2]], [3,2,1]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, words, queries, expected):
    assert sol.vowelStrings(words, queries) == expected
