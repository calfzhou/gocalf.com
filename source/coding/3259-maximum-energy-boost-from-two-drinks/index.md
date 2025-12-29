---
title: 3259. Maximum Energy Boost From Two Drinks
notebook: coding
tags:
- medium
date: 2024-11-26 22:54:49
updated: 2024-11-26 22:54:49
katex: true
---
## Problem

You are given two integer arrays `energyDrinkA` and `energyDrinkB` of the same length `n` by a futuristic sports scientist. These arrays represent the energy boosts per hour provided by two different energy drinks, A and B, respectively.

You want to _maximize_ your total energy boost by drinking one energy drink _per hour_. However, if you want to switch from consuming one energy drink to the other, you need to wait for _one hour_ to cleanse your system (meaning you won't get any energy boost in that hour).

Return the **maximum** total energy boost you can gain in the next `n` hours.

**Note** that you can start consuming _either_ of the two energy drinks.

<https://leetcode.cn/problems/maximum-energy-boost-from-two-drinks/>

**Example 1:**

> Input: `energyDrinkA = [1,3,1], energyDrinkB = [3,1,1]`
> Output: `5`
> Explanation:
> To gain an energy boost of `5`, drink only the energy drink A (or only B).

**Example 2:**

> Input: `energyDrinkA = [4,1,1], energyDrinkB = [1,1,3]`
> Output: `7`
> Explanation:
> To gain an energy boost of `7`:
> Drink the energy drink A for the first hour.
> Switch to the energy drink B and we lose the energy boost of the second hour.
> Gain the energy boost of the drink B in the third hour.

**Constraints:**

- `n == energyDrinkA.length == energyDrinkB.length`
- `3 <= n <= 10⁵`
- `1 <= energyDrinkA[i], energyDrinkB[i] <= 10⁵`

## Test Cases

```python
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
```

{% asset_code coding/3259-maximum-energy-boost-from-two-drinks/solution_test.py %}

## Thoughts

由于存在切换饮料时的惩罚项，很容易发现子问题的最优解不一定包含在整个问题的最优解中。

记 `ma(i)` 是第 i 个小时喝 A 饮料的情况下，能获得的最大能量；`mb(i)` 是第 i 个小时喝 B 饮料的情况下，能获得的最大能量。显然问题的答案是 `max{ma(n), mb(n)}`。

如果第 i 个小时喝 A 饮料，那么要么是 `i - 1` 小时的时候也喝 A，要么是 `i - 2` 小时的时候喝 B 然后空一个小时。可得：

$$
ma(i)=\begin{cases}
  energyDrinkA(0) & \text{if }i=0 \\
  ma(i-1)+energyDrinkA(i) & \text{if }i=1 \\
  \max\{ma(i-1),mb(i-2)\}+energyDrinkA(i) & \text{if }i>2
\end{cases}
$$

同理可得：

$$
mb(i)=\begin{cases}
  energyDrinkB(0) & \text{if }i=0 \\
  mb(i-1)+energyDrinkB(i) & \text{if }i=1 \\
  \max\{mb(i-1),ma(i-2)\}+energyDrinkB(i) & \text{if }i>2
\end{cases}
$$

时间和空间复杂度都是 `O(n)`。

## Code

{% asset_code coding/3259-maximum-energy-boost-from-two-drinks/solution.py %}
