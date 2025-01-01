import pytest

from solution import MyCalendar

null = None
false = False
true = True


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["MyCalendar", "book", "book", "book"],
        [[], [10, 20], [15, 25], [20, 30]],
        [null, true, false, true]
    ),
])
@pytest.mark.parametrize('clazz', [MyCalendar])
def test_solution(clazz, actions, params, expects):
    sol = None
    for action, args, expected in zip(actions, params, expects):
        if action == 'MyCalendar':
            sol = clazz(*args)
        else:
            assert getattr(sol, action)(*args) == expected
