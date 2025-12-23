---
title: 2944. Minimum Number of Coins for Fruits
notebook: coding
tags:
- medium
katex: true
date: 2025-02-19 17:58:13
updated: 2025-02-19 17:58:13
---
## Problem

You are given an **0-indexed** integer array `prices` where `prices[i]` denotes the number of coins needed to purchase the `(i + 1)ᵗʰ` fruit.

The fruit market has the following reward for each fruit:

- If you purchase the `(i + 1)ᵗʰ` fruit at `prices[i]` coins, you can get any number of the next `i` fruits for free.

**Note** that even if you **can** take fruit `j` for free, you can still purchase it for `prices[j - 1]` coins to receive its reward.

Return the **minimum** number of coins needed to acquire all the fruits.

<https://leetcode.cn/problems/minimum-number-of-coins-for-fruits/>

**Example 1:**

> Input: `prices = [3,1,2]`
> Output: `4`
> Explanation:
>
> - Purchase the 1ˢᵗ fruit with `prices[0] = 3` coins, you are allowed to take the 2ⁿᵈ fruit for free.
> - Purchase the 2ⁿᵈ fruit with `prices[1] = 1` coin, you are allowed to take the 3ʳᵈ fruit for free.
> - Take the 3ʳᵈ fruit for free.
>
> Note that even though you could take the 2ⁿᵈ fruit for free as a reward of buying 1ˢᵗ fruit, you purchase it to receive its reward, which is more optimal.

**Example 2:**

> Input: `prices = [1,10,1,1]`
> Output: `2`
> Explanation:
>
> - Purchase the 1ˢᵗ fruit with `prices[0] = 1` coin, you are allowed to take the 2ⁿᵈ fruit for free.
> - Take the 2ⁿᵈ fruit for free.
> - Purchase the 3ʳᵈ fruit for `prices[2] = 1` coin, you are allowed to take the 4ᵗʰ fruit for free.
> - Take the 4ᵗʰ fruit for free.

**Example 3:**

> Input: `prices = [26,18,6,12,49,7,45,45]`
> Output: `39`
> Explanation:
>
> - Purchase the 1ˢᵗ fruit with `prices[0] = 26` coin, you are allowed to take the 2ⁿᵈ fruit for free.
> - Take the 2ⁿᵈ fruit for free.
> - Purchase the 3ʳᵈ fruit for `prices[2] = 6` coin, you are allowed to take the 4ᵗʰ, 5ᵗʰ and 6ᵗʰ (the next three) fruits for free.
> - Take the 4ᵗʰ fruit for free.
> - Take the 5ᵗʰ fruit for free.
> - Purchase the 6ᵗʰ fruit with `prices[5] = 7` coin, you are allowed to take the 8ᵗʰ and 9ᵗʰ fruit for free.
> - Take the 7ᵗʰ fruit for free.
> - Take the 8ᵗʰ fruit for free.
>
> Note that even though you could take the 6ᵗʰ fruit for free as a reward of buying 3ʳᵈ fruit, you purchase it to receive its reward, which is more optimal.

**Constraints:**

- `1 <= prices.length <= 1000`
- `1 <= prices[i] <= 10⁵`

## Test Cases

``` python
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
```

{% asset_code coding/assets/2944-minimum-number-of-coins-for-fruits/solution_test.py %}

## Thoughts

定义 `dp(i)` 表示购买第 `i + 1` 个水果并获得后续所有水果所需的最少 coins。所求结果即为 `dp(0)`。

因为购买了第 `i + 1` 个水果，可以免费获得第 `i + 2` 个到第 `2i + 2` 个水果（共 `i + 1` 个）。如果这 `i + 1` 个水果都直接免费获得，那么就必需买第 `2i + 3` 个水果，总花费为 `prices[i] + dp(2i + 2)`。也可以选择购买这 `i + 1` 个水果中的某个（设为第 `j + 1` 个，其中 `i + 1 ≤ j ≤ 2i + 1`），总花费为 `prices[i] + dp(j)`。

