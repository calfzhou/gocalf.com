import pytest

from solution import Solution


@pytest.mark.parametrize('floor, numCarpets, carpetLen, expected', [
    ("10110101", 2, 2, 2),
    ("11111", 2, 3, 0),

    ("1110111", 2, 1, 4),
    ("110000", 1, 1, 1),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, floor, numCarpets, carpetLen, expected):
    assert sol.minimumWhiteTiles(floor, numCarpets, carpetLen) == expected
