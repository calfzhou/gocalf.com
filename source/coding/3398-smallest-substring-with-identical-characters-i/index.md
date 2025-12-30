---
title: 3398. Smallest Substring With Identical Characters I
notebook: coding
tags:
- hard
katex: true
date: 2025-01-04 15:28:44
updated: 2025-01-04 16:05:25
---
## Problem

You are given a binary string `s` of length `n` and an integer `numOps`.

You are allowed to perform the following operation on `s` **at most** `numOps` times:

- Select any index `i` (where `0 <= i < n`) and **flip** `s[i]`. If `s[i] == '1'`, change `s[i]` to `'0'` and vice versa.

You need to **minimize** the length of the **longest** substring of `s` such that all the characters in the substring are **identical**.

> A **substring** is a contiguous **non-empty** sequence of characters within a string.

Return the **minimum** length after the operations.

<https://leetcode.com/problems/smallest-substring-with-identical-characters-i/>

**Example 1:**

> Input: `s = "000001", numOps = 1`
> Output: `2`
> Explanation:
> By changing `s[2]` to `'1'`, s becomes `"001001"`. The longest substrings with identical characters are `s[0..1]` and `s[3..4]`.

**Example 2:**

> Input: `s = "0000", numOps = 2`
> Output: `1`
> Explanation:
> By changing `s[0]` and `s[2]` to `'1'`, s becomes `"1010"`.

**Example 3:**

> Input: `s = "0101", numOps = 0`
> Output: `1`

**Constraints:**

- `1 <= n == s.length <= 1000`
- `s` consists only of `'0'` and `'1'`.
- `0 <= numOps <= n`

## Test Cases

```python
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
```

{% asset_code solution_test.py %}

## Thoughts

本题跟 [3264. Final Array State After K Multiplication Operations I](../3264-final-array-state-after-k-multiplication-operations-i/index.md) 几乎一样。唯一的区别是 [problem 3264](../3264-final-array-state-after-k-multiplication-operations-i/index.md) 是把 m 个球分 k 次得到 `k + 1` 堆，每堆的球数累加即为 m；本题相当于在 m 个排成一排的球中选 k 个拿掉从而得到 `k + 1` 堆，每堆的球数累加还要再加上 k 才等于 m。

按照相同的思路来处理。

首先如果有连续 m 个 `'0'`（`'1'` 也类似），从其中选 k 个改成 `'1'`，那么剩下的最大连续 `'0'` 的个数的最小值为 $\lceil\frac{m-k}{k+1}\rceil$（即尽可能平均分）。

反过来，如果希望剩下的最大连续 `'0'` 的个数为 a，则需要把至少 $k = \lceil\frac{m-a}{a+1}\rceil$ 个 `'0'` 改为 `'1'`。

但这里有个边界刺客就是当 `m = 2` 的时候，改变任何一个 `'0'` 都会再跟这一段两边原本的 `'1'` 连续起来，而改左边的 `'0'` 还是右边的 `'0'` 会导致最终需要的操作次数不一样。

幸运地是如果最大的 m 是 2，想要进一步降低就只能是全都降为 1，也就是把整个 s 改成 `'0'`、`'1'` 交替的字符串。这时候结果字符串只有两种可能，要么是 `"010101..."`，要么是 `"101010..."`，而且这两个还是互补的。只需要拿 s 跟其中一个（比如 `"010101..."`）逐位比较（跟 [782. Transform to Chessboard](../782-transform-to-chessboard/index.md) 类似），如果有 k 个位置的数不一样，那么最少的操作次数就是 `min{k, n - k}`，如果 `numOps` 足够的话，最终结果就是 1。

如果 `numOps` 不足以把 s 改成完全 `'0'`、`'1'` 交替的字符串，那么就用模拟的方法，每次选最长连续段，用若干次操作把它打散，这样不断操作，看操作次数用尽的时候，剩下的最长连续段的长度就是结果（显然结果一定大于等于 2）。

扫描一遍 s，把所有连续段落的长度放入最大堆。显然只需要放长度大于 2 的那些。又显然如果没有长度大于 2 的连续段落，最终结果就是 2。

每次取当前最大的连续段落长度记为 a，取第二大的记为 b，令 `b' = max{2, b - 1}`，对 a 做 $\lceil\frac{a-b'}{b'+1}\rceil$ 次操作就可以得到比 b 小值 `a'`（`a' ≤ b'`）。把 `a'` 放回堆中，此时堆里最大值就是 b，继续做同样的操作，直到次数用尽，或者堆顶的值小于等于 2。

> 跟 [problem 3264](../3264-final-array-state-after-k-multiplication-operations-i/index.md) 类似，如果堆顶的 a 是由原本的 m 做了 k1 次操作得到的，就不能直接对 a 操作，而是把 k1 次操作退回去，重新对 m 做 $\lceil\frac{m-b'}{b'+1}\rceil$ 次操作。
>
> 另外需要注意，最后堆顶的值可能是 1，这时候并不意味着结果就是 1（实际上是 2），因为前边提到了，初始化的时候，所有长度为 2 的段落全都没有放进来。

一个小优化是如果有很多个相同的 m 值，并不用全都加到堆里对每一个都算一次，可以直接在堆里同时放上相同值的个数（如 cnt）。如果把 m 降到 b 需要 k 次操作，那么 cnt 个 m 就一共需要 `k * cnt` 次操作。唯一需要注意的是，如果剩余的操作次数（如 `numOps`）比 `k * cnt` 小，就得特殊处理一下了。记 `k, r = divmod(numOps, cnt)`，那么可以对 r 个 m 做 `k + 1` 次操作，对剩下的 `cnt - r` 个 m 做 k 次操作（产生了裂变，但这次裂变之后循环也就结束了）。

最坏时间复杂度 `O(n log n)`，但平均情况远小于此。空间复杂度 `O(n)`。提交之后 runtime 只用了 3 ms，远低于一般的几十到几千 ms。

## Code

{% asset_code solution.py %}

## 二分法

另外 [problem 3264](../3264-final-array-state-after-k-multiplication-operations-i/index.md) 后边还提到了 [二分的处理方法](../1760-minimum-limit-of-balls-in-a-bag/index.md#二分法) ，显然因为本题跟它几乎一致，也是可以套用一样的二分法。

前置的处理逻辑是一样的，先判断 `numOps` 是否足够把 s 改成完全 '0'、'1' 交替的字符串，可以的话就直接返回 1。

然后也是扫描 s，记录所有连续段落的长度，同样可以忽略掉长度为 2 的那些，而且可以把相同长度的段落视为同样的，只保留长度和个数。

二分法实际上是要尝试不同的结果值，看哪一个刚好能够在 `numOps` 次操作下可以实现。显然下界 l 就是 2，而上界 r 就是扫描 s 得到的初始时最大的连续段落长度（显然小于等于 n）。

每次取 l 和 r 的中间值 mid，看 `numOps` 次操作是否足够。对所有长度超过 mid 的连续段落执行操作，如果该段落长度为 m，则需要操作 $\lceil\frac{m-mid}{mid+1}\rceil$ 次；如果有 cnt 个长度为 m 的段落，再乘以 cnt 即可。

可以事先对所有的段落长度数组排序，就可以用二分法快速找到大于 mid 的起点位置，遍历右半个数组即可。

时间复杂度也是 `O(n log n)`，实际跑下来速度跟上边最大堆方法差不多。

{% asset_code solution2.py %}
