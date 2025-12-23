---
title: 3266. Final Array State After K Multiplication Operations II
notebook: coding
tags:
- hard
katex: true
date: 2024-12-14 00:56:32
updated: 2024-12-14 00:56:32
---
## Problem

You are given an integer array `nums`, an integer `k`, and an integer `multiplier`.

You need to perform `k` operations on `nums`. In each operation:

- Find the **minimum** value `x` in `nums`. If there are multiple occurrences of the minimum value, select the one that appears **first**.
- Replace the selected minimum value `x` with `x * multiplier`.

After the `k` operations, apply **modulo** `10⁹ + 7` to every value in `nums`.

Return an integer array denoting the _final state_ of `nums` after performing all `k` operations and then applying the modulo.

<https://leetcode.cn/problems/final-array-state-after-k-multiplication-operations-ii/>

**Example 1:**

> Input: `nums = [2,1,3,5,6], k = 5, multiplier = 2`
> Output: `[8,4,6,5,6]`
> Explanation:
>
> | Operation         | Result            |
> |-------------------|-------------------|
> | After operation 1 | `[2, 2, 3, 5, 6]` |
> | After operation 2 | `[4, 2, 3, 5, 6]` |
> | After operation 3 | `[4, 4, 3, 5, 6]` |
> | After operation 4 | `[4, 4, 6, 5, 6]` |
> | After operation 5 | `[8, 4, 6, 5, 6]` |

**Example 2:**

> Input: `nums = [100000,2000], k = 2, multiplier = 1000000`
> Output: `[999999307,999999993]`
> Explanation:
>
> | Operation             | Result                       |
> |-----------------------|------------------------------|
> | After operation 1     | `[100000, 2000000000]`       |
> | After operation 2     | `[100000000000, 2000000000]` |
> | After applying modulo | `[999999307, 999999993]`     |

**Constraints:**

- `1 <= nums.length <= 10⁴`
- `1 <= nums[i] <= 10⁹`
- `1 <= k <= 10⁹`
- `1 <= multiplier <= 10⁶`

## Test Cases

``` python
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
```

{% asset_code coding/3266-final-array-state-after-k-multiplication-operations-ii/solution_test.py %}

## Thoughts

> 这可能是提交遇到解答错误次数最多的一题了。

[3264. Final Array State After K Multiplication Operations I](../3264-final-array-state-after-k-multiplication-operations-i/index.md) 的进阶版。不只是 `n = nums.length` 从 100 提升到 10⁴，k 也从 10 提升到了 10⁹。

### Huge "k"

先看变得更大的 k，从 1 遍历到 k 肯定是跑不动的。但这个跟 [1760. Minimum Limit of Balls in a Bag](../1760-minimum-limit-of-balls-in-a-bag/index.md) 非常像（指最大堆的那种实现方式，而非二分法），巨大的 k 其实会给每个数字都平摊很多，可以先计算出每个数字平摊多少，直接乘上去，可以省掉大量的循环。

设 `nums` 中的最大值为 `top`。先把所有其他数字通过乘以 `multiplier` 的某个次方，增大到不超过 `top`，即修改之后的数组满足：对于任意的 i，`nums[i] <= top < nums[i] * multiplier`。设某个数字是 v，那么 `p = ⌊log(top / v, multiplier)⌋`，让 v 乘以 `multiplier` 的 p 次方即可。

