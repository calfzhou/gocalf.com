import pytest

from solution import Solution


@pytest.mark.parametrize('param, expected', [
    (0, 0),
    (1, 1),
])
@pytest.mark.parametrize('sol', [Solution()])
class Test:
    def test_solution(self, sol, param, expected):
        assert sol.foo(param) == expected
