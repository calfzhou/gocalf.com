import timeit

from solution import Solution
from solution2 import Solution as Solution2
from solution3 import Solution as Solution3

ns = [30, 100, 300, 1000, 3000, 10000]
sols = [Solution(), Solution2(), Solution3()]
sols = {
    '1': Solution(),
    '2': Solution2(),
    '3': Solution3(),
}
for n in ns:
    for name, sol in sols.items():
        timer = timeit.Timer(lambda: sol.knightDialer(n))
        cnt, time = timer.autorange()
        avg = time * 1000000 / cnt
        print(f'[{name}] n = {n:5}: {avg:11.6f} μs')

    print()
