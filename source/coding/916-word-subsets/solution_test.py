import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('words1, words2, expected', [
    (["amazon","apple","facebook","google","leetcode"], ["e","o"], ["facebook","google","leetcode"]),
    (["amazon","apple","facebook","google","leetcode"], ["l","e"], ["apple","google","leetcode"]),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, words1, words2, expected):
    assert sorted(sol.wordSubsets(words1, words2)) == sorted(expected)
