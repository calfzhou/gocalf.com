import pytest

from solution import Solution


@pytest.mark.parametrize('param, expected', [
    (100, 100),
    (200, 200),
    (300, 300),
])
@pytest.mark.parametrize('sol', [Solution()])
class Test:
    def test_solution(self, sol, param, expected):
        assert sol.foo(param) == expected
