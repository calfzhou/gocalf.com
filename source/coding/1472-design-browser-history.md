---
title: 1472. Design Browser History
notebook: coding
tags:
- medium
date: 2025-02-26 10:09:29
updated: 2025-02-26 10:09:29
---
## Problem

You have a **browser** of one tab where you start on the `homepage` and you can visit another `url`, get back in the history number of `steps` or move forward in the history number of `steps`.

Implement the `BrowserHistory` class:

- `BrowserHistory(string homepage)` Initializes the object with the `homepage` of the browser.
- `void visit(string url)` Visits `url` from the current page. It clears up all the forward history.
- `string back(int steps)` Move `steps` back in history. If you can only return `x` steps in the history and `steps > x`, you will return only `x` steps. Return the current `url` after moving back in history **at most** `steps`.
- `string forward(int steps)` Move `steps` forward in history. If you can only forward `x` steps in the history and `steps > x`, you will forward only `x` steps. Return the current `url` after forwarding in history **at most** `steps`.

<https://leetcode.cn/problems/design-browser-history/>

**Example 1:**

> Input:
> `["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]`
> `[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]`
> Output:
> `[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]`
> Explanation:
>
> ``` cpp
> BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
> browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
> browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
> browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
> browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
> browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
> browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
> browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
> browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
> browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
> browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
> ```

**Constraints:**

- `1 <= homepage.length <= 20`
- `1 <= url.length <= 20`
- `1 <= steps <= 100`
- `homepage` and `url` consist of  '.' or lower case English letters.
- At most `5000` calls will be made to `visit`, `back`, and `forward`.

## Test Cases

``` python
class BrowserHistory:

    def __init__(self, homepage: str):


    def visit(self, url: str) -> None:


    def back(self, steps: int) -> str:


    def forward(self, steps: int) -> str:



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
```

{% asset_code coding/assets/1472-design-browser-history/solution_test.py %}

## Thoughts

用数组记录访问历史，用一个变量 `current` 记录当前访问的是历史记录中的哪一条。前进和后退的时候就增减这个记录值（处理好边界）。

访问新地址的时候，`current` 右边的原有历史记录全部失效，先对 `current` 自增，然后把新地址存入 `current` 对应的数组位置。当然如果 `current` 自增前就已经是数组的最右，则需要把新地址添加到数组末尾。如果 `current` 右边还有很多空间，可以不用直接释放掉，而是用另一个变量记录当前有效的历史记录数量，减少内存分配的波动（用 Python 可能不太需要自行处理这个）。

构造方法时间复杂度 `O(1)`，`visit` 方法时间复杂度平均为 `O(1)`，`back` 和 `forward` 方法时间复杂度 `O(1)`。空间复杂度 `O(n)`。

## Code

{% asset_code coding/assets/1472-design-browser-history/solution.py %}