> 这里有个坑，在 Python 里直接计算 `log(a, b)` 结果可能会有些偏差，导致下取整会少 1。比如 `log(3**17, 3) = 16.999999999999996`，比如 `log10(5**7) / log10(5) = 6.999999999999999`。即使用 [decimal](https://docs.python.org/3/library/decimal.html) 也同样会遇到 bad case。目前的处理方法是计算完之后根据情况修正一下：
>
> ``` python
> def ilog(a: int, b: int) -> int:
>     """Calculates int(log(a, b))."""
>     p = int(log10(a) / log10(b))
>     if b ** (p + 1) <= a:
>         p += 1
>     return p
> ```

可以发现这个状态下，每连续 n 次操作就刚好给 `nums` 中每个数字都乘以 `multiplier` 一次。设前边为了达到这个状态需要 t 次操作，那么 `(k - t) // n` 就是每个数字平摊到的操作次数。不妨设 `divmod(k - t, n) = q, r`。

先看剩下的零头 r（`0 ≤ r < n`）。只需要对目前 `nums` 中最小的 r 个数字，分别乘以 `multiplier` 一次即可。可以用大小为 r 的最大堆找出最小的 r 个数字，时间为 `n log r = O(n log n)`。

> 需要注意取模之后再比较大小就没意义了，所以在确定好最小的 r 个数字之前，不要取模。因为 `nums` 中所有值都不超过 `top`，也就不需要取模。

然后给 `nums` 中每个数字都乘以 `multiplier` 的 q 次方。注意到这里的 q 依然非常大，需要使用二分法进行幂运算，时间复杂度可以降到 `O(log q) = O(log k - log n) ≈ O(log k)`。

二分法幂运算在 [935. Knight Dialer](../935-knight-dialer/index.md) 和 [70. Climbing Stairs](../70-climbing-stairs/index.md) 都有涉及（矩阵的幂运算跟整数的幂运算没有本质区别）。在这两题中计算幂用的是正向的循环，如：

``` python
MOD = 1_000_000_007

def bi_power(a: int, n: int) -> int:
    """Calculates x ** n % MOD."""
    if n == 0: return 1
    mask = 1
    n1 = n
    while n1 := n1 >> 1:
        mask <<= 1
    res = a
    while mask := mask >> 1:
        res = res * res % MOD
        if n & mask:
            res = res * a % MOD
    return res
```

还有另外一种计算方式，本题用的是这种方式：

``` python
MOD = 1_000_000_007

def bi_power(a: int, n: int) -> int:
    """Calculates x ** n % MOD."""
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % MOD
        n >>= 1
        a = a * a % MOD

    return res
```

至此就计算完成了，把当前的 `nums` 返回即可。时间复杂度 `O((n log n) + (log k))`，空间复杂度 `O(n)`。

### Normal "k"

上边的处理的基础是 k 足够大，足够把 `nums` 所有数字都增大到刚好不超过 `top`。但如果 k 没有那么大，就还是按照 [3264. Final Array State After K Multiplication Operations I](../3264-final-array-state-after-k-multiplication-operations-i/index.md) 中那样，用最小堆来处理。

时间复杂度 `O((n + k) log n)`，空间复杂度 `O(n)`。

一个小的优化是类似 [1760. Minimum Limit of Balls in a Bag](../1760-minimum-limit-of-balls-in-a-bag/index.md) 里的处理，取当前最小值 a，看第二小的值 b，直接对 a 操作若干次使它刚好超过 b。令 `p = ⌈log(b + 1 - a, multiplier)⌉`，如果剩余的次数足够，那就给 a 加上 `multiplier` 的 p 次方，再放回堆中。

注意需要保证对于相同的两个数，要优先对在 `nums` 中排在前边的数字操作。所以如果 b 的下标小于 a 的下标，就令 `p = ⌈log(b - a), multiplier⌉`，确保 a 不会超过 b。

另外考虑到 Python 的 log 浮点误差问题，虽然没有实际遇到 log 结果上取整有错，但保险起见还是可以特殊处理一下：

``` python
def clog(a: int, b: int) -> int:
    """Calculates ceil(log(a, b))."""
    p = ceil(log10(a) / log10(b))
    if b ** (p - 1) > a:
        p -= 1
    return p
```

另外注意取模之后再排序就无效了，所以运算过程中不能取模。但进入这个处理逻辑的前提是 k 不够把 `nums` 所有数字都增大到刚好不超过 `top`，也就不用取模。

## Code

{% asset_code coding/3266-final-array-state-after-k-multiplication-operations-ii/solution.py %}
