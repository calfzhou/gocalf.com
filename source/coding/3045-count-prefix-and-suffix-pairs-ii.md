---
title: 3045. Count Prefix and Suffix Pairs II
notebook: coding
tags:
- hard
date: 2025-01-08 11:21:25
updated: 2025-01-08 11:21:25
---
## Problem

跟 [3042. Count Prefix and Suffix Pairs I](3042-count-prefix-and-suffix-pairs-i) 一模一样，但单词数量从 50 提升到 10⁵，同时单词的长度也从 10 提升到 10⁵。

<https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/>

**Constraints:**

- `1 <= words.length <= 10⁵`
- `1 <= words[i].length <= 10⁵`
- `words[i]` consists only of lowercase English letters.
- The sum of the lengths of all `words[i]` does not exceed `5 * 10⁵`.

## Test Cases

``` python
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
```

{% asset_code coding/assets/3045-count-prefix-and-suffix-pairs-ii/solution_test.py %}

## Thoughts

[3042. Count Prefix and Suffix Pairs I](3042-count-prefix-and-suffix-pairs-i) 的时间复杂度是 `O(k * n²)`。

考虑用 Trie 树来减少重复的比较次数。传统的 Trie 树是前缀树，但本题需要同时满足前缀和后缀。可以对 Trie 树做调整，对于一个单词 word，原本第 i（`0 ≤ i < n`）层的 key 是 `word[i]`，为了能同时匹配前缀和后缀，以元组 `(word[i], word[k-1-i])`（其中 `k = len(word)`）作为 key（实践中可以用长度为 2 的字符串替代元组）。

> Trie 树的实现和相关操作参考 [208. Implement Trie (Prefix Tree)](208-implement-trie-prefix-tree)。

从左到右遍历 words，依次把每个单词加入 Trie 树中，加入过程中，如果当前层的节点对应一个已有的单词，说明该单词是当前正在加入的单词的前后缀，给计数加一。题目没有限制单词不能重复，所以在 Trie 树中需要记录每个单词的次数，对于满足前后缀条件的单词，将该次数累加到计数中。

每个单词加入的时间复杂度是 `O(k)`，总的时间复杂度 `O(k * n)`，空间复杂度 `O(k * n)`。

## Code

{% asset_code coding/assets/3045-count-prefix-and-suffix-pairs-ii/solution.py %}
