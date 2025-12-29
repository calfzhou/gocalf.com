---
title: 338. Counting Bits
notebook: coding
tags:
- easy
date: 2024-11-22 20:04:18
updated: 2024-11-22 20:04:18
---
## Problem

Given an integer `n`, return _an array_ `ans` _of length_ `n + 1` _such that for each_ `i` (`0 <= i <= n`)_,_ `ans[i]` _is the **number of**_ `1`_**'s** in the binary representation of_ `i`.

<https://leetcode.com/problems/counting-bits/>

**Example 1:**

> Input: `n = 2`
> Output: `[0,1,1]`
> Explanation:
>
> ```text
> 0 --> 0
> 1 --> 1
> 2 --> 10
> ```

**Example 2:**

> Input: n = 5
> Output: [0,1,1,2,1,2]
> Explanation:
>
> ```text
> 0 --> 0
> 1 --> 1
> 2 --> 10
> 3 --> 11
> 4 --> 100
> 5 --> 101
> ```

**Constraints:**

- `0 <= n <= 10⁵`

**Follow up:**

- It is very easy to come up with a solution with a runtime of `O(n log n)`. Can you do it in linear time `O(n)` and possibly in a single pass?
- Can you do it without using any built-in function (i.e., like `__builtin_popcount` in C++)?

## Test Cases

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
```

{% asset_code coding/338-counting-bits/solution_test.py %}

## Thoughts

计算一个整数 n 的二进制中 `1` 的个数，就循环右移直到数字降为 0，过程中记录最低位是 `1` 的次数，时间为 `O(log n)`。

对所有从 0 到 n 的整数都算一次，总时间是 `O(n log n)`。

## Code

{% asset_code coding/338-counting-bits/solution.py %}

## Follow Up - O(n)

连续计算的时候，可以利用已有的结果加速。

一个思路是看当从 `n - 1` 变到 n 时，减少了几个 `1`，增加了几个 `1`。

比如 `n = 0b1001000`，那么 `n - 1 = 0b1000111`。二者二进制位没有变化的部分可以用 bit-and 计算，即 `common = n & (n-1) = 0b1000000`。

用 `common` 分别与两个数计算 bit-xor，结果就是变化的部分。

如 `xor(common, n-1) = 0b111`，这些 `1` 都被去掉了。`xor(common, n) = 0b1000`，这些 `1` 是新加入的。

令 `f(n)` 表示整数 n 的二进制中 `1` 的个数，那么：

`f(n) = f(n-1) - f(xor(common, n-1)) + f(xor(common, n))`。

一般 `xor(common, n-1)` 和 `xor(common, n)` 都小于 n。唯独当 n 是 2 的幂时，`xor(common, n)` 等于 n，可以对这个情况做特判，`f(2ⁱ) = 1`。

这样对于每个数，都只需要常数时间进行计算和查表，总时间是 `O(n)`。

{% asset_code coding/338-counting-bits/solution2.py %}

## Faster O(n)

上边的方法还是太繁琐（且慢），而且「n 是 2 的幂」这种特例容易被忽略而造成 bug。

实际上对于一个 d 位的二进制数 n，最高位是 `1`，剩下的 `d - 1` 位构成了 `m = n - 2ᵈ⁻¹`，显然 `0 <= m < n`。如果 m 中 `1` 的个数已知，那么显然 `f(n) = 1 + f(m)`。

只剩下一个问题就是常数时间确定 d，或者 `P = 2ᵈ⁻¹`。在遍历整数的过程中，很容易跟踪 P 的变化。初始 `P = n = 1`，当 n 递增到 `P * 2` 时，就可以更新 `P = P * 2`。

总的时间复杂度也是 `O(n)`，但系数要小得多。

{% asset_code coding/338-counting-bits/solution3.py %}

三种算法的实际运行时间对比：

```text
[1:n log n] n =     10:      4.994 μs
[2: linear] n =     10:      2.907 μs
[3: linear] n =     10:      1.752 μs

[1:n log n] n =    100:     83.195 μs
[2: linear] n =    100:     27.409 μs
[3: linear] n =    100:     10.770 μs

[1:n log n] n =   1000:   1223.218 μs
[2: linear] n =   1000:    280.717 μs
[3: linear] n =   1000:    109.602 μs

[1:n log n] n =  10000:  16359.447 μs
[2: linear] n =  10000:   2837.669 μs
[3: linear] n =  10000:   1194.283 μs

[1:n log n] n = 100000: 209923.616 μs
[2: linear] n = 100000:  28099.642 μs
[3: linear] n = 100000:  12005.032 μs
```
