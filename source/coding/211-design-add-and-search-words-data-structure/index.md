---
title: 211. Design Add and Search Words Data Structure
notebook: coding
tags:
- medium
date: 2024-11-22 23:09:07
updated: 2024-11-22 23:09:07
---
## Problem

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:

- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds `word` to the data structure, it can be matched later.
- `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

<https://leetcode.com/problems/design-add-and-search-words-data-structure/>

**Example 1:**

> Input
> `["WordDictionary","addWord","addWord","addWord","search","search","search","search"]`
> `[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]`
> Output
> `[null,null,null,null,false,true,true,true]`
> Explanation
>
> ``` cpp
> WordDictionary wordDictionary = new WordDictionary();
> wordDictionary.addWord("bad");
> wordDictionary.addWord("dad");
> wordDictionary.addWord("mad");
> wordDictionary.search("pad"); // return False
> wordDictionary.search("bad"); // return True
> wordDictionary.search(".ad"); // return True
> wordDictionary.search("b.."); // return True
> ```

**Constraints:**

- `1 <= word.length <= 25`
- `word` in `addWord` consists of lowercase English letters.
- `word` in `search` consist of `'.'` or lowercase English letters.
- There will be at most `2` dots in `word` for `search` queries.
- At most `10⁴` calls will be made to `addWord` and `search`.

## Test Cases

``` python
class WordDictionary:

    def __init__(self):


    def addWord(self, word: str) -> None:


    def search(self, word: str) -> bool:



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```

{% asset_code coding/211-design-add-and-search-words-data-structure/solution_test.py %}

## Thoughts

[208. Implement Trie (Prefix Tree)](../208-implement-trie-prefix-tree/index.md) 里的 trie 树正好适合这个问题。

在原来的 `search` 方法上增加模糊匹配的功能。即如果 `word` 当前的字符是 `.` 就遍历所有的子树。

> 为了避免混淆， 把 trie 标识单词结束的符号换成 `#` 了（[Problem 208](../208-implement-trie-prefix-tree/index.md) 中用的是 `.`）。

直接用递归写就比较简单。

也可以用栈加循环避免递归。

## Code

### Recursively

{% asset_code coding/211-design-add-and-search-words-data-structure/solution.py %}

### Non-recursively

{% asset_code coding/211-design-add-and-search-words-data-structure/solution2.py %}

> 刻意将非递归方法写的跟递归的处理逻辑能对应上，可以注意从递归改为非递归时所做的调整。实际上就是树的深度优先遍历，这里将 `node` 设置为 `None` 来标识路径已经结束，可以从栈里弹出其他待处理的节点。
