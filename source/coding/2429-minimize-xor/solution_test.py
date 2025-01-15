import pytest

from solution import Solution


@pytest.mark.parametrize('num1, num2, expected', [
    (3, 5, 3),
    (1, 12, 3),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, num1, num2, expected):
    assert sol.minimizeXor(num1, num2) == expected
