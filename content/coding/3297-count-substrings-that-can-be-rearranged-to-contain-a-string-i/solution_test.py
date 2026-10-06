import pytest

from solution import Solution


@pytest.mark.parametrize('word1, word2, expected', [
    ("bcca", "abc", 1),
    ("abcabc", "abc", 10),
    ("abcabc", "aaabc", 0),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, word1, word2, expected):
    assert sol.validSubstringCount(word1, word2) == expected
