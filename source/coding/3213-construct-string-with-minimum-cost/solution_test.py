import pytest

from solution import Solution


@pytest.mark.parametrize('target, words, costs, expected', [
    ("abcdef", ["abdef","abc","d","def","ef"], [100,1,1,10,5], 7),
    ("aaaa", ["z","zz","zzz"], [1,10,100], -1),

    ("r", ["r","r","r","r"], [1,6,3,3], 1),
])
class Test:
    def test_solution(self, target, words, costs, expected):
        sol = Solution()
        assert sol.minimumCost(target, words.copy(), costs.copy()) == expected
