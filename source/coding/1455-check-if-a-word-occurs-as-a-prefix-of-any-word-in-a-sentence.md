---
title: 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
notebook: coding
tags:
- easy
date: 2024-12-02 11:17:09
updated: 2024-12-02 11:17:09
---
## Problem

Given a `sentence` that consists of some words separated by a **single space**, and a `searchWord`, check if `searchWord` is a prefix of any word in `sentence`.

Return _the index of the word in_ `sentence` _(**1-indexed**) where_ `searchWord` _is a prefix of this word_. If `searchWord` is a prefix of more than one word, return the index of the first word **(minimum index)**. If there is no such word return `-1`.

A **prefix** of a string `s` is any leading contiguous substring of `s`.

<https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/>

**Example 1:**

> Input: `sentence = "i love eating burger", searchWord = "burg"`
> Output: `4`
> Explanation: `"burg"` is prefix of `"burger"` which is the 4th word in the sentence.

**Example 2:**

> Input: `sentence = "this problem is an easy problem", searchWord = "pro"`
> Output: `2`
> Explanation: `"pro"` is prefix of `"problem"` which is the 2nd and the 6th word in the sentence, but we return `2` as it's the minimal index.

**Example 3:**

> Input: `sentence = "i am tired", searchWord = "you"`
> Output: `-1`
> Explanation: `"you"` is not a prefix of any word in the sentence.

**Constraints:**

- `1 <= sentence.length <= 100`
- `1 <= searchWord.length <= 10`
- `sentence` consists of lowercase English letters and spaces.
- `searchWord` consists of lowercase English letters.

## Test Cases

``` python
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
```

{% asset_code coding/assets/1455-check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/solution_test.py %}

## Thoughts

第一反应是用 Trie 树，但单次搜索就没必要了，不等 Trie 建好就查完了。

因为给定的是一个句子，而非单词的数组，肯定要避免做 split 以节省时间和空间。

直接遍历句子中的每一个字符，在每个空格之后跟 `searchWord` 对齐逐个比对即可。

时间复杂度 `O(n)`，空间复杂度 `O(1)`。

## Code

{% asset_code coding/assets/1455-check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/solution.py %}
