import pytest

from solution import RangeFreqQuery

null = None


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["RangeFreqQuery", "query", "query"],
        [[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]],
        [null, 1, 2],
    ),
])
@pytest.mark.parametrize('clazz', [RangeFreqQuery])
def test_solution(clazz, actions, params, expects):
    sol = None
    for action, args, expected in zip(actions, params, expects):
        if action == 'RangeFreqQuery':
            sol = clazz(*args)
        else:
            assert getattr(sol, action)(*args) == expected
