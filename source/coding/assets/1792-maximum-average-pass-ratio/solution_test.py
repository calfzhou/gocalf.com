import pytest

from solution import Solution


@pytest.mark.parametrize('classes, extraStudents, expected', [
    ([[1,2],[3,5],[2,2]], 2, 0.78333),
    ([[2,4],[3,9],[4,5],[2,10]], 4, 0.53485),
])
class Test:
    def test_solution(self, classes, extraStudents, expected):
        sol = Solution()
        assert sol.maxAverageRatio(classes, extraStudents) == pytest.approx(expected, abs=1e-5)
