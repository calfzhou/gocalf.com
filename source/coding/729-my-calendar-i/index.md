---
title: 729. My Calendar I
notebook: coding
tags:
- medium
date: 2025-01-02 00:36:56
updated: 2025-01-02 00:36:56
---
## Problem

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a **double booking**.

A **double booking** happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers `startTime` and `endTime` that represents a booking on the half-open interval `[startTime, endTime)`, the range of real numbers `x` such that `startTime <= x < endTime`.

Implement the `MyCalendar` class:

- `MyCalendar()` Initializes the calendar object.
- `boolean book(int startTime, int endTime)` Returns `true` if the event can be added to the calendar successfully without causing a **double booking**. Otherwise, return `false` and do not add the event to the calendar.

<https://leetcode.cn/problems/my-calendar-i/>

**Example 1:**

> Input
> `["MyCalendar", "book", "book", "book"]`
> `[[], [10, 20], [15, 25], [20, 30]]`
> Output
> `[null, true, false, true]`
> Explanation
>
> ```c++
> MyCalendar myCalendar = new MyCalendar();
> myCalendar.book(10, 20); // return True
> myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
> myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
> ```

**Constraints:**

- `0 <= start < end <= 10⁹`
- At most `1000` calls will be made to `book`.

## Test Cases

```python
class MyCalendar:

    def __init__(self):


    def book(self, startTime: int, endTime: int) -> bool:



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
```

{% asset_code solution_test.py %}

## Thoughts

用一个数组记录所有已知的 events，且按开始时间排序。

对于想要 book 的一个 event，用二分搜索找到可以插入的位置。用 Python 的 [`bisect.bisect_left`](https://docs.python.org/3/library/bisect.html#bisect.bisect_left)，返回的 i 满足 `∀events[:i] < event`、`∀events[i:] ≥ event`。这时候只要检查 `events[i-1]` 是否在 event 之前结束、event 是否在 `events[i]` 之前结束。如果都符合，则可以将 event 插入到位置 i。

`MyCalendar` 构造的时间复杂度 `O(1)`。

`book` 方法的时间复杂度，当 book 失败的时候是 `O(log n)`，book 成功的时候是 `O(n)`。如果用更高级的数据结构（比如有序集合、红黑树、AVL 等），可以做到 book 成功时也是 `O(log n)` 时间。

空间复杂度 `O(n)`。

## Code

{% asset_code solution.py %}
