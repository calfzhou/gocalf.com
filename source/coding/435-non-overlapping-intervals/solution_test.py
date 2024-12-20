import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('intervals, expected', [
    ([[1,2],[2,3],[3,4],[1,3]], 1),
    ([[1,2],[1,2],[1,2]], 2),
    ([[1,2],[2,3]], 0),

    (
        [[-70,27],[-41,11],[78,85],[-95,55],[-63,4],[-96,38],[33,65],[-16,38],[-43,15],[-69,-7],[64,67],[-33,97],[58,74],[75,83],[87,94],[-64,20],[-77,-7],[48,65],[-80,3],[-10,61],[71,87],[75,82],[-79,-34],[-67,50],[-13,4],[34,42],[-50,-12],[32,51],[-73,40],[18,87],[-16,74],[-27,75],[15,60],[-15,63],[-70,57],[-6,57],[-77,85],[59,94],[38,73],[18,25],[-57,36],[88,95],[72,98],[38,40],[-73,9],[-27,60],[79,92],[-77,47],[47,67],[86,96],[16,44],[37,54],[37,76],[-92,-81],[90,92],[77,84],[-88,5],[26,64],[13,26],[-42,-36],[-96,60],[98,100],[92,94],[94,100],[63,70],[-41,-22],[6,38],[-53,-5],[35,79],[49,50],[-46,-15],[90,93],[-45,63],[20,48],[-50,-30],[17,85],[-9,97],[-97,-12],[43,96],[-4,64],[-34,60],[29,87],[-90,-59],[46,81],[-77,86],[56,86],[-30,-24],[-39,-37],[-17,44],[-40,-1],[71,81]],
        79
    ),
])
class Test:
    def test_solution(self, intervals, expected):
        sol = Solution()
        assert sol.eraseOverlapIntervals(intervals) == expected

    def test_solution2(self, intervals, expected):
        sol = Solution2()
        assert sol.eraseOverlapIntervals(intervals) == expected
