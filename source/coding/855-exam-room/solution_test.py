import pytest

from solution import ExamRoom
from solution2 import ExamRoom as ExamRoom2

null = None


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"],
        [[10], [], [], [], [], [4], []],
        [null, 0, 9, 4, 2, null, 5]
    ),

    (
        ["ExamRoom","seat","seat","seat","leave","leave"],
        [[10],[],[],[],[0],[4]],
        [null, 0, 9, 4, null, null]
    )
])
@pytest.mark.parametrize('clazz', [ExamRoom, ExamRoom2])
def test_solution(clazz, actions, params, expects):
    sol = None
    for action, args, expected in zip(actions, params, expects):
        if action == 'ExamRoom':
            sol = clazz(*args)
        else:
            assert getattr(sol, action)(*args) == expected
