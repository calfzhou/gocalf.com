---
title: 2490. Circular Sentence
tags:
- easy
date: "2024-11-27T19:05:55+08:00"
lastmod: "2024-11-27T19:05:55+08:00"
---
## Problem

A **sentence** is a list of words that are separated by a **single** space with no leading or trailing spaces.

- For example, `"Hello World"`, `"HELLO"`, `"hello world hello world"` are all sentences.

Words consist of **only** uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is **circular** if:

- The last character of each word in the sentence is equal to the first character of its next word.
- The last character of the last word is equal to the first character of the first word.

For example, `"leetcode exercises sound delightful"`, `"eetcode"`, `"leetcode eats soul"` are all circular sentences. However, `"Leetcode is cool"`, `"happy Leetcode"`, `"Leetcode"` and `"I like Leetcode"` are **not** circular sentences.

Given a string `sentence`, return `true` _if it is circular_. Otherwise, return `false`.

<https://leetcode.com/problems/circular-sentence/>

**Example 1:**

> Input: `sentence = "leetcode exercises sound delightful"`\
> Output: `true`\
> Explanation: The words in sentence are `["leetcode", "exercises", "sound", "delightful"]`.
>
> - leetcod{{< u text="e" >}}'s last character is equal to {{< u text="e" >}}xercises's first character.
> - exercise{{< u text="s" >}}'s last character is equal to {{< u text="s" >}}ound's first character.
> - soun{{< u text="d" >}}'s last character is equal to {{< u text="d" >}}elightful's first character.
> - delightfu{{< u text="l" >}}'s last character is equal to {{< u text="l" >}}eetcode's first character.
>
> The sentence is circular.

**Example 2:**

> Input: `sentence = "eetcode"`\
> Output: `true`\
> Explanation: The words in sentence are `["eetcode"]`.
>
> - eetcod{{< u text="e" >}}'s last character is equal to {{< u text="e" >}}etcode's first character.
>
> The sentence is circular.

**Example 3:**

> Input: `sentence = "Leetcode is cool"`\
> Output: `false`\
> Explanation: The words in sentence are `["Leetcode", "is", "cool"]`.
>
> - Leetcod{{< u text="e" >}}'s last character is **not** equal to {{< u text="L" >}}eetcode's first character.
>
> The sentence is **not** circular.

**Constraints:**

- `1 <= sentence.length <= 500`
- `sentence` consist of only lowercase and uppercase English letters and spaces.
- The words in `sentence` are separated by a single space.
- There are no leading or trailing spaces.

## Test Cases

```python
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
```

{{< snippet src="solution_test.py" >}}

## Thoughts

直接遍历一遍每个字符，在每个空格处，比较空格前后的字符是否一致。首尾字符单独比较一次。

## Code

{{< snippet src="solution.py" >}}
