import pytest

from solution import Solution


@pytest.mark.parametrize('events, expected', [
    ([[1,3,2],[4,5,2],[2,4,3]], 4),
    ([[1,3,2],[4,5,2],[1,5,5]], 5),
    ([[1,5,3],[1,5,1],[6,6,5]], 8),

    ([[35,90,47],[72,80,70]], 70),
    ([[10,83,53],[63,87,45],[97,100,32],[51,61,16]], 85),
])
class Test:
    def test_solution(self, events, expected):
        sol = Solution()
        assert sol.maxTwoEvents(events.copy()) == expected
