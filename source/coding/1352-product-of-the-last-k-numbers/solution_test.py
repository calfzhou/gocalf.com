import pytest

from solution import ProductOfNumbers

null = None


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"],
        [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]],
        [null,null,null,null,null,null,20,40,0,null,32],
    ),
])
@pytest.mark.parametrize('clazz', [ProductOfNumbers])
def test_solution(clazz, actions, params, expects):
    sol = None
    for action, args, expected in zip(actions, params, expects):
        if action == 'ProductOfNumbers':
            sol = clazz(*args)
        else:
            assert getattr(sol, action)(*args) == expected
