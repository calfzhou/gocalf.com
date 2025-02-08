import pytest

from solution import NumberContainers

null = None


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"],
        [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]],
        [null, -1, null, null, null, null, 1, null, 2],
    ),
])
@pytest.mark.parametrize('clazz', [NumberContainers])
def test_solution(clazz, actions, params, expects):
    sol = None
    for action, args, expected in zip(actions, params, expects):
        if action == 'NumberContainers':
            sol = clazz(*args)
        else:
            assert getattr(sol, action)(*args) == expected
