import pytest

from solution import Solution


@pytest.mark.parametrize('grid, catJump, mouseJump, expected', [
    (["####F","#C...","M...."], 1, 2, True),
    (["M.C...F"], 1, 4, True),
    (["M.C...F"], 1, 3, False),

    (["..#C","...#","..M.","#F..","...."], 2, 1, True),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, grid, catJump, mouseJump, expected):
    assert sol.canMouseWin(grid, catJump, mouseJump) == expected
