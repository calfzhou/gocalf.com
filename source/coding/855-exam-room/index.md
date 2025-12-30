---
title: 855. Exam Room
notebook: coding
tags:
- medium
date: 2024-12-23 11:39:00
updated: 2024-12-23 11:39:00
---
## Problem

There is an exam room with `n` seats in a single row labeled from `0` to `n - 1`.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person. If there are multiple such seats, they sit in the seat with the lowest number. If no one is in the room, then the student sits at seat number `0`.

Design a class that simulates the mentioned exam room.

Implement the `ExamRoom` class:

- `ExamRoom(int n)` Initializes the object of the exam room with the number of the seats `n`.
- `int seat()` Returns the label of the seat at which the next student will set.
- `void leave(int p)` Indicates that the student sitting at seat `p` will leave the room. It is guaranteed that there will be a student sitting at seat `p`.

<https://leetcode.cn/problems/exam-room/>

**Example 1:**

> Input
> `["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]`
> `[[10], [], [], [], [], [4], []]`
> Output
> `[null, 0, 9, 4, 2, null, 5]`
>
> Explanation
>
> ```c++
> ExamRoom examRoom = new ExamRoom(10);
> examRoom.seat(); // return 0, no one is in the room, then the student sits at seat number 0.
> examRoom.seat(); // return 9, the student sits at the last seat number 9.
> examRoom.seat(); // return 4, the student sits at the last seat number 4.
> examRoom.seat(); // return 2, the student sits at the last seat number 2.
> examRoom.leave(4);
> examRoom.seat(); // return 5, the student sits at the last seat number 5.
> ```

**Constraints:**

- `1 <= n <= 10⁹`
- It is guaranteed that there is a student sitting at seat `p`.
- At most `10⁴` calls will be made to `seat` and `leave`.

## Test Cases

```python
class ExamRoom:

    def __init__(self, n: int):

    def seat(self) -> int:

    def leave(self, p: int) -> None:


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
```

{% asset_code solution_test.py %}

## Thoughts

首先看如何计算「the maximum distance to the closest person」。

设有一段没有人坐的区域，该区域的左边位置 l 处有人，右边位置 r 处有人。显然这个距离（记为 dis）为 `dis = (r - l) // 2`。

还需要考虑两头的情况，如果位置 0 没有人，可以令 `l = -1`，此时 `dis = r`。如果位置 `n - 1` 没人坐，可以令 `r = n`，此时 `dis = n - l - 1`。这两个设定是彼此互洽的。

汇总一下，对于任意的空位区间，「the maximum distance to the closest person」的计算逻辑为：

```python
if l == -1:
    dis = r
elif r == n:
    dis = n - l - 1
else:
    dis = (r - l) >> 1
```

如果一个人要坐在这个区间，当 `l = -1` 时显然直接坐 0 号座位，否则坐 `l + dis` 号座位。

再看如何维护已经被占用的座位信息。

一个直观的做法是维护一个有序集合，记录所有被占用的座位号（设共有 m 个座位被占用）。初始时集合为 `[-1, n]`，这样可以简化边界判定。

- 一个人离开的时候，可以用二分法找到对应的记录并删除。时间复杂度 `O(log m)` 或 `O(m)`（如果用普通数组）。
- 一个人要坐下的时候，遍历每一个空位区间，记录第一个 dis 值最大的区间，让他坐在这个区间，并把所坐的座位号更新到有序集合中。时间复杂度 `O(m)`。

这个方法对于离开的操作比较快，但如果坐下的操作更频繁，应当考虑对坐下操作优化。

因为坐下的时候要找 dis 值最大的区间，所以可以用堆来记录所有的空位区间。如果用最小堆，需要以 `(-dis, l)` 作为比较大小的 key，可以让堆顶是 dis 最大的区间中最靠左的那个。初始时堆中只有一个区间，即 `(dis = n, l = -1, r = n)`。

- 一个人要坐下的时候，取堆顶的空位区间坐下即可。这时候此空位区间会被分割成左右两个空位区间，把堆顶区间弹出，把分割得到的两个新区间加入堆中。时间复杂度 `O(log m)`。如果借助 `l = -1` 和 `r = n` 来管理最两头的空位，可以大大简化边界值的处理。
- 一个人离开的时候，需要遍历堆中元素，找到该位置左边和右边的空位区间，将这两个区间删掉，加入合并之后的区间，然后恢复堆。时间复杂度 `O(m)`。

两个方法的空间复杂度都是 `O(m)`。

## Code

### Leave Fast, Seat Slow

{% asset_code solution.py %}

### Seat Fast, Leave Slow

{% asset_code solution2.py %}

实际提交运行的话，这个策略比上一个快两百多倍。
