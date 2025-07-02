import pytest

from solution import Solution


@pytest.mark.parametrize('votes, expected', [
    (["ABC","ACB","ABC","ACB","ACB"], "ACB"),
    (["WXYZ","XYZW"], "XWYZ"),
    (["ZMNAGUEDSJYLBOPHRQICWFXTVK"], "ZMNAGUEDSJYLBOPHRQICWFXTVK"),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, votes, expected):
    assert sol.rankTeams(votes) == expected
