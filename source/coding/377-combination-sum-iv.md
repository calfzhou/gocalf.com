---
title: 377. Combination Sum IV
notebook: coding
tags:
- medium
date: 2024-11-24 20:52:25
updated: 2024-11-24 20:52:25
katex: true
---
## Problem

Given an array of **distinct** integers `nums` and a target integer `target`, return _the number of possible combinations that add up to_ `target`.

The test cases are generated so that the answer can fit in a **32-bit** integer.

<https://leetcode.com/problems/combination-sum-iv/>

**Example 1:**

> Input: `nums = [1,2,3], target = 4`
> Output: `7`
> Explanation:
> The possible combination ways are:
> `(1, 1, 1, 1)`
> `(1, 1, 2)`
> `(1, 2, 1)`
> `(1, 3)`
> `(2, 1, 1)`
> `(2, 2)`
> `(3, 1)`
> Note that different sequences are counted as different combinations.

**Example 2:**

> Input: `nums = [9], target = 3`
> Output: `0`

**Constraints:**

- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 1000`
- All the elements of `nums` are **unique**.
- `1 <= target <= 1000`

**Follow up:** What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?

## Test Cases

``` python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
```

{% asset_code coding/377-combination-sum-iv/solution_test.py %}

## Thoughts

相当于 [322. Coin Change](/coding/322-coin-change) 的进阶版，从找到最少的硬币数量，改为找出所有可能的方案总数。

对于一个整数 t，记能组合出 t 的方法总数为 `cw(t)`。显然有：

$$
cw(t)=\begin{cases}
  1 & \text{if }t=0 \\
  0 & \text{if }0<t<\min\{nums\} \\
  \sum_i\{cw(a-nums[i])\mid nums[i]\le t\} & \text{otherwise} \\
\end{cases}
$$

跟 [problem 322](/coding/322-coin-change) 几乎一模一样，只是把初始值 `1` 改成 `0`，无解值 $\infty$ 改成 `0`，`1 + min` 改成 `sum`。

代码也直接照搬过来改一下。

时间复杂度是 `O(target * n)`，空间复杂度是 `O(target)`。

## Code

{% asset_code coding/377-combination-sum-iv/solution.py %}
