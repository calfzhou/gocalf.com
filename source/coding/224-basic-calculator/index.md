---
title: 224. Basic Calculator
notebook: coding
tags:
- hard
date: 2024-12-20 15:07:45
updated: 2024-12-20 15:08:56
---
## Problem

Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return _the result of the evaluation_.

**Note:** You are **not** allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

<https://leetcode.com/problems/basic-calculator/>

**Example 1:**

> Input: `s = "1 + 1"`
> Output: `2`

**Example 2:**

> Input: `s = " 2-1 + 2 "`
> Output: `3`

**Example 3:**

> Input: `s = "(1+(4+5+2)-3)+(6+8)"`
> Output: `23`

**Constraints:**

- `1 <= s.length <= 3 * 10⁵`
- `s` consists of digits, `'+'`, `'-'`, `'('`, `')'`, and `' '`.
- `s` represents a valid expression.
- `'+'` is **not** used as a unary operation (i.e., `"+1"` and `"+(2 + 3)"` is invalid).
- `'-'` could be used as a unary operation (i.e., `"-1"` and `"-(2 + 3)"` is valid).
- There will be no two consecutive operators in the input.
- Every number and running calculation will fit in a signed 32-bit integer.

## Test Cases

```python
class Solution:
    def calculate(self, s: str) -> int:
```

{% asset_code solution_test.py %}

## Thoughts

表达式计算的通用做法是先分词（tokenize），把原始字符串拆成 tokens，一个 token 可能是运算符（包括括号），也可能是一个数字。然后按照运算符的规则构造逆波兰表达式（[Reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)），即数学表达式的后缀表示法。然后基于栈，扫描逆波兰表达式就可以完成计算。

实际上一个表达式可以表示成一个树，叶子节点都是数字，中间节点是运算符。几元运算符就有几个子节点，且子节点的顺序就是该运算符若干个操作数的顺序。

比如表达式 `"(1+(4+5+2)-3)+(6+8)"`，其表达式树是：

::: invert-when-dark
{% diagramsnet case3-tree.drawio %}
:::

逆波兰表达式实际上就是这棵树后序遍历的结果，即：`1, 4, 5, +, 2, +, +, 3, -, 6, 8, +, +`。

因为括号会改变计算的顺序，需要用一个栈来辅助构造逆波兰表达式，这个栈用来缓存需要稍后计算的一些运算符。

- 如果当前 token 是数字，直接输出（相当于最高优先级）。
- 如果当前 token 是左括号 `(`，直接放入 ops 栈（相当于最高优先级），等待匹配到右括号。
- 如果当前 token 是右括号 `)`，则把 ops 栈中第一个左括号之后的运算符都出栈并输出，左括号出栈后丢弃（逆波兰表达式不需要用括号）。
- 如果当前 token 是非括号的运算符，则把 ops 栈中相同或更高优先级的运算符依次出栈并输出（先运算）（但这里隐含了运算符的运算顺序是从左到右的要求），然后将当前运算符放入 ops 栈。
  - 虽然实际上括号的优先级最高，但必须成对使用。相当于左括号在入栈时是最高优先级，但出栈时是最低优先级。可以为左括号设置最低的优先级避免被误出栈。可以近似认为右括号的优先级介于左括号和其他任何运算符之间。
  - 需要注意一下负号，它有两个含义，一个是二元减法运算，一个是一元取反运算。目前的做法是将两种含义区分开，用运算符 `n` 表达一元取反运算。根据前一个 token 可以确定是二元减法还是一元取反。同时要注意一元取反的优先级高于二元减法。
  - 目前的实现有 bug，取反运算符号的运算顺序应该是从右向左的（加减乘除都是从左向右），应该调整出栈的顺序，不过本题的测试用例不涉及这种情况。

扫描的最后，如果 ops 栈不为空，则把里面的运算符依次出栈并输出。

比如上边的表达式 `"(1+(4+5+2)-3)+(6+8)"`，从左到右扫描所有的 tokens：

| token | yields | ops       |
|-------|--------|-----------|
| `(`   |        | `(`       |
| 1     | 1      |           |
| `+`   |        | `( +`     |
| `(`   |        | `( + (`   |
| 4     | 4      |           |
| `+`   |        | `( + ( +` |
| 5     | 5      | `( + ( +` |
| `+`   | `+`    | `( + ( +` |
| 2     | 2      | `( + ( +` |
| `)`   | `+`    | `( +`     |
| `-`   | `+`    | `( -`     |
| 3     | 3      | `( -`     |
| `)`   | `-`    |           |
| `+`   |        | `+`       |
| `(`   |        | `+ (`     |
| 6     | 6      | `+ (`     |
| `+`   |        | `+ ( +`   |
| 8     | 8      | `+ ( +`   |
| `)`   | `+`    | `+`       |
|       | `+`    |           |

可见输出的结果为 `1, 4, 5, +, 2, +, +, 3, -, 6, 8, +, +`。

计算的时候，用一个栈缓存待处理的操作数。如果看到一个数字则入栈。如果看到一个运算符，栈顶的若干个数字就是该运算的操作数（个数取决于运算符的元数），把这些数字出栈然后按照运算符的规则计算出结果，再把结果入栈。

| tokens | calc           | stack  |
|--------|----------------|--------|
| 1 4 5  |                | 1 4 5  |
| `+`    | `4 + 5 = 9`    | 1 9    |
| 2      |                | 1 9 2  |
| `+`    | `9 + 2 = 11`   | 1 11   |
| `+`    | `1 + 11 =13`   | 13     |
| 3      |                | 13 3   |
| `-`    | `13 - 3 = 10`  | 10     |
| 6 8    |                | 10 6 8 |
| `+`    | `6 + 8 =14`    | 10 14  |
| `+`    | `10 + 14 = 24` | 24     |

如果是合法的表达式，最后栈里会只剩下一个数，就是整个表达式的计算结果。

时间复杂度 `O(n)`，空间复杂度 `O(n)`。其中 n 是 s 的长度。

## Code

{% asset_code solution.py %}

比较慢，可能系数太大了。唯一的好处是之后扩展更多的运算符方便一些。

Test cases for solution inner methods:

{% asset_code solution_inner_test.py %}

## Directly

简单点儿的话，本题相当于若干个数字相加，数字的正负号取决于其前边的运算符是 `+` 还是 `-`。括号也比较简单，加号后边的括号可以直接去掉，减号后边的括号去掉的时候，其内部的所有数都相当于要乘以 -1。

可以维护一个栈，记录嵌套的括号累积下来的正负性，用来辅助确定下一个数字的符号。最终把所有数字加起来就行。

{% asset_code solution2.py %}
