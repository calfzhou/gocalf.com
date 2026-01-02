---
title: 1760. Minimum Limit of Balls in a Bag
notebook: coding
tags:
- medium
katex: true
date: 2024-12-07 20:55:03
updated: 2024-12-07 20:55:03
---
## Problem

You are given an integer array `nums` where the `iᵗʰ` bag contains `nums[i]` balls. You are also given an integer `maxOperations`.

You can perform the following operation at most `maxOperations` times:

- Take any bag of balls and divide it into two new bags with a **positive** number of balls.
  - For example, a bag of `5` balls can become two new bags of `1` and `4` balls, or two new bags of `2` and `3` balls.

Your penalty is the **maximum** number of balls in a bag. You want to **minimize** your penalty after the operations.

Return _the minimum possible penalty after performing the operations_.

<https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/>

**Example 1:**

> Input: `nums = [9], maxOperations = 2`
> Output: `3`
> Explanation:
>
> - Divide the bag with 9 balls into two bags of sizes 6 and 3. `[`{% u 9 %}`] -> [6,3]`.
> - Divide the bag with 6 balls into two bags of sizes 3 and 3. `[`{% u 6 %}`,3] -> [3,3,3]`.
>
> The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.

**Example 2:**

> Input: `nums = [2,4,8,2], maxOperations = 4`
> Output: `2`
> Explanation:
>
> - Divide the bag with 8 balls into two bags of sizes 4 and 4. `[2,4,`{% u 8 %}`,2] -> [2,4,4,4,2]`.
> - Divide the bag with 4 balls into two bags of sizes 2 and 2. `[2,`{% u 4 %}`,4,4,2] -> [2,2,2,4,4,2]`.
> - Divide the bag with 4 balls into two bags of sizes 2 and 2. `[2,2,2,`{% u 4 %}`,4,2] -> [2,2,2,2,2,4,2]`.
> - Divide the bag with 4 balls into two bags of sizes 2 and 2. `[2,2,2,2,2,`{% u 4 %}`,2] -> [2,2,2,2,2,2,2,2]`.
>
> The bag with the most number of balls has 2 balls, so your penalty is 2, and you should return 2.

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `1 <= maxOperations, nums[i] <= 10⁹`

## Test Cases

```python
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
```

{% snippet solution_test.py %}

## Thoughts

首先对于 a 个球，按题目要求拆分 k 次，数量最大的那袋里的球数（即 penalty）最小值为 $\lceil\frac{a}{k+1}\rceil$。

反过来，如果希望 penalty 不超过 b，则至少要分 $\lceil\frac{a}{b}\rceil-1$ 次。

取 `nums` 中的最大值记为 a，取第二大的值记为 b，对 a 做 $\lceil\frac{a}{b-1}\rceil-1$ 次拆分可以得到比 b 小的 penalty。把 a 的新 penalty 值放回 `nums`。这时候 `nums` 中最大值为 b，再取此时的第二大，重复同样的操作，直到操作次数用尽，或者 `nums` 中的数都降为 1。

需要注意，如果某一次取到的最大值 a 本身就是从 `nums` 中某个原始的数字拆分后得到的，则不能直接对 a 做拆分，而是应该对原始的数字做拆分。占用的操作数量也做相应的更新。

用最大堆就很合适，从堆顶弹出（耗时 `O(log n)`）的是最大值，弹出后新的堆顶就是第二大。新的 penalty 放回到堆中，耗时 `O(log n)`。

时间复杂度是 `O(k log n)`（`k = maxOperations`），空间复杂度 `O(n)`。

结果超时了，因为题目中 k 的取值可以达到 `10⁹`，而 n 是 `10⁵`。

`nums` 所有数字的总和 `S = Σ{nums}`，如果对 S 做 k 次拆分，得到的 penalty 是 $t=\lceil\frac{S}{k+1}\rceil$。考虑先把 `nums` 中所有数字都拆分到 penalty 不超过 t，累计的拆分次数应该小于等于 k，剩余的拆分次数的量级估计在 `O(n)` 吧，然后再套用前边的方法把剩余的次数用尽。

这样时间复杂度大约为 `O(n log n)`（循环 `O(n)` 次，每次用 `O(log n)` 时间出堆和入堆）。实际提交之后，大约能跑到 `99.x%`。

## Code

{% snippet solution.py %}

## 二分法

发现其他人都在用二分法。作区间为从 0 到 `nums` 最大值，记区间中间值为 m，把 `nums` 中所有数字拆分到 penalty 不超过 m，看累计的拆分次数，如果超过 k，说明 m 太小了，就对右半个区间递归。否则说明 m 太大了，对左半个区间递归。

时间复杂度是 `O(n log max(nums))`。按题目给定的约束，`max(nums)` 跟 k 的量级可能相当，所以时间复杂度大约为 `O(n log k)`。难怪没有上边改进之后 `O(n log n)` 快。

不过二者可以结合一下，仍然用二分法，但调整一下初始区间范围。

上边提到的 $t=\lceil\frac{S}{k+1}\rceil$ 可以作为上界。实际上对于 n 较大而 k 较小的情况，`max(nums)` 可能比这个值还小，所以二者取最小作为上界。

另外 S 到 `nums` 相当于已经做了 `n - 1` 次拆分，如果这个拆分已经是最优的，那么跟给定的 k 次拆分合起来，相当于总共有 `n - 1 + k` 次拆分机会，那么下界就是 $\lceil\frac{a}{n-1+k+1}\rceil=\lceil\frac{a}{n+k}\rceil$。

时间复杂度应该小于 `O(n log n)`（循环 `log n` 次，每次用 `O(n)` 时间计算所有数字拆到目标值需要的次数），空间复杂度 `O(1)`。实际跑的时间跟上边差不多，略快一些些。

{% snippet solution2.py %}
