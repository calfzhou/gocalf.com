import pytest

from solution import Skiplist

null = None
false = False
true = True


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"],
        [[], [1], [2], [3], [0], [4], [1], [0], [1], [1]],
        [null, null, null, null, false, null, true, false, true, false]
    ),

    (
        ['Skiplist', 'add', 'add', 'add', 'add', 'add', 'add', 'search', 'add', 'add', 'search'],
        [[], [30], [40], [50], [60], [70], [90], [45], [80], [45]],
        [None, None, None, None, None, None, None, False, None, None, True]
    ),
])
@pytest.mark.parametrize('clazz', [Skiplist])
def test_solution(clazz, actions, params, expects):
    sol = None
    for action, args, expected in zip(actions, params, expects):
        if action == 'Skiplist':
            sol = clazz(*args)
        else:
            assert getattr(sol, action)(*args) == expected
