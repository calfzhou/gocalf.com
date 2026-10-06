import pytest

from solution import BrowserHistory

null = None


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"],
        [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]],
        [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"],
    ),
])
@pytest.mark.parametrize('clazz', [BrowserHistory])
def test_solution(clazz, actions, params, expects):
    sol = None
    for action, args, expected in zip(actions, params, expects):
        if action == 'BrowserHistory':
            sol = clazz(*args)
        else:
            assert getattr(sol, action)(*args) == expected