当然如果第 `i + 1` 个水果后边的水果个数不超过 `i + 1` 个，显然就不用再买了，全部免费获得即可，总花费为 `prices[i]`。

由此得到状态转移公式为：

$$
dp(i)=prices[i]+\begin{cases}
  0 & \text{if }2i+2\ge n \\
  \min_{i+1\le j\le 2i+2}\{dp(j)\} & \text{otherwise}
\end{cases}
$$

从 i 的最大值 `n - 1` 开始递减计算。

时间复杂度 `O(n²)`，空间复杂度 `O(n)`。

另外计算 `dp(i)` 的时候只需要 `prices[i]` 以及后边一些 dp 值，可以直接复用 prices 的空间，空间复杂度降为 `O(1)`。

再另外当 `2i + 2 ≥ n` 时，`dp(i) = prices[i]`，都不需要计算或处理，所以遍历的起点为 $\lceil\frac{n}{2}\rceil-2=\lfloor\frac{n-3}{2}\rfloor$。

## Code

{% asset_code coding/assets/2944-minimum-number-of-coins-for-fruits/solution.py %}

## Faster

从上边状态转移公式就很容易发现有大量的重复计算，比如：

- `dp(i) = prices[i] + min{dp(i+1), dp(i+2), ..., dp(2i), dp(2i+1), dp(2i+2)}`
- `dp(i-1) = prices[i-1] + min{dp(i), dp(i+1), dp(i+2), ..., dp(2i)}`

其中 `dp(i+1)` 到 `dp(2i)` 的最小值判定是重复的，看看怎么避免重复计算。

从 i 过渡到 `i - 1` 的时候，找最小值的区间的右边减少了两个（`2i + 2` 和 `2i + 1`），左边加入了一个（i）。关键在于当区间缩小的时候，如何快速获得新区间内的最小值。

考虑借助 [1475. Final Prices With a Special Discount in a Shop](1475-final-prices-with-a-special-discount-in-a-shop) 中提到的单调栈。

准备一个单调递增栈（栈里的数字是严格递增的），从右向左依次把每个 dp 值按单调栈的规则入栈，即如果比栈顶的值大则直接入栈，否则把所有小于等于它的值都弹出后再入栈。从 `dp(2i+2)` 到 `dp(i+1)` 都处理完，栈底就是这组数的最小值。利用此最小值计算出 `dp(i)` 后按同样的规则入栈，栈底是 `dp(i)` 到 `dp(2i+2)` 的最小值。

当需要计算 `dp(i-1)` 时，先从栈底开始检查其中数值的来源，如果 `dp(2i+2)` 或 `dp(2i+1)` 在栈里（如果在，这俩一定在最接近栈底的位置）则从栈底弹出（相当于队列，这是对一般单调栈的变体）。操作之后的新的栈底值就是 `dp(i)` 到 `dp(2i)` 的最小值（显然栈不会为空，因为如果 `dp(i)` 到 `dp(2i)` 中有比 `dp(2i+2)` 和 `dp(2i+1)` 更小的值，栈底就不会是 `dp(2i+2)` 或 `dp(2i+1)`，也就不会有数据被弹出；反之 `dp(i)` 到 `dp(2i)` 的最小值比 `dp(2i+2)` 和 `dp(2i+1)` 大，此值一定会在栈里）。利用此最小值即可算出 `dp(i-1)`，再按同样规则入栈即可。

当处理完 `dp(0)` 后，此值位于栈顶。

为了便于处理 `2i + 2 ≥ n` 时的 dp 值，可以在单调栈初始化的时候，直接放入一个 0，因为任何 dp 值都大于 0，这个 0 会一直待在栈底直到当 i 降到 $\lceil\frac{n}{2}\rceil-2=\lfloor\frac{n-3}{2}\rfloor$ 时被弹出。

时间复杂度 `O(n)`，空间复杂度 `O(n)`。

{% asset_code coding/assets/2944-minimum-number-of-coins-for-fruits/solution2.py %}
