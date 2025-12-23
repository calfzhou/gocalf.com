---
title: 382. Linked List Random Node
notebook: coding
tags:
- medium
date: 2025-01-01 14:03:23
updated: 2025-01-01 14:03:23
---
## Problem

Given a singly linked list, return a random node's value from the linked list. Each node must have the **same probability** of being chosen.

Implement the `Solution` class:

- `Solution(ListNode head)` Initializes the object with the head of the singly-linked list `head`.
- `int getRandom()` Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.

<https://leetcode.com/problems/linked-list-random-node/>

**Example 1:**

{% invert %}
![case1](assets/382-linked-list-random-node/case1.png)
{% endinvert %}

> Input
> `["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]`
> `[[[1, 2, 3]], [], [], [], [], []]`
> Output
> `[null, 1, 3, 2, 2, 3]`
> Explanation
>
> ``` c++
> Solution solution = new Solution([1, 2, 3]);
> solution.getRandom(); // return 1
> solution.getRandom(); // return 3
> solution.getRandom(); // return 2
> solution.getRandom(); // return 2
> solution.getRandom(); // return 3
> // getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
> ```

**Constraints:**

- The number of nodes in the linked list will be in the range `[1, 10⁴]`.
- `-10⁴ <= Node.val <= 10⁴`
- At most `10⁴` calls will be made to `getRandom`.

**Follow up:**

- What if the linked list is extremely large and its length is unknown to you?
- Could you solve this efficiently without using extra space?

## Test Cases

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):


    def getRandom(self) -> int:



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
```

{% asset_code coding/382-linked-list-random-node/solution_test.py %}

## Thoughts

`Solution` 类在构造的时候，直接用数组记录下链表中的所有数字。每次调用 `getRandom` 随机选取其中一个返回即可。

`__init__` 的时间复杂度 `O(n)`，`getRandom` 的时间复杂度 `O(1)`，整体空间复杂度 `O(n)`。

## Code

{% asset_code coding/382-linked-list-random-node/solution.py %}

## O(1) Space

如果要 `O(1)` 空间复杂度，可以在构造的时候只记录链表的总长度。每次调用 `getRandom` 生成一个随机位置，遍历链表到指定位置的节点并返回其值即可。

`__init__` 的时间复杂度 `O(n)`，`getRandom` 的时间复杂度 `O(n)`，整体空间复杂度 `O(1)`。

{% asset_code coding/382-linked-list-random-node/solution2.py %}
