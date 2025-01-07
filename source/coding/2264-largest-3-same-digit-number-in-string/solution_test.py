import pytest

from solution import Solution


@pytest.mark.parametrize('num, expected', [
    ("6777133339", "777"),
    ("2300019", "000"),
    ("42352338", ""),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, num, expected):
    assert sol.largestGoodInteger(num) == expected
