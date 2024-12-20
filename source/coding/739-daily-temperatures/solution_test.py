import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('temperatures, expected', [
    ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
    ([30,40,50,60], [1,1,1,0]),
    ([30,60,90], [1,1,0]),

    ([89,62,70,58,47,47,46,76,100,70], [8,1,5,4,3,2,1,1,0,0]),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
class Test:
    def test_solution(self, sol, temperatures, expected):
        assert sol.dailyTemperatures(temperatures.copy()) == expected
