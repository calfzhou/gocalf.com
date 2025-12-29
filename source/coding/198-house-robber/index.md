---
title: 198. House Robber
notebook: coding
tags:
- medium
date: 2024-11-20 17:39:05
updated: 2024-11-20 17:42:44
katex: true
---
## Problem

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return _the maximum amount of money you can rob tonight **without alerting the police**_.

<https://leetcode.com/problems/house-robber/>

**Example 1:**

> Input: `nums = [1,2,3,1]`
> Output: `4`
> Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
> Total amount you can rob = 1 + 3 = 4.

**Example 2:**

> Input: `nums = [2,7,9,3,1]`
> Output: `12`
> Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
> Total amount you can rob = 2 + 9 + 1 = 12.

**Constraints:**

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## Test Cases

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
```

{% asset_code coding/198-house-robber/solution_test.py %}

## Thoughts

动态规划问题关键在于 dp 函数的定义，不同的定义会得到不同的递推公式，理解或计算的复杂程度（甚至可行性）也会随之不同。

不妨设 `t[i]` 表示从前 `i + 1` 个房间（即 `0, 1, 2, ..., i`）能抢到的最多的金额（注意房间 i 可能抢也可能不抢）。

显然 `t[0] = nums[0]`，即只有一家的时候，肯定要抢。

然后 `t[1] = max{nums[0], nums[1]}`，即有两家的话抢金额大的那家。根据 `t` 的定义还可以得出 `t[1] = max{t[0], 0 + nums[1]}`，表示要么不抢房间 1，直接拿走已经抢到的金额（即 `t[0]`），要么抢房间 1，但必须放弃房间 0。

对于 `i > 1`，有两个选择。一个是抢房间 i，这就必须放弃房间 `i - 1`，总金额是 `t[i-2] + nums[i]`。另一个是不抢房间 i，那么总金额维持在 `t[i-1]`。两个选择下取总金额最大的那个记录为 `t[i]`。

所以 `t[i] = max{t[i-1], t[i-2] + nums[i]}`。

需要注意的是 `t[i-1]` 或 `t[i-2]` 并不意味房间 `i - 1` 或 `i - 2` 一定要抢。这导致并不是一定要每隔一个房间就抢一个房间，有可能会连续跳过两个房间（很容易有个错误想法是要么抢所有奇数房间，要么抢所有偶数房间）。

假设 `t[i-2]` 对应的选择是不抢房间 `i - 2`，必然有 `t[i-2] = t[i-3]`，那么 `t[i-1] = max{t[i-2], t[i-3] + nums[i-1]} = t[i-2] + nums[i-1]`，如果 `nums[i-1] < nums[i]` 就也会放弃房间 `i - 1`，即连续放弃 `i - 2` 和 `i - 1` 两个房间。

比如 `nums = [2, 7, 9, 3, 1, 2]`，当 `i = 5` 时可知 `t[2] = t[3] = 11`，而 `nums[4] < nums[5]`，导致房间 3 和 4 被连续放弃。

$$
\begin{array}{c:ccccc}
\small rob & \blacktriangledown & & \blacktriangledown & & & \blacktriangledown \\
\small nums & 2 & 7 & 9 & 3 & 1 & 2 \\
\hline
\small i & \tiny 0 & \tiny 1 & \tiny 2 & \tiny 3 & \tiny 4 & \tiny 5 \\
\small t[i-1] & \tiny / & \tiny\cancel 2 & \tiny\cancel 7 & \tiny 11 & \tiny\cancel{11} & \tiny\cancel{12} \\
\small t[i-2]+nums[i] & \tiny 2 & \tiny 7 & \tiny 11 & \tiny\cancel{10} & \tiny 12 & \tiny 13
\end{array}
$$

时间复杂度 `O(n)`，空间复杂度 `O(n)`。实际上 `t` 只需要保留最新的两个值，也可以直接复用 `nums` 的空间，空间复杂度降为 `O(1)`。

## Code

{% asset_code coding/198-house-robber/solution.py %}

## Another DP

另外一个思路是定义 `t'[i]` 为「走到房间 i 时，如果抢房间 i，最大可得金额」。跟上边的区别是，使用 `t'[i]` 就意味着一定要抢房间 i。

显然 `t'[0] = nums[0]`，`t'[1] = nums[1]`，`t'[2] = nums[0] + nums[2]`。注意 t 不再是递增序列，这里除了一定有 `t'[0] <= t'[2]` 外，`t'[0]` 与 `t'[1]` 的大小关系不确定，`t'[1]` 与 `t'[2]` 的大小关系也不确定。

计算 `t'[i]` 时，因为房间 i 一定要抢，所以需要放弃房间 `i - 1`，可以在抢了房间 `i - 2` 的基础上再抢房间 i，得到 `t'[i-2] + nums[i]`。但是 `t'[i-2]` 和 `t'[i-3]` 的大小关系不确定，就还得看 `t'[i-3] + nums[i]`（即抢房间 `i - 3`，跳过 `i - 2` 和 `i - 1`）会不会更大。

所以 `t'[i] = nums[i] + max{t'[i-2], t'[i-3]}`。

最终的结果，需要从 `t'[n-1]` 和 `t'[n-2]` 中取较大的（分别对应与抢和不抢最后一个房间）。

比如上边例子 `nums = [2, 7, 9, 3, 1, 2]`，按 `t'` 计算的过程为：

$$
\begin{array}{c:ccccc}
\small rob & \blacktriangledown & & \blacktriangledown & & & \blacktriangledown \\
\small nums & 2 & 7 & 9 & 3 & 1 & 2 \\
\hline
\small i & \tiny 0 & \tiny 1 & \tiny 2 & \tiny 3 & \tiny 4 & \tiny 5 \\
\small t'[i-2]+nums[i] & \tiny 2 & \tiny 7 & \tiny 11 & \tiny 10 & \tiny 12 & \tiny\cancel{12} \\
\small t'[i-3]+nums[i] & \tiny 2 & \tiny 7 & \tiny\cancel{9} & \tiny\cancel{5} & \tiny\cancel{8} & \tiny 13 \\
\end{array}
$$

{% asset_code coding/198-house-robber/solution2.py %}

整体上 `t[i]` 的逻辑和处理都更简单直接，但思考过程中总是会不自觉地绕到 `t'[i]` 上。主要可能是因为 `t[i]` 不明确房间是抢还是不抢，这种不明确性在思考的时候总会想要避免。
