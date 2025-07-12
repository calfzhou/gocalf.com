import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ("acab", 1), # -1 a.
    ("wddw", 0),
    ("aaabc", 2), # -2 a.

    ("ruuu", 1), # -1 r.
    ("gigigjjggjjgg", 3), # -1 g, 2 i to j.
    ("ympylhyyyhmyhlypylyphylhpyyynyhplymyyylyppyypnhllympymnnyylmh", 23), # +1 h, -1 m, 5 m to n, -16 y.
    ("accdddddbebbabbe", 5), # +1 a, -1 b, 1 b to c, -1 d, 1 d to e.
])
@pytest.mark.parametrize('sol', [Solution()])
class Test:
    def test_solution(self, sol, s, expected):
        assert sol.makeStringGood(s) == expected
