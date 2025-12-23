import pytest

from solution import Solution


@pytest.mark.parametrize('tiles, expected', [
    ("AAB", 8),
    ("AAABBC", 188),
    ("V", 1),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, tiles, expected):
    assert sol.numTilePossibilities(tiles) == expected
