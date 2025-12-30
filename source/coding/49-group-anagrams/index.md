---
title: 49. Group Anagrams
notebook: coding
tags:
- medium
date: 2024-11-17 22:45:23
updated: 2024-11-17 22:45:23
---
## Problem

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

> An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

<https://leetcode.com/problems/group-anagrams/>

**Example 1:**

> Input: `strs = ["eat","tea","tan","ate","nat","bat"]`
> Output: `[["bat"],["nat","tan"],["ate","eat","tea"]]`
> Explanation:
>
> - There is no string in strs that can be rearranged to form `"bat"`.
> - The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.
> - The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

**Example 2:**

> Input: `strs = [""]`
> Output: `[[""]]`

**Example 3:**

> Input: `strs = ["a"]`
> Output: `[["a"]]`

**Constraints:**

- `1 <= strs.length <= 10⁴`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Test Cases

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
```

{% asset_code solution_test.py %}

## Thoughts

每个 group 都有共同的「字母成分特征」，即包含哪几个字母、每个字母出现几次。

可以构造一个特征值，确保同组内的字符串计算得到的特征值一致，但不同组的不一致。利用该特征值做哈希表即可。

可以对某个字符串按字母排序，排序后的字符串作为特征值。

因为只有 26 个字母，可以统计字符串中每个字母的次数，拼成一个长度为 26 的不变元组，像 Python 就可以直接以不变元组作为哈希表的 key。

如果不借助 Python 这种特性，可以把不变元组格式化为字符串，或者用多层的哈希表，每层只对一个字母的数量做哈希散列。

整体时间复杂度为 `O(n * k)` 或者 `O(n * k * log k)`，其中 `k` 是每个字符串的平均长度。

## Code

{% asset_code solution.py %}

直接把字符串排序当作 key 在字典中查找 group，就挺快的了。
