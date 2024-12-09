import pytest

from solution import Solution


@pytest.mark.parametrize('param, expected', [
    (0, 0),
    (1, 1),
])
class Test:
    def test_solution(self, param, expected):
        sol = Solution()
        assert sol.foo(param) == expected
