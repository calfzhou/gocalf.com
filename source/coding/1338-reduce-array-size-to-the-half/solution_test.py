import pytest

from solution import Solution


@pytest.mark.parametrize('arr, expected', [
    ([3,3,3,3,5,5,5,2,2,7], 2),
    ([7,7,7,7,7,7], 1),

    ([1,9], 1),
])
class Test:
    def test_solution(self, arr, expected):
        sol = Solution()
        assert sol.minSetSize(arr) == expected
