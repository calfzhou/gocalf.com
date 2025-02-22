import pytest

from solution import Solution


@pytest.mark.parametrize('traversal, expected', [
    ("1-2--3--4-5--6--7", [(0,1), (1,2), (2,3), (2,4), (1,5), (2,6), (2,7)]),
    ("1-2--3---4-5--6---7", [(0,1), (1,2), (2,3), (3,4), (1,5), (2,6), (3,7)]),
    ("1-401--349---90--88", [(0,1), (1,401), (2,349), (3,90), (2,88)]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, traversal, expected):
    res = sol.tokenize(traversal)
    assert list(res) == expected
