---
title: 2296. Design a Text Editor
notebook: coding
tags:
- hard
date: 2025-02-27 11:32:34
updated: 2025-02-27 11:32:34
---
## Problem

Design a text editor with a cursor that can do the following:

- **Add** text to where the cursor is.
- **Delete** text from where the cursor is (simulating the backspace key).
- **Move** the cursor either left or right.

When deleting text, only characters to the left of the cursor will be deleted. The cursor will also remain within the actual text and cannot be moved beyond it. More formally, we have that `0 <= cursor.position <= currentText.length` always holds.

Implement the `TextEditor` class:

- `TextEditor()` Initializes the object with empty text.
- `void addText(string text)` Appends `text` to where the cursor is. The cursor ends to the right of `text`.
- `int deleteText(int k)` Deletes `k` characters to the left of the cursor. Returns the number of characters actually deleted.
- `string cursorLeft(int k)` Moves the cursor to the left `k` times. Returns the last `min(10, len)` characters to the left of the cursor, where `len` is the number of characters to the left of the cursor.
- `string cursorRight(int k)` Moves the cursor to the right `k` times. Returns the last `min(10, len)` characters to the left of the cursor, where `len` is the number of characters to the left of the cursor.

<https://leetcode.cn/problems/design-a-text-editor/>

**Example 1:**

> Input
> `["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]`
> `[[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]`
> Output
> `[null, null, 4, null, "etpractice", "leet", 4, "", "practi"]`
> Explanation
>
> ``` cpp
> TextEditor textEditor = new TextEditor(); // The current text is "|". (The '|' character represents the cursor)
> textEditor.addText("leetcode"); // The current text is "leetcode|".
> textEditor.deleteText(4); // return 4
> // The current text is "leet|".
> // 4 characters were deleted.
> textEditor.addText("practice"); // The current text is "leetpractice|".
> textEditor.cursorRight(3); // return "etpractice"
> // The current text is "leetpractice|".
> // The cursor cannot be moved beyond the actual text and thus did not move.
> // "etpractice" is the last 10 characters to the left of the cursor.
> textEditor.cursorLeft(8); // return "leet"
> // The current text is "leet|practice".
> // "leet" is the last min(10, 4) = 4 characters to the left of the cursor.
> textEditor.deleteText(10); // return 4
> // The current text is "|practice".
> // Only 4 characters were deleted.
> textEditor.cursorLeft(2); // return ""
> // The current text is "|practice".
> // The cursor cannot be moved beyond the actual text and thus did not move.
> // "" is the last min(10, 0) = 0 characters to the left of the cursor.
> textEditor.cursorRight(6); // return "practi"
> // The current text is "practi|ce".
> // "practi" is the last min(10, 6) = 6 characters to the left of the cursor.
> ```

**Constraints:**

- `1 <= text.length, k <= 40`
- `text` consists of lowercase English letters.
- At most `2 * 10⁴` calls **in total** will be made to `addText`, `deleteText`, `cursorLeft` and `cursorRight`.

**Follow-up:** Could you find a solution with time complexity of `O(k)` per call?

## Test Cases

``` python
class TextEditor:

    def __init__(self):


    def addText(self, text: str) -> None:


    def deleteText(self, k: int) -> int:


    def cursorLeft(self, k: int) -> str:


    def cursorRight(self, k: int) -> str:



# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
```

{% asset_code coding/2296-design-a-text-editor/solution_test.py %}

## Thoughts

算是 [1472. Design Browser History](../1472-design-browser-history/index.md) 的进阶吧，支持的操作更多一些。

开始想着用双向链表，但相对于存储的文本来说，额外的结构开销太大了（速度应该会很快，空间开销大）。

这个 text editor 还是比较局限的，不会把光标随机换到其他地方（只会向左右移动 `O(k)` 距离），那么可以用两个（字符的）数组分别存储光标左边和右边的文字。

添加文本时，直接把新的文字追加到左边的数组末尾即可。删除时也是直接从左边数组的末尾删除。

往左移动光标，意味着左边数组末尾的如干个字符会跑到光标右边，把这些字符从左边数组末尾删除，添加到右边数组的开头。因为在数组开头位置添加内容的开销是 `O(n)`，可以用队列实现，或者右边数组中按逆序存储所有的字符，只需要逆序追加到数组末尾即可。

往右移动光标也是类似，把右边数组开头的若干个字符删除，添加到左边数组的末尾。同样右边数组应该用队列，或者用逆序数组以便可以从末尾删除。

构造方法时间复杂度 `O(1)`，`addText`、`deleteText`、`cursorLeft` 和 `cursorRight` 的时间复杂度都是 `O(k)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/2296-design-a-text-editor/solution.py %}
