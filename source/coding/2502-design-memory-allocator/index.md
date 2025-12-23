---
title: 2502. Design Memory Allocator
notebook: coding
tags:
- medium
date: 2025-02-25 11:38:20
updated: 2025-02-25 11:38:20
---
## Problem

You are given an integer `n` representing the size of a **0-indexed** memory array. All memory units are initially free.

You have a memory allocator with the following functionalities:

1. **Allocate** a block of `size` consecutive free memory units and assign it the id `mID`.
2. **Free** all memory units with the given id `mID`.

**Note** that:

- Multiple blocks can be allocated to the same `mID`.
- You should free all the memory units with `mID`, even if they were allocated in different blocks.

Implement the `Allocator` class:

- `Allocator(int n)` Initializes an `Allocator` object with a memory array of size `n`.
- `int allocate(int size, int mID)` Find the **leftmost** block of `size` **consecutive** free memory units and allocate it with the id `mID`. Return the block's first index. If such a block does not ext, return `-1`.
- `int freeMemory(int mID)` Free all memory units with the id `mID`. Return the number of memory units you have freed.

<https://leetcode.cn/problems/design-memory-allocator/>

**Example 1:**

> Input
> `["Allocator", "allocate", "allocate", "allocate", "freeMemory", "allocate", "allocate", "allocate", "freeMemory", "allocate", "freeMemory"]`
> `[[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]`
> Output
> `[null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]`
> Explanation
>
> ``` cpp
> Allocator loc = new Allocator(10); // Initialize a memory array of size 10. All memory units are initially free.
> loc.allocate(1, 1); // The leftmost block's first index is 0. The memory array becomes [1,_,_,_,_,_,_,_,_,_]. We return 0.
> loc.allocate(1, 2); // The leftmost block's first index is 1. The memory array becomes [1,2,_,_,_,_,_,_,_,_]. We return 1.
> loc.allocate(1, 3); // The leftmost block's first index is 2. The memory array becomes [1,2,3,_,_,_,_,_,_,_]. We return 2.
> loc.freeMemory(2); // Free all memory units with mID 2. The memory array becomes [1,_, 3,_,_,_,_,_,_,_]. We return 1 since there is only 1 unit with mID 2.
> loc.allocate(3, 4); // The leftmost block's first index is 3. The memory array becomes [1,_,3,4,4,4,_,_,_,_]. We return 3.
> loc.allocate(1, 1); // The leftmost block's first index is 1. The memory array becomes [1,1,3,4,4,4,_,_,_,_]. We return 1.
> loc.allocate(1, 1); // The leftmost block's first index is 6. The memory array becomes [1,1,3,4,4,4,1,_,_,_]. We return 6.
> loc.freeMemory(1); // Free all memory units with mID 1. The memory array becomes [_,_,3,4,4,4,_,_,_,_]. We return 3 since there are 3 units with mID 1.
> loc.allocate(10, 2); // We can not find any free block with 10 consecutive free memory units, so we return -1.
> loc.freeMemory(7); // Free all memory units with mID 7. The memory array remains the same since there is no memory unit with mID 7. We return 0.
> ```

**Constraints:**

- `1 <= n, size, mID <= 1000`
- At most `1000` calls will be made to `allocate` and `freeMemory`.

## Test Cases

``` python
class Allocator:

    def __init__(self, n: int):


    def allocate(self, size: int, mID: int) -> int:


    def freeMemory(self, mID: int) -> int:



# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
```

{% asset_code coding/2502-design-memory-allocator/solution_test.py %}

## Thoughts

已分配的内存可以用字典记录，key 为 `mID`。因为允许为同一个 `mID` 多次分配内存，那么 value 就要用一个数组，数组的一个元素为某一次分配的内存空间区间 `[start, end)`。

再用一个有序数组记录空闲的内存空间，数组的一个元素为一段连续空闲空间的起止位置 `[start, end)`。

分配内存的时候，从左到右依次扫描每一段连续空闲空间，找到第一段足够大的区间。如果该区间大小刚好等于申请的大小，则直接从数组中删掉。否则把 start 修改为 `start + size` 即可。

释放内存的时候，从字典中取出 `mID` 已经分配的内存空间数组，对其中的每一段做释放处理。因为空闲空间数组的有序的，可以用二分法找到待释放区间在空闲空间数组中的插入位置。只是需要注意，释放一段区间前，先要检查它是否跟左边和右边的空闲区间相连，如果相连则需要做合并。

构造方法的时间复杂度 `O(1)`，`allocate` 和 `freeMemory` 的时间复杂度最坏都是 `O(n)`。空间复杂度最坏是 `O(n)`。

## Code

{% asset_code coding/2502-design-memory-allocator/solution.py %}
