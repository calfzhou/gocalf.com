class Solution:
    def canChange(self, start: str, target: str) -> bool:
        bal = 0 # bal < 0: there are some `L`s requested by `target`; bal > 0: `start` has some `R`s to move right.
        for s, t in zip(start, target):
            if s == 'R':
                if bal < 0: # `L` is already requested, but get an `R` in `start`.
                    return False
                bal += 1
            if t == 'R':
                if bal <= 0: # `start` doesn't have `R` to match it.
                    return False
                bal -= 1

            if t == 'L':
                if bal > 0: # `start` already had some `R`s, but `target` is `L`.
                    return False
                bal -= 1
            if s == 'L':
                if bal >= 0: # `L` is not requested, but get one.
                    return False
                bal += 1

        return bal == 0
