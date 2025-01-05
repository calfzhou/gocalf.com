import pytest

from solution import ATM

null = None


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw"],
        [[], [[0,0,1,2,1]], [600], [[0,1,0,1,1]], [600], [550]],
        [null, null, [0,0,1,0,1], null, [-1], [0,1,0,0,1]],
    ),

    (
        ["ATM", "deposit", "withdraw"],
        [[], [[0,2,1,1,0]], [300]],
        [null, null, [0,0,1,1,0]],
    ),
    (
        ["ATM", "deposit", "withdraw"],
        [[], [[0,0,0,3,1]], [600]],
        [null, null, [-1]],
    ),
])
@pytest.mark.parametrize('clazz', [ATM])
def test_solution(clazz, actions, params, expects):
    sol = None
    for action, args, expected in zip(actions, params, expects):
        if action == 'ATM':
            sol = clazz(*args)
        else:
            assert getattr(sol, action)(*args) == expected

