import pytest

from solution import Solution


@pytest.mark.parametrize('words, expected', [
    (["mass","as","hero","superhero"], ["as","hero"]),
    (["leetcode","et","code"], ["et","code"]),
    (["blue","green","bu"], []),

    (["leetcoder","leetcode","od","hamlet","am"], ["leetcode","od","am"])
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, words, expected):
    assert sorted(sol.stringMatching(words.copy())) == sorted(expected)
