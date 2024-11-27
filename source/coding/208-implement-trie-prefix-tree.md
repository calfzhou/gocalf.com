---
title: 208. Implement Trie (Prefix Tree)
notebook: coding
tags:
- medium
date: 2024-11-22 17:59:34
updated: 2024-11-22 17:59:34
---
## Problem

A [**trie**](https://en.wikipedia.org/wiki/Trie) (pronounced as "try") or **prefix tree** is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string `word` into the trie.
- `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
- `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

<https://leetcode.com/problems/implement-trie-prefix-tree/>

**Example 1:**

> Input
> `["Trie", "insert", "search", "search", "startsWith", "insert", "search"]`
> `[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]`
> Output
> `[null, null, true, false, true, null, true]`
>
> Explanation
>
> ``` cpp
> Trie trie = new Trie();
> trie.insert("apple");
> trie.search("apple");   // return True
> trie.search("app");     // return False
> trie.startsWith("app"); // return True
> trie.insert("app");
> trie.search("app");     // return True
> ```

**Constraints:**

- `1 <= word.length, prefix.length <= 2000`
- `word` and `prefix` consist only of lowercase English letters.
- At most `3 * 10⁴` calls **in total** will be made to `insert`, `search`, and `startsWith`.

## Test Cases

``` python
class Trie:

    def __init__(self):


    def insert(self, word: str) -> None:


    def search(self, word: str) -> bool:


    def startsWith(self, prefix: str) -> bool:



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

{% asset_code coding/208-implement-trie-prefix-tree/solution_test.py %}

## Thoughts

就是个树形结构。每个节点保存一个哈希表，key 是字符，value 是下一层节点。为了区分是否完整的单词，最后一个节点的哈希表里加一个特殊的终止字符作为标记。

## Code

{% asset_code coding/208-implement-trie-prefix-tree/solution.py %}
