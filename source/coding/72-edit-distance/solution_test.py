import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('word1, word2, expected', [
    ("horse", "ros", 3),
    ("intention", "execution", 5),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, word1, word2, expected):
    assert sol.minDistance(word1, word2) == expected
