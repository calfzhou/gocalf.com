---
title: 321. Create Maximum Number
notebook: coding
tags:
- hard
- todo
date: 2024-12-30 15:45:35
updated: 2024-12-30 15:45:35
---
## Problem

You are given two integer arrays `nums1` and `nums2` of lengths `m` and `n` respectively. `nums1` and `nums2` represent the digits of two numbers. You are also given an integer `k`.

Create the maximum number of length `k <= m + n` from digits of the two numbers. The relative order of the digits from the same array must be preserved.

Return an array of the `k` digits representing the answer.

<https://leetcode.com/problems/create-maximum-number/>

**Example 1:**

> Input: `nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5`
> Output: `[9,8,6,5,3]`

**Example 2:**

> Input: `nums1 = [6,7], nums2 = [6,0,4], k = 5`
> Output: `[6,7,6,0,4]`

**Example 3:**

> Input: `nums1 = [3,9], nums2 = [8,9], k = 3`
> Output: `[9,8,9]`

**Constraints:**

- `m == nums1.length`
- `n == nums2.length`
- `1 <= m, n <= 500`
- `0 <= nums1[i], nums2[i] <= 9`
- `1 <= k <= m + n`
- `nums1` and `nums2` do not have leading zeros.

## Test Cases

``` python
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
```

{% asset_code coding/assets/321-create-maximum-number/solution_test.py %}

## Thoughts

将 k 分成 k1 和 k2（`k = k1 + k2`），分别从 nums1 中 取 k1 个元素、从 nums2 中取 k2 个元素，合并成长度为 k 的数组。

对于特定的 k1 和 k2，从 nums1 和 nums2 中取的时候，应该取最大的子序列出来（稍后看如何取出最大的）。合并的时候也合并成最大的，就可以得到 k1 和 k2 对应的最大的结果。遍历所有可能的 k1 和 k2，取结果最大的那个。

### 遍历

显然 k1 的下限为 `max{0, k - n}`，上限为 `min{m, k}`。遍历所有可能的 k1 即可。

### 选取

在 [1475. Final Prices With a Special Discount in a Shop](../1475-final-prices-with-a-special-discount-in-a-shop/index.md) 中提到用单调栈确定数组中每个元素左侧/右侧第一个比当前值小/大的元素，其中 [正向扫描](../1475-final-prices-with-a-special-discount-in-a-shop/index.md#Another-O-n) 时最终留在单调栈里的就是右侧没有比它更大值的元素集合（如果是在找右侧第一个比当前值大的元素）。代码示意：

``` python
def pick_max(nums: list[int]) -> list[int]:
    stack = []
    for num in nums:
        while stack and stack[-1] < num:
            stack.pop()

        stack.append(num)

    return stack
```

比如 `nums = [9, 1, 2, 5, 8, 3]`，最后栈里剩下的是 `[9, 8, 3]`，这几个数在 nums 中右侧都找不到比它们更大的数。

如果 `k = 3`，`[9, 8, 3]` 刚好就是从 nums 中能找到的最大的子序列。如果 `k < 3`，那么在 `[9, 8, 3]` 中从左开始取 k 个即可。如果 `k > 3`，那么在单调栈弹出的时候记录弹出的个数，最多弹出 `n - k` 个，够了之后就不再弹出。可以有两种类似的对 `pick_max` 的改造方法：

``` python
def pick_max_sub(nums: list[int], k: int) -> list[int]:
    remain_drop = len(nums) - k
    stack = []
    for num in nums:
        while remain_drop and stack and stack[-1] < num:
            stack.pop()
            remain_drop -= 1

        if len(stack) < k:
            stack.append(num)
        else:
            remain_drop -= 1

    return stack
```

``` python
def pick_max_sub(nums: list[int], k: int) -> list[int]:
    remain_drop = len(nums) - k
    stack = []
    for num in nums:
        while remain_drop and stack and stack[-1] < num:
            stack.pop()
            remain_drop -= 1

        stack.append(num)

    return stack[:k]
```

可知数组 `[9, 1, 2, 5, 8, 3]` 对于不同的 k，返回的结果分别为：

``` yaml
1: [9]
2: [9, 8]
3: [9, 8, 3]
4: [9, 5, 8, 3]
5: [9, 2, 5, 8, 3]
6: [9, 1, 2, 5, 8, 3]
```

对于指定的 k，算法的时间复杂度都是 `O(n)`，空间复杂度 `O(k)`（或者 `O(n)`）。

### 合并

从 nums1 中取出长度为 k1 的子序列 sub1，从 nums2 中取出长度为 k2 的子序列 sub2，需要合并二者使得结果最大。

这就跟归并类似，每次看 sub1 和 sub2 最左边的数字，哪个大就把哪个取走。

但是如果两边最左边数字相等，就不能随意选，还要继续比下一个数字。

对于长度分别为 m 和 n 的两个序列，合并的时间复杂度最环情况是 `O(m * n)`，一般情况下是 `O(m + n)`。

### 整体

所以对 k1 从 `max{0, k - n}` 遍历到 `min{m, k}`，最多 k + 1 次。每一次用 `O(m + n)` 时间取出两个子序列，用平均 `O(k)` 时间合并。

最终时间复杂度大约 `O(k * (m + n))`，空间复杂度 `O(k)`。

## Code

{% asset_code coding/assets/321-create-maximum-number/solution.py %}

选取和合并逻辑的测试代码：

{% asset_code coding/assets/321-create-maximum-number/solution_inner_test.py %}

## ToDo

在考虑贪心法的可行性。每次直接从 nums1 和 nums2 中找出能够作为结果数组的下一个元素。显然每次都应该在可选的位置区间内找最大的数字。而使用一定的预处理，可以让每次操作的时间复杂度接近常数。

但如果两个数字可选的最大数字一样，就应该类似于上边合并那里，需要再比前边的数字，而不能随便选。这块还没想好可行性以及具体的处理逻辑。
