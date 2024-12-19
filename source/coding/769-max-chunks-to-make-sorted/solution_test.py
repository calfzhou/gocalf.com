import pytest

from solution import Solution


@pytest.mark.parametrize('arr, expected', [
    ([4,3,2,1,0], 1),
    ([1,0,2,3,4], 4),
])
@pytest.mark.parametrize('sol', [Solution()])
class Test:
    def test_solution(self, sol, arr, expected):
        assert sol.maxChunksToSorted(arr) == expected
