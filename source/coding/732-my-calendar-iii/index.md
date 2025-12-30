---
title: 732. My Calendar III
notebook: coding
tags:
- hard
date: 2025-01-02 20:52:29
updated: 2025-01-02 20:52:29
---
## Problem

A `k`-booking happens when `k` events have some non-empty intersection (i.e., there is some time that is common to all `k` events.)

You are given some events `[startTime, endTime)`, after each given event, return an integer `k` representing the maximum `k`-booking between all the previous events.

Implement the `MyCalendarThree` class:

- `MyCalendarThree()` Initializes the object.
- `int book(int startTime, int endTime)` Returns an integer `k` representing the largest integer such that there exists a `k`-booking in the calendar.

<https://leetcode.cn/problems/my-calendar-iii/>

**Example 1:**

> Input
> `["MyCalendarThree", "book", "book", "book", "book", "book", "book"]`
> `[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]`
> Output
> `[null, 1, 1, 2, 3, 3, 3]`
> Explanation
>
> ```c++
> MyCalendarThree myCalendarThree = new MyCalendarThree();
> myCalendarThree.book(10, 20); // return 1
> myCalendarThree.book(50, 60); // return 1
> myCalendarThree.book(10, 40); // return 2
> myCalendarThree.book(5, 15); // return 3
> myCalendarThree.book(5, 10); // return 3
> myCalendarThree.book(25, 55); // return 3
> ```

**Constraints:**

- `0 <= startTime < endTime <= 10⁹`
- At most `400` calls will be made to `book`.

## Test Cases

```python
class MyCalendarThree:

    def __init__(self):


    def book(self, startTime: int, endTime: int) -> int:



# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
```

{% asset_code solution_test.py %}

## Thoughts

系列问题：

- [729. My Calendar I](../729-my-calendar-i/index.md) 任何时刻不能有两个 events
- [731. My Calendar II](../731-my-calendar-ii/index.md) 任何时刻不能有三个 events

本题不再做限制，但是要能知道重叠的 events 的最大数量。

考虑记录每一个时间段的 events 个数。当两个 events 有重叠的时候，需要根据重叠的情况拆分成几个小的时间段，记录每个片段的 events 数量。

实现起来很麻烦，即便两头加了 `-inf` 和 `inf` 避免越界，仍然有各种边界情况需要处理，到处都是边界值刺客。而且运行时间很长（常数系数太大）。

[solution_omg.py](solution_omg.py)

> 虽然 AC 了，但不确定会不会在某些边缘 case 下会出错。

实际上大的区间被不断打散，经常会出现连续的多个区间在时间上也是相连的，与其以区间的形式一个一个记录，不如直接记录所有的分界点。对于一个时间段 `[start, end)`，可以记录成 `[(start, 1), (end, 0)]`，表示从 start 开始的每个时刻都有一个 event，从 end 开始的每个时刻则没有 event。如果另一个时间段 `[start2, end2)` 跟它有重叠，比如 `start < start2 < end < end2`，记录数组就可以改为 `[(start, 1), (start2, 2), (end, 1), (end2, 0)]`，说明时间段 `[start2, end)` 内有两个 events，end2 开始的时刻都没有 event，而 `[start, start2)` 和 `[end, end2)` 时段都各有一个 event。

> 可以在数组两头分别加上 `(-inf, 0)` 和 `(inf, 0)` 以简化边界处理。

对于一个待添加的时间段 `[start, end)`，用二分搜索分别找到 start 和 end 的插入位置（记为 i 和 j）。易知从 i（包含）到 j（不含）的每一个时间分界点，从其开始的每个时刻都多了一个 event （待添加的这个）。只需要注意 start 和 end 是不是原本已经存在并做好相应的更新。

> 注意 Python 自带的 [`bisect.bisect_left`](https://docs.python.org/3/library/bisect.html#bisect.bisect_left) 的返回值（比如记作 i），有 `∀arr[:i] < x`，`∀arr[i:] ≥ x`（在数组 arr 中二分查找 x 的插入位置）。

`MyCalendarThree` 构造的时间复杂度 `O(1)`。

`book` 方法的时间复杂度最坏是 `O(n)`。

空间复杂度 `O(n)`。

提交后运行速度是上边时间段方法的 200 倍，runtime beats 100%。

## Code

{% asset_code solution.py %}
