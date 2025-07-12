import pytest

from solution import Solution


@pytest.mark.parametrize('words, expected', [
    (["a","aba","ababa","aa"], 4),
    (["pa","papa","ma","mama"], 2),
    (["abab","ab"], 0),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, words, expected):
    assert sol.countPrefixSuffixPairs(words) == expected
