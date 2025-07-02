---
title: 731. My Calendar II
notebook: coding
tags:
- medium
date: 2025-01-02 16:19:06
updated: 2025-01-02 16:19:06
---
## Problem

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a **triple booking**.

A **triple booking** happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers `startTime` and `endTime` that represents a booking on the half-open interval `[startTime, endTime)`, the range of real numbers `x` such that `startTime <= x < endTime`.

Implement the `MyCalendarTwo` class:

- `MyCalendarTwo()` Initializes the calendar object.
- `boolean book(int startTime, int endTime)` Returns `true` if the event can be added to the calendar successfully without causing a **triple booking**. Otherwise, return `false` and do not add the event to the calendar.

<https://leetcode.cn/problems/my-calendar-ii/>

**Example 1:**

> Input
> `["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]`
> `[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]`
> Output
> `[null, true, true, true, false, true, true]`
> Explanation
>
> ``` c++
> MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
> myCalendarTwo.book(10, 20); // return True, The event can be booked.
> myCalendarTwo.book(50, 60); // return True, The event can be booked.
> myCalendarTwo.book(10, 40); // return True, The event can be double booked.
> myCalendarTwo.book(5, 15);  // return False, The event cannot be booked, because it would result in a triple booking.
> myCalendarTwo.book(5, 10); // return True, The event can be booked, as it does not use time 10 which is already double booked.
> myCalendarTwo.book(25, 55); // return True, The event can be booked, as the time in [25, 40) will be double booked with the third event, the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
> ```

**Constraints:**

- `0 <= start < end <= 10⁹`
- At most `1000` calls will be made to `book`.

## Test Cases

``` python
class MyCalendarTwo:

    def __init__(self):


    def book(self, startTime: int, endTime: int) -> bool:



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
```

{% asset_code coding/assets/731-my-calendar-ii/solution_test.py %}

## Thoughts

[729. My Calendar I](729-my-calendar-i) 的进阶版，从任意两个 events 不能有重叠，扩展为三个 events 不能有共同的交集。

如果已经知道所有同时被两个 events 占用的时段，就可以像 [729. My Calendar I](729-my-calendar-i) 那样直接判断一个新的 event，是否跟某个时段有重叠，有的话就无法预订。

按这个思路，维护两个有序数组，`single_occupies` 记录所有被至少一个 event 占用的时段，`double_occupies` 记录所有被两个 events 同时占用的时段，都按照时段的开始时间排序，且任意两个时段之间没有重叠。

对于想要 book 的一个 event，对 `double_occupies` 用二分搜索找到可以插入的位置（如 i），检查 `double_occupies[i-1]` 的结束时间是否在 event 之前，`double_occupies[i]` 的开始时间是否在 event 之后。如果都符合，则此 event 可以预订成功，否则直接返回 false。这个逻辑跟 [729. My Calendar I](729-my-calendar-i) 一样。

> 为了简化边界的处理，可以给 `single_occupies` 和 `double_occupies` 的两头分别加一个 `(-inf, -inf)` 和 `(inf, inf)` 做占位符。

麻烦在于维护 `single_occupies` 和 `double_occupies` 这两个数组。

首先用二分搜索在 `single_occupies` 中找到可以插入的位置，从这个位置开始，找到新 event 会覆盖到的所有后续时段，一方面需要把每个时段与新 event 的交集加入到 `double_occupies`（因为这些交集部分同时被两个 events 占用），另一方面需要将所有这些时段合并为一个（以便以后使用）。

实操的时候需要注意新 event 的两个端点处，可能会跟 `single_occupies` 中的时段部分重叠，而中间的部分会完全覆盖 `single_occupies` 中的对应时段。

> 被边界情况搞到吐血。所幸提交后 runtime beats 100%。

`MyCalendarTwo` 构造的时间复杂度 `O(1)`。

`book` 方法，判定能否预订的时间复杂度 `O(log n)`，执行预订的时间复杂度 `O(n)`。

空间复杂度 `O(n)`。

## Code

{% asset_code coding/assets/731-my-calendar-ii/solution.py %}

> 此实现中未对相邻相连的两个时段做合并。比如 `[10, 20)` 和 `[20, 50)` 虽然可以连成一个完整的 `[10, 50)`，但代码中并未进行合并，不会影响后续处理逻辑。
