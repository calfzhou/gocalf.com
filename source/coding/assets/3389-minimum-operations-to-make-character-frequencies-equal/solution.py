class Solution:
    def makeStringGood(self, s: str) -> int:
        min2 = lambda a, b: a if a <= b else b
        max2 = lambda a, b: a if a >= b else b

        counts = [0] * 26
        for c in s: counts[ord(c) - 97] += 1
        chars = [i for i, f in enumerate(counts) if f > 0]
        top = max(counts)

        result = len(s)
        for target in range(top + 1):
            ops = p_ops = 0
            _del = 0
            pc = -2
            for c in chars:
                freq = counts[c]
                if freq >= target:
                    _del = freq - target
                    curr_ops = ops + _del # Delete some `c`s to reach `target`.
                else:
                    ins = target - freq
                    curr_ops = ops + ins # Insert some `c`s to reach `target`.
                    if pc == c - 1:
                        curr_ops = min2(
                            ops + max2(0, ins - _del), # Change some `c-1`s to `c`.
                            p_ops + counts[pc] + max2(0, ins - counts[pc]), # # Change some `c-1`s to `c`, delete others.
                        )

                    _del = 0
                    if curr_ops > ops + freq:
                        curr_ops = ops + freq # Delete all `c`s.
                        _del = freq

                if curr_ops >= result: break # Pruning.
                pc = c
                p_ops, ops = ops, curr_ops
            else:
                result = ops

        return result
