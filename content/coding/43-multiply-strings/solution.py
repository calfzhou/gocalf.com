class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num2 == '0' or num1 == '1': return num2
        elif num1 == '0' or num2 == '1': return num1

        digits1 = [int(d) for d in num1]
        digits2 = [int(d) for d in num2]
        res = [0] * (len(num1) + len(num2))
        for i, d1 in enumerate(digits1):
            if d1 == 0: continue
            for j, d2 in enumerate(digits2):
                if d2 > 0:
                    res[i+j+1] += d1 * d2

        for i in range(len(res) - 1, 0, -1): # res[0] is for final carry, it is 0 now.
            c, res[i] = divmod(res[i], 10)
            res[i-1] += c

        i = 0 if res[0] else 1
        return ''.join(str(d) for d in res[i:])
