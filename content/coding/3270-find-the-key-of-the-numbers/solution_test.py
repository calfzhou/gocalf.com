import pytest

from solution import Solution


@pytest.mark.parametrize('num1, num2, num3, expected', [
    (1, 10, 1000, 0),
    (987, 879, 798, 777),
    (1, 2, 3, 1),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, num1, num2, num3, expected):
    assert sol.generateKey(num1, num2, num3) == expected
