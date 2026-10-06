import pytest

from solution import Allocator

null = None


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["Allocator", "allocate", "allocate", "allocate", "freeMemory", "allocate", "allocate", "allocate", "freeMemory", "allocate", "freeMemory"],
        [[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]],
        [null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0],
    ),

    (
        ["Allocator","freeMemory","freeMemory","freeMemory","freeMemory","freeMemory","allocate","allocate","allocate","freeMemory","freeMemory","freeMemory","allocate","allocate","freeMemory","freeMemory","freeMemory","allocate","allocate","freeMemory","allocate","allocate","allocate","freeMemory","freeMemory","freeMemory","freeMemory","freeMemory","freeMemory","freeMemory","allocate","freeMemory","allocate","freeMemory","allocate","allocate","freeMemory","allocate","allocate","freeMemory","freeMemory","allocate","freeMemory","freeMemory","allocate","allocate","allocate","freeMemory","allocate","allocate","freeMemory","freeMemory","allocate","allocate","allocate","freeMemory","allocate","allocate","freeMemory","freeMemory","freeMemory","allocate","freeMemory","freeMemory","freeMemory","freeMemory","allocate","allocate","allocate","freeMemory","allocate","freeMemory","freeMemory","allocate","freeMemory","allocate","freeMemory","freeMemory"],
        [[100],[27],[12],[53],[61],[80],[21,78],[81,40],[50,76],[40],[76],[63],[25,100],[96,12],[92],[92],[84],[19,71],[22,90],[60],[42,79],[26,41],[59,33],[79],[58],[97],[92],[97],[92],[40],[52,74],[40],[53,17],[17],[36,32],[51,13],[41],[5,87],[44,66],[71],[53],[74,14],[78],[14],[32,54],[45,28],[84,47],[16],[100,78],[5,99],[33],[100],[62,79],[31,32],[85,81],[78],[34,45],[47,7],[7],[84],[6],[35,55],[94],[87],[20],[87],[96,60],[40,66],[28,96],[28],[25,2],[100],[96],[19,35],[16],[92,42],[80],[79]],
        [null,0,0,0,0,0,0,-1,21,0,50,0,21,-1,0,0,0,46,65,0,-1,-1,-1,0,0,0,0,0,0,0,-1,0,-1,0,-1,-1,0,87,-1,19,0,-1,21,0,-1,-1,-1,0,-1,0,0,25,-1,5,-1,0,-1,-1,0,0,0,-1,0,5,0,0,-1,-1,36,0,-1,0,28,36,0,-1,0,0],
    ),
])
@pytest.mark.parametrize('clazz', [Allocator])
def test_solution(clazz, actions, params, expects):
    sol = None
    for action, args, expected in zip(actions, params, expects):
        if action == 'Allocator':
            sol = clazz(*args)
        else:
            assert getattr(sol, action)(*args) == expected
