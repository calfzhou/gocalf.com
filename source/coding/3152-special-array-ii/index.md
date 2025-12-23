---
title: 3152. Special Array II
notebook: coding
tags:
- medium
katex: true
date: 2024-12-09 10:27:47
updated: 2024-12-09 10:27:47
---
## Problem

An array is considered **special** if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer `nums` and a 2D integer matrix `queries`, where for `queries[i] = [fromᵢ, toᵢ]` your task is to check that subarray `nums[fromᵢ..toᵢ]` is **special** or not.

> A **subarray** is a contiguous sequence of elements within an array.

Return an array of booleans `answer` such that `answer[i]` is `true` if `nums[fromᵢ..toᵢ]` is special.

<https://leetcode.com/problems/special-array-ii/>

**Example 1:**

> Input: `nums = [3,4,1,2,6], queries = [[0,4]]`
> Output: `[false]`
> Explanation:
> The subarray is `[3,4,1,2,6]`. 2 and 6 are both even.

**Example 2:**

> Input: `nums = [4,3,1,6], queries = [[0,2],[2,3]]`
> Output: `[false,true]`
> Explanation:
>
> 1. The subarray is `[4,3,1]`. 3 and 1 are both odd. So the answer to this query is false.
> 2. The subarray is `[1,6]`. There is only one pair: `(1,6)` and it contains numbers with different parity. So the answer to this query is true.

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁵`
- `1 <= queries.length <= 10⁵`
- `queries[i].length == 2`
- `0 <= queries[i][0] <= queries[i][1] <= nums.length - 1`

## Test Cases

``` python
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
```

{% asset_code coding/assets/3152-special-array-ii/solution_test.py %}

## Thoughts

[3151. Special Array I](3151-special-array-i) 的进阶版，从一次查询增加成 q 次查询。

> 跟 [3258. Count Substrings That Satisfy K-Constraint I](3258-count-substrings-that-satisfy-k-constraint-i) 到 [3261. Count Substrings That Satisfy K-Constraint II](3261-count-substrings-that-satisfy-k-constraint-ii) 进阶类似。

直接算是 `O(n²)` 时间，因为不同的 query 之间可能有大量重复的判定。这种情况很适合动态规划。

令 `dp(i)` 表示以 `nums[i]` 为终点的最长连续奇偶交替的 subarray 长度。显然：

$$
\begin{cases}
  dp(0) & =1 \\
  dp(i) & =\begin{cases}
    1 & \text{if }nums[i]\equiv nums[i-1]\pmod{2} \\
    dp(i-1)+1 & \text{otherwise}
  \end{cases}
\end{cases}
$$

这样对于任意 query `(from, to)`，比较 query 区间的长度 `to - from + 1` 和 `dp(to)` 的大小，如果前者 **小于等于** 后者（`to - from + 1 <= dp(to)` ⟺ `from > to - dp(to)`）则为 `true`，否则是 `false`。

时间复杂度 `O(n)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/assets/3152-special-array-ii/solution.py %}
