import pytest

from solution import Solution


@pytest.mark.parametrize('s, k, queries, expected', [
    ('0001111', 2, [[0,6]], [26]),
    ('010101', 1, [[0,5],[1,4],[2,3]], [15,9,3]),

    ('000', 1, [[0,0],[0,1],[0,2],[1,1],[1,2],[2,2]], [1,3,6,1,3,1])
])
class Test:
    def test_solution(self, s, k, queries, expected):
        sol = Solution()
        assert sol.countKConstraintSubstrings(s, k, queries) == expected
