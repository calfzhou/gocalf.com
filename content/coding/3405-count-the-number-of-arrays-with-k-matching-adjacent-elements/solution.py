MAX = 100_000
MOD = 1_000_000_007


def bi_power_mod(a: int, n: int) -> int:
    """Calculates x ** n % MOD."""
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % MOD
        n >>= 1
        a = a * a % MOD

    return res


def mod_inverse(a: int) -> int:
    """Calculates a's modular multiplicative inverse b where (a * b) % MOD == 1.
    b = a ** (p - 2)
    """
    return bi_power_mod(a, MOD - 2)


# Pre-calculate factorial(i) % MOD, and mode_inverse(factorial(i))
facts = [1] * MAX
inv_facts = [0] * MAX
for i in range(1, MAX):
    facts[i] = facts[i - 1] * i % MOD
inv_facts[-1] = mod_inverse(facts[-1])
for i in range(MAX - 2, -1, -1):
    inv_facts[i] = inv_facts[i + 1] * (i + 1) % MOD


def c_mod(n: int, m: int) -> int:
    """Calculates C(n, m) % MOD.
    C(n, m) = n! // m! // (n-m)!
    """
    return facts[n] * inv_facts[m] * inv_facts[n-m] % MOD


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return m * bi_power_mod(m - 1, n - k - 1) * c_mod(n - 1, k) % MOD
