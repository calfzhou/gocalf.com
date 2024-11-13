import argparse
import importlib
from pathlib import Path
import timeit

from solution import Solution


def main():
    parser = argparse.ArgumentParser(description='Timeit a Huge Case',
                                     allow_abbrev=False, 
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('case_file', help='python file name of a huge case')
    parser.add_argument('limit', nargs='?', type=int, help='only run given number of queries')
    args = parser.parse_args()


    module_name = Path(args.case_file).stem
    case = importlib.import_module(module_name)
    s, k, queries = case.s, case.k, case.queries
    limit = args.limit
    print(f'[{module_name}]: {len(s) = }, {k = }, {len(queries) = }')
    if limit is not None:
        print(f'only run {limit} queries')

    stmt = lambda: Solution().countKConstraintSubstrings(s, 1, queries[:limit])
    t = timeit.timeit(stmt, number=1)
    print('timeit:', t)


if __name__ == '__main__':
    main()
