import pytest

from solution import OrderedStream

null = None


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["OrderedStream", "insert", "insert", "insert", "insert", "insert"],
        [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]],
        [null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]],
    ),
])
@pytest.mark.parametrize('clazz', [OrderedStream])
def test_solution(clazz, actions, params, expects):
    sol = None
    for action, args, expected in zip(actions, params, expects):
        if action == 'OrderedStream':
            sol = clazz(*args)
        else:
            assert getattr(sol, action)(*args) == expected
