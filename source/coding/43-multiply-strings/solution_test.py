import pytest

from solution import Solution


@pytest.mark.parametrize('num1, num2, expected', [
    ('2', '3', '6'),
    ('123', '456', '56088'),

    ("123456789", "987654321", "121932631112635269"),
    ('9', '9', '81'),
    ('99', '99', '9801'),
    ('1000', '1000', '1000000'),
])

@pytest.mark.parametrize('sol', [Solution()])
class Test:
    def test_solution(self, sol, num1, num2, expected):
        assert sol.multiply(num1, num2) == expected
