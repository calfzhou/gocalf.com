import pytest

from solution import Solution


@pytest.mark.parametrize('n, k, expected', [
    (1, 3, "c"),
    (1, 4, ""),
    (3, 9, "cab"),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, n, k, expected):
    assert sol.getHappyString(n, k) == expected
