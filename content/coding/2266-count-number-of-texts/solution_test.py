import pytest

from solution import Solution


@pytest.mark.parametrize('pressedKeys, expected', [
    ("22233", 8),
    ("222222222222222222222222222222222222", 82876089),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, pressedKeys, expected):
    assert sol.countTexts(pressedKeys) == expected
