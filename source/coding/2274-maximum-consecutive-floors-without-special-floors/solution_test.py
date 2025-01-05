import pytest

from solution import Solution


@pytest.mark.parametrize('bottom, top, special, expected', [
    (2, 9, [4,6], 3),
    (6, 8, [7,6,8], 0),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, bottom, top, special, expected):
    assert sol.maxConsecutive(bottom, top, special.copy()) == expected
