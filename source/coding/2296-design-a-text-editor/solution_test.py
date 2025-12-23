import pytest

from solution import TextEditor

null = None


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft", "cursorRight"],
        [[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]],
        [null, null, 4, null, "etpractice", "leet", 4, "", "practi"],
    ),
])
@pytest.mark.parametrize('clazz', [TextEditor])
def test_solution(clazz, actions, params, expects):
    sol = None
    for action, args, expected in zip(actions, params, expects):
        if action == 'TextEditor':
            sol = clazz(*args)
        else:
            assert getattr(sol, action)(*args) == expected
