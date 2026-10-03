import pytest

from solution import Solution


@pytest.mark.parametrize('height, threshold, expected', [
    ([1,2,3,4,5], 2, [3,4]),
    ([10,1,10,1,10], 3, [1,3]),
    ([10,1,10,1,10], 10, []),
])
@pytest.mark.parametrize('sol', [Solution()])
class Test:
    def test_solution(self, sol, height, threshold, expected):
        result = sol.stableMountains(height, threshold)
        assert sorted(result) == sorted(expected)
