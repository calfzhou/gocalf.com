---
title: 2349. Design a Number Container System
notebook: coding
tags:
- medium
date: 2025-02-08 17:43:23
updated: 2025-02-08 17:43:23
---
## Problem

Design a number container system that can do the following:

- **Insert** or **Replace** a number at the given index in the system.
- **Return** the smallest index for the given number in the system.

Implement the `NumberContainers` class:

- `NumberContainers()` Initializes the number container system.
- `void change(int index, int number)` Fills the container at `index` with the `number`. If there is already a number at that `index`, replace it.
- `int find(int number)` Returns the smallest index for the given `number`, or `-1` if there is no index that is filled by `number` in the system.

<https://leetcode.com/problems/design-a-number-container-system/>

**Example 1:**

> Input
> `["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]`
> `[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]`
> Output
> `[null, -1, null, null, null, null, 1, null, 2]`
> Explanation
>
> ``` cpp
> NumberContainers nc = new NumberContainers();
> nc.find(10); // There is no index that is filled with number 10. Therefore, we return -1.
> nc.change(2, 10); // Your container at index 2 will be filled with number 10.
> nc.change(1, 10); // Your container at index 1 will be filled with number 10.
> nc.change(3, 10); // Your container at index 3 will be filled with number 10.
> nc.change(5, 10); // Your container at index 5 will be filled with number 10.
> nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
> nc.change(1, 20); // Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20.
> nc.find(10); // Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.
> ```

**Constraints:**

- `1 <= index, number <= 10⁹`
- At most `10⁵` calls will be made **in total** to `change` and `find`.

## Test Cases

``` python
class NumberContainers:

    def __init__(self):


    def change(self, index: int, number: int) -> None:


    def find(self, number: int) -> int:



# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
```

{% asset_code coding/2349-design-a-number-container-system/solution_test.py %}

## Thoughts

跟 [3160. Find the Number of Distinct Colors Among the Balls](3160-find-the-number-of-distinct-colors-among-the-balls) 差不多。index 相当于球的编号，number 相当于颜色。主要的区别是本题需要记录每个 number 对应的 index 数组，以便随时可以查询此 number 所在的所有 index 的最小值。

同样用字典记录每个 index 最新的 number。再用字典记录每个 number 的所有 index，用有序数组记录，这里直接用 Python 的 list。需要增加或删除的时候，先用二分法查找再执行插入或删除操作。

构造函数的时间复杂度 `O(1)`；`change` 方法的时间复杂度 `O(n)`；`find` 方法的时间复杂度 `O(n)`。空间复杂度 `O(n)`。其中 n 是 `change` 的调用次数。

## Code

{% asset_code coding/2349-design-a-number-container-system/solution.py %}
