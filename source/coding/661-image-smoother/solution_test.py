import pytest

from solution import Solution


@pytest.mark.parametrize('img, expected', [
    ([[1,1,1],[1,0,1],[1,1,1]], [[0,0,0],[0,0,0],[0,0,0]]),
    ([[100,200,100],[200,50,200],[100,200,100]], [[137,141,137],[141,138,141],[137,141,137]])
])
class Test:
    def test_solution(self, img, expected):
        sol = Solution()
        assert sol.imageSmoother(img) == expected
