---
title: 494. Target Sum
notebook: coding
tags:
- medium
katex: true
date: 2024-12-26 15:06:49
updated: 2024-12-26 15:06:49
---
## Problem

You are given an integer array `nums` and an integer `target`.

You want to build an **expression** out of nums by adding one of the symbols `'+'` and `'-'` before each integer in nums and then concatenate all the integers.

- For example, if `nums = [2, 1]`, you can add a `'+'` before `2` and a `'-'` before `1` and concatenate them to build the expression `"+2-1"`.

Return the number of different **expressions** that you can build, which evaluates to `target`.

<https://leetcode.com/problems/target-sum/>

**Example 1:**

> Input: `nums = [1,1,1,1,1], target = 3`
> Output: `5`
> Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
> `-1 + 1 + 1 + 1 + 1 = 3`
> `+1 - 1 + 1 + 1 + 1 = 3`
> `+1 + 1 - 1 + 1 + 1 = 3`
> `+1 + 1 + 1 - 1 + 1 = 3`
> `+1 + 1 + 1 + 1 - 1 = 3`

**Example 2:**

> Input: `nums = [1], target = 1`
> Output: `1`

**Constraints:**

- `1 <= nums.length <= 20`
- `0 <= nums[i] <= 1000`
- `0 <= sum(nums[i]) <= 1000`
- `-1000 <= target <= 1000`

## Test Cases

``` python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
```

{% asset_code coding/assets/494-target-sum/solution_test.py %}

## Thoughts

首先如果 nums 的总和比 target 的绝对值小，那么所有数字都用正号或者都用负号都够不到 target，直接返回 0 即可。

然后考虑把负号抹掉。假设有一个式子，那么在等号两边同时加上 nums 中的所有数字，等号左边的每一项就变成 `2 * nums[i]` 或者 0，右边变成 `sum(nums) + target`。这就相当于对一个新的数组 `[2*nums[0], 2*nums[1], ..., 2*nums[n-1]]`，每一项可以选中或不选中，要使得选中的数字之和等于 `sum(nums) + target`。都除以 2 就等价于原始数字 nums 中任选若干个数字，其和要等于 `target' = (sum(nums) + target) / 2`。显然 `sum(nums) + target` 必须是个偶数，否则直接返回 0。

那么题目转变为，给定一个数组 nums，求从其中任选若干个数字能组合出 `target'` 的不同方案数量。

这时候题目就跟 [377. Combination Sum IV](377-combination-sum-iv) 非常像，只不过这里 nums 中的每个数字都最多只能使用一次。

因为限制了每个数字被使用的次数，动态规划的状态变量和状态转移就需要考虑这个因素。

令 `dp(i, t)`表示 nums 中前 i 个数字可以组合出 t 的方案数量。初值 `dp(i, 0) = 1`（一个都不选也是一种方案，对应到原问题就是所有数字前边都用负号）。题目的解为 `dp(n, target')`。

状态转移函数为（其中 `numsᵢ = nums[i - 1]`）：

$$
dp(i,t)=dp(i-1,t)+\begin{cases}
  0 & \text{for }t<nums_i \\
  dp(i-1,t-nums_i) & \text{for }t\ge nums_i
\end{cases}
$$

因为计算 i 的所有 dp 值时，只会用到 `i - 1` 相关的值，所以在遍历 i 的时候只需要缓存前一组 dp 值。另外对于确定的 i，任何 t 的 dp 值也只跟 `t - numsᵢ` 的 dp 有关，只需要从 `target'` 逆序计算到 `numsᵢ`，就可以 in-place 更新 dp 缓存，空间占用更少一些。

总的时间复杂度 `O(target'²)`，空间复杂度 `O(target')`。

## Code

{% asset_code coding/assets/494-target-sum/solution.py %}
