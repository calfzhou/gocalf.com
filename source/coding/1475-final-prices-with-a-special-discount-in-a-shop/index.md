---
title: 1475. Final Prices With a Special Discount in a Shop
notebook: coding
tags:
- easy
date: 2024-12-18 11:31:56
updated: 2024-12-18 23:05:48
---
## Problem

You are given an integer array `prices` where `prices[i]` is the price of the `iᵗʰ` item in a shop.

There is a special discount for items in the shop. If you buy the `iᵗʰ` item, then you will receive a discount equivalent to `prices[j]` where `j` is the minimum index such that `j > i` and `prices[j] <= prices[i]`. Otherwise, you will not receive any discount at all.

Return an integer array `answer` where `answer[i]` is the final price you will pay for the `ith` item of the shop, considering the special discount.

<https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/>

**Example 1:**

> Input: `prices = [8,4,6,2,3]`
> Output: `[4,2,4,2,3]`
> Explanation:
> For item 0 with `price[0]=8` you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is `8 - 4 = 4`.
> For item 1 with `price[1]=4` you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is `4 - 2 = 2`.
> For item 2 with `price[2]=6` you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is `6 - 2 = 4`.
> For items 3 and 4 you will not receive any discount at all.

**Example 2:**

> Input: `prices = [1,2,3,4,5]`
> Output: `[1,2,3,4,5]`
> Explanation: In this case, for all items, you will not receive any discount at all.

**Example 3:**

> Input: `prices = [10,1,1,6]`
> Output: `[9,0,1,6]`

**Constraints:**

- `1 <= prices.length <= 500`
- `1 <= prices[i] <= 1000`

## Test Cases

``` python
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
```

{% asset_code coding/assets/1475-final-prices-with-a-special-discount-in-a-shop/solution_test.py %}

## Thoughts

按题目限定的规模，直接暴力（brute force）就够了。对于位置 i，从 `i + 1` 开始找到第一个不高于 `prices[i]` 的价格，作为折扣减去即可。

时间复杂度 `O(n²)`，附加的空间复杂度 `O(1)`。

## Code

{% asset_code coding/assets/1475-final-prices-with-a-special-discount-in-a-shop/solution.py %}

## O(n log n)

有点儿类似 [1847. Closest Room](../1847-closest-room/index.md)，事先对 prices 排序，从小到大扫描，把不高于当前价格的商品加入到有序集合，该有序集合按商品下标保持有序。然后在该有序集合中用二分法查找当前价格的下标，找到大于其下标中的最小。

扫描排序后 prices 的过程中，所有已经处理过的就都不比当前价格高，对于重复的相等价格，可以在前边排序的时候，优先按价格，其次按下标（逆序）排序，确保可选的商品一定会被先处理。

时间复杂度 `O(n log n)`（虽然 Python list 的 [`bisect.insort`](https://docs.python.org/3/library/bisect.html#bisect.insort) 也是 `O(n)` 时间，但在当下规模下还是比较快的，更大规模可以用其他有序集合的实现），空间复杂度 `O(n)`。

不过实际提交跑就很慢，可能系数太大了。

{% asset_code coding/assets/1475-final-prices-with-a-special-discount-in-a-shop/solution_nlogn.py %}

## O(n)

这种找左侧/右侧第一个比当前元素小/大的问题，都可以使用单调栈，线性时间可解。

单调栈是保持栈里的元素有序。

比如 `prices = [8,4,6,2,5]`。从右向左扫描 prices。

1. 第 -1 个元素 5：此时栈为空，说明没有在其右边且不大于它的元素。将 5 入栈。
2. 第 -2 个元素 2：此时栈顶为 5，大于 2，把 5 弹出。之后栈变为空，也说明没有在其右边且不大于它的元素。将 2 入栈。这里的关键是 5 的出栈是安全的，因为：
   - 如果后续元素小于 2，那么也一定小于 5，5 在这里没用；
   - 如果后续元素大于等于 2，2 就是离它最近且不大于它的元素，也不需要考虑 5。
3. 第 -3 个元素 6：此时栈顶 2 小于等于 6，说明 2 就是其右边第一个不大于它的元素，即为相应的折扣。然后将 6 入栈（目前栈为 `[2, 6]`）。
4. 第 -4 个元素 4：栈顶 6 大于 4，弹出。栈顶变为 2，小于等于 6，说明 2 就是其右边第一个不大于它的元素，即为相应的折扣。将 4 入栈（即 `[2, 4]`）。
5. 第 -5 个元素 8：栈顶 4 小于等于 8，即为相应折扣。将 8 入栈（即 `[2, 4, 8]`）。

{% asset_code coding/assets/1475-final-prices-with-a-special-discount-in-a-shop/solution_n.py %}

## Another O(n)

上边是逆向扫描数组，还可以正向扫描（从左到右）。

在一个价格右边找第一个不大于它的价格作为折扣。逆向扫描的时候，是把折扣的候选值放在栈中。那么正向扫描时，是把待打折的元素（其实是下标）放在栈中。

1. 第 1 个元素 8：此时栈为空，说明它无法作为其他商品的折扣（它左边没有不小于它的元素）。将下标 0 入栈（因为后续还需要使用下标对该位置的元素进行操作）。
2. 第 2 个元素 4：此时栈顶价格为 8（下标 0），大于等于 4，说明 4 可以作为其折扣，将其出栈，出栈的同时给对应下标 0 的价格减去当前价格（折扣）4。之后栈为空，将下标 1 入栈。
3. 第 3 个元素 6：此时栈顶价格为 4（下标 1），小于 6，说明 6 不能作为其折扣，直接入栈（目前栈为 `[1(4), 2(6)]`）。
4. 第 4 个元素 2：此时栈顶价格为 6（下标 2），大于等于 2，说明 2 可以作为其折扣，将其出栈并同时给对应下标 2 的价格减去当前价格（折扣）2。新的栈顶价格为 4（下标 1），依然大于等于 2，说明 2 也可作为其折扣，将其出栈并同时给下标 1 的价格减去当前价格 2。之后栈为空，将下标 3 入栈。
5. 第 5 个元素 3：此时栈顶价格为 2（下标 3），小于 3，说明 3 不能作为其折扣，直接入栈（目前栈为 `[3(2), 4(3)]`）。

最后栈里剩下的都是找不到折扣的。

正向扫描优点还挺多的，首先扫描方向更符合直觉，其次代码简洁很多，再次如果做 in-place 修改，修改操作发生在被修改元素（的下标）出栈的时候，修改之后也就不会被访问到，比较安全（节省空间）。而逆向扫描，修改操作发生在入栈的时候，需要注意入栈的应该是修改前的值。但有些场景需要入栈下标（如 [739. Daily Temperatures](../739-daily-temperatures/index.md)），那么通过下标再引用对应元素值的时候，就要注意应该取到修改前还是修改后的值，从而考虑是否必需开辟额外的存储空间记录修改后的值。

{% asset_code coding/assets/1475-final-prices-with-a-special-discount-in-a-shop/solution_n2.py %}
