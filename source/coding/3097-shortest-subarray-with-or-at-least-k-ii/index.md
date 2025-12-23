---
title: 3097. Shortest Subarray With OR at Least K II
notebook: coding
tags:
- medium
date: 2025-01-17 18:58:21
updated: 2025-01-17 18:58:21
---
## Problem

跟 [3095. Shortest Subarray With OR at Least K I](../3095-shortest-subarray-with-or-at-least-k-i/index.md) 一模一样，只是问题规模更大。

<https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/>

**Constraints:**

- `1 <= nums.length <= 2 * 10⁵`
- `0 <= nums[i] <= 10⁹`
- `0 <= k <= 10⁹`

## Test Cases

``` python
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
```

{% asset_code coding/3097-shortest-subarray-with-or-at-least-k-ii/solution_test.py %}

## Thoughts

直接用 [3095. Shortest Subarray With OR at Least K I](../3095-shortest-subarray-with-or-at-least-k-i/index.md) 的代码，速度不是很快（时间复杂度 `O(n log k)`），考虑如何优化。

主要在于本题 k 的量级非常大，`log k` 带来的影响非常可观。

关键还是窗口左边界 l 的右移速度如何提升。

开始的时候 `l = 0`，r 逐渐右移，直接不断更新记录 `nums[l:r]` 各数字的 `OR` 的结果（依然记为 res），就跟 [problem 3095](../3095-shortest-subarray-with-or-at-least-k-i/index.md) 一样。但不用遍历每个数字的所有二进制位，不用记录 res 的每个二进制位的贡献量。每次右移 r 的时间复杂度为 `O(1)`。

如果能有一个辅助数组 dp，其中的值为 `dp[i] = nums[i] | nums[i+1] | ... | nums[r-1]`（`l ≤ i < r`），那么 `dp[l]` 就是 `nums[l:r]` 对应的 res，而 `dp[l+1]` 就是 `nums[l+1:r]` 对应的 res，这样右移 l 的时间就是 `O(1)`（直接让 l 自增即可）。

但是当再次右移 r 的时候，如果更新 dp 里所有相关的值，就变成 `O(n²)` 时间复杂度了，所以关键是右移 r 的时候不要动 dp。先记录下刚才的 r 值，比如记为 `r'`，那么 `dp[l:r']` 都被赋值了。从 `r'` 继续右移 r 的过程中，记录 `nums[r':r]` 各数字的 `OR` 值，记为 `res'`。这时候 `nums[l:r]` 各数字的 `OR` 值就等于 `dp[l] | res'`。可见右移 r 的时间复杂度依然是 `O(1)`。

dp 中只有区间 `[l, r')` 的值可用，当 l 右移到 `r'` 时，就需要在 dp 中填充区间 `[r', r)` 的那些值。

所以最坏情况下，l 和 r 都从 0 遍历到 n；dp 中一共计算 n 个值，每个值的计算时间为 `O(1)`。整体的时间复杂度 `O(n)`。空间复杂度 `O(n)`，但 dp 可以直接利用 nums 的空间，那么空间复杂度为 `O(1)`。

## Code

{% asset_code coding/3097-shortest-subarray-with-or-at-least-k-ii/solution.py %}
