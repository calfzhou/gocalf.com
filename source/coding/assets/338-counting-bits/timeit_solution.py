import timeit

from solution import Solution
from solution2 import Solution as Solution2
from solution3 import Solution as Solution3

ns = [10, 100, 1000, 10000, 100000]
sols = [Solution(), Solution2()]
sols = {
    '1:n log n': Solution(),
    '2: linear': Solution2(),
    '3: linear': Solution3(),
}
for n in ns:
    for name, sol in sols.items():
        timer = timeit.Timer(lambda: sol.countBits(n))
        cnt, time = timer.autorange()
        avg = time * 1000000 / cnt
        print(f'[{name}] n = {n:6}: {avg:10.3f} μs')

    print()
