import timeit

from solution import Solution
from solution_log import Solution as SolutionLog

ns = [30, 100, 300, 1000, 3000, 10000]
sols = [Solution(), SolutionLog()]
sols = {
    'linear': Solution(),
    'log(n)': SolutionLog(),
}
for n in ns:
    for name, sol in sols.items():
        timer = timeit.Timer(lambda: sol.climbStairs(n))
        cnt, time = timer.autorange()
        avg = time * 1000000 / cnt
        print(f'[{name}] n = {n:5}: {avg:11.6f} μs')

    print()
