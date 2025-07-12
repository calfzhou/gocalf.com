import pytest

from solution import MyCalendarTwo

null = None
false = False
true = True


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"],
        [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]],
        [null, true, true, true, false, true, true],
    ),

    (
        ["MyCalendarTwo","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"],
        [[],[89,100],[30,43],[92,100],[31,49],[59,76],[60,73],[31,49],[80,99],[48,60],[36,52],[67,82],[96,100],[22,35],[18,32],[9,24],[11,27],[94,100],[12,22],[61,74],[3,20],[14,28],[27,37],[5,20],[1,11],[96,100],[33,44],[90,100],[40,54],[23,35],[18,32],[78,89],[56,66],[83,93],[45,59],[40,59],[94,100],[99,100],[86,96],[43,61],[29,45],[21,36],[13,31],[17,30],[16,30],[80,94],[38,50],[15,30],[62,79],[25,39],[73,85],[39,56],[80,97],[42,57],[32,47],[59,78],[35,53],[56,74],[75,85],[39,54],[63,82]],
        [null,true,true,true,true,true,true,false,false,true,false,false,false,false,false,true,true,false,false,false,false,false,false,false,true,false,false,false,false,false,false,true,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,true,false,false,false,false,false,false,false,false,false,false],
    )
])
@pytest.mark.parametrize('clazz', [MyCalendarTwo])
def test_solution(clazz, actions, params, expects):
    sol = None
    for action, args, expected in zip(actions, params, expects):
        if action == 'MyCalendarTwo':
            sol = clazz(*args)
        else:
            assert getattr(sol, action)(*args) == expected
