---
title: 295. Find Median from Data Stream
notebook: coding
tags:
- hard
date: 2024-11-16 18:40:50
updated: 2024-11-16 18:40:50
---
## Problem

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

- For example, for `arr = [2,3,4]`, the median is `3`.
- For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the MedianFinder class:

- `MedianFinder()` initializes the `MedianFinder` object.
- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
- `double findMedian()` returns the median of all elements so far. Answers within `10⁻⁵` of the actual answer will be accepted.

<https://leetcode.com/problems/find-median-from-data-stream/>

**Example 1:**

> Input
> `["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]`
> `[[], [1], [2], [], [3], []]`
> Output
> `[null, null, null, 1.5, null, 2.0]`
>
> Explanation
>
> ```c++
> MedianFinder medianFinder = new MedianFinder();
> medianFinder.addNum(1);    // arr = [1]
> medianFinder.addNum(2);    // arr = [1, 2]
> medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
> medianFinder.addNum(3);    // arr[1, 2, 3]
> medianFinder.findMedian(); // return 2.0
> ```

**Constraints:**

- `-10⁵ <= num <= 10⁵`
- There will be at least one element in the data structure before calling `findMedian`.
- At most `5 * 10⁴` calls will be made to `addNum` and `findMedian`.

**Follow up:**

- If all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?
- If `99%` of all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?

## Test Cases

```python
class MedianFinder:

    def __init__(self):


    def addNum(self, num: int) -> None:


    def findMedian(self) -> float:



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```

{% snippet solution_test.py %}

## Thoughts

因为后续数据的分布未知，曾经见过的任何一个数都有可能成为中位数，从信息量的角度看，所有见过的数字是一定要存下来的。

中位数比它左边的所有数字都不小，且比它右边的所有数字都不大。可以用最大堆存左半个数组，最小堆存右半个数组，并保持两个堆的大小一致或相差不超过 1。

如果数据总数是偶数，那么最中间的两个数就分别是左半边的最大也右半边的最小，取两个堆的堆顶求平均即可。如果总数是奇数，那么较大的堆（比另一个堆多一个数）的堆顶就是中位数。

实现的时候，可以实现比如最大堆，并用存储相反数的方式模拟最小堆（反之亦然）。

没必要始终保持左半边的堆的大小不比右半边的小，虽然代码会简洁一些，但平均会多一组出堆再入堆操作。对于新的数字，先根据两个堆的堆顶数字大小判断应该放入哪边，然后如果出现两边的堆大小过于不平衡（大小相差超过 1），再从较大的堆弹出堆顶，放入另一个堆中。

设已经有了 n 个数字，那么下次增加新数字的时间复杂度是 `O(log n)`，查中位数的时间复杂度是 `O(1)`。整体需要 `O(n)` 空间复杂度维持两个堆。

## Code

{% snippet solution.py %}

## Follow up 1

如果所有的数据都只在 `[1, 100]` 范围内，就不需要堆了，只要记录每个整数的次数。

记录当前中位数是哪个整数，以及该整数在左右半边分别有多少个。下次 `addNum` 时，更新这个信息。

`addNum` 和 `findMedian` 的时间和空间复杂度都是 `O(1)`。

{% snippet solution_follow1.py %}

## Follow up 2

如果所有的数据有 99% 在 `[1, 100]` 范围内，那么中位数也有极大的概率出现在 `[1, 100]` 内，可以在上边的基础上，多记录 `< 0` 和 `> 100` 的数字个数。其他的逻辑不受影响。

极端情况，比如给的第一个数字就在 `[1, 100]` 范围之外，然后立刻要获取中位数，想要依然能正确返回结果，可以记录 `< 0` 的最大的几个数和 `> 100` 的最小的几个数，根据输入数据的分布特点，可能最多各存一到两个就行。
