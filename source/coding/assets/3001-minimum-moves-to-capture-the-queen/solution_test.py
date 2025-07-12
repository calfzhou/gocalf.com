import pytest

from solution import Solution


@pytest.mark.parametrize('params, expected', [
    ([1, 1, 8, 8, 2, 3], 2),
    ([5, 3, 3, 4, 5, 2], 1),
])
class Test:
    def test_solution(self, params, expected):
        sol = Solution()
        assert sol.minMovesToCaptureTheQueen(*params) == expected
