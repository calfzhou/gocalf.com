---
title: 770. Basic Calculator IV
notebook: coding
tags:
- hard
date: 2024-12-20 19:15:33
updated: 2024-12-20 19:15:33
---
## Problem

Given an expression such as `expression = "e + 8 - a + 5"` and an evaluation map such as `{"e": 1}` (given in terms of `evalvars = ["e"]` and `evalints = [1]`), return a list of tokens representing the simplified expression, such as `["-1*a","14"]`

- An expression alternates chunks and symbols, with a space separating each chunk and symbol.
- A chunk is either an expression in parentheses, a variable, or a non-negative integer.
- A variable is a string of lowercase letters (not including digits.) Note that variables can be multiple letters, and note that variables never have a leading coefficient or unary operator like `"2x"` or `"-x"`.

Expressions are evaluated in the usual order: brackets first, then multiplication, then addition and subtraction.

- For example, `expression = "1 + 2 * 3"` has an answer of `["7"]`.

The format of the output is as follows:

- For each term of free variables with a non-zero coefficient, we write the free variables within a term in sorted order lexicographically.
  - For example, we would never write a term like `"b*a*c"`, only `"a*b*c"`.
- Terms have degrees equal to the number of free variables being multiplied, counting multiplicity. We write the largest degree terms of our answer first, breaking ties by lexicographic order ignoring the leading coefficient of the term.
  - For example, `"a*a*b*c"` has degree `4`.
- The leading coefficient of the term is placed directly to the left with an asterisk separating it from the variables (if they exist.) A leading coefficient of 1 is still printed.
- An example of a well-formatted answer is `["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"]`.
- Terms (including constant terms) with coefficient `0` are not included.
  - For example, an expression of `"0"` has an output of `[]`.

**Note:** You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2³¹, 2³¹ - 1]`.

<https://leetcode.com/problems/basic-calculator-iv/>

**Example 1:**

> Input: `expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]`
> Output: `["-1*a","14"]`

**Example 2:**

> Input: `expression = "e - 8 + temperature - pressure", evalvars = ["e", "temperature"], evalints = [1, 12]`
> Output: `["-1*pressure","5"]`

**Example 3:**

> Input: `expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []`
> Output: `["1*e*e","-64"]`

**Constraints:**

- `1 <= expression.length <= 250`
- `expression` consists of lowercase English letters, digits, `'+'`, `'-'`, `'*'`, `'('`, `')'`, `' '`.
- `expression` does not contain any leading or trailing spaces.
- All the tokens in `expression` are separated by a single space.
- `0 <= evalvars.length <= 100`
- `1 <= evalvars[i].length <= 20`
- `evalvars[i]` consists of lowercase English letters.
- `evalints.length == evalvars.length`
- `-100 <= evalints[i] <= 100`

## Test Cases

```python
class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
```

{% asset_code solution_test.py %}

## Thoughts

系列题：

- [224. Basic Calculator](../224-basic-calculator/index.md) 加减、括号、取反符号
- [227. Basic Calculator II](../227-basic-calculator-ii/index.md) 加减乘除

本题主要是引入了自变量，相当于多项式的符号运算。

先用类似于 [224. Basic Calculator](../224-basic-calculator/index.md) 和 [227. Basic Calculator II](../227-basic-calculator-ii/index.md) 的方式，对表达式字符串做分词并构建逆波兰表达式。

微调 `tokenize` 方法，支持自变量的识别和输出。

微调 `reverse_polish` 方法，保留括号和加减乘运算符，增加对定值自变量的处理（对于给了值的自变量，直接换成值）。

计算的时候，把数字或自变量都构造成（只有一项的）多项式（[polynomial](https://en.wikipedia.org/wiki/Polynomial)）。多项式就是若干个项（[term](https://en.wikipedia.org/wiki/Addition#Terms)）的数组。

实现多项式的 [加法、减法](https://en.wikipedia.org/wiki/Polynomial#Addition_and_subtraction) 和 [乘法](https://en.wikipedia.org/wiki/Polynomial#Multiplication) 运算（这些运算的结果都需要做简化，也就是数学上的合并同类项）。

不考虑合并同类项的话，几个运算的逻辑其实很简单：

- 加法 `a + b`：直接把两个多项式中的所有项放到一个数组里即可。
- 减法 `a - b`：相当于 `a + (-b)`，把 b 中所有项的系数取反，再跟 a 中所有项放到一个数组里。
- 乘法 `a * b`：a 和 b 中所有项的笛卡尔积。

合并同类项的操作是把所有项按次数从高到低排序，相同次数的项按项中自变量的字典顺序排列（每个项里的自变量都是按字典顺序排列的）。排序后，相邻的两个项，如果自变量完全一致，就可以合并成一个，二者的系数相加即可。如果系数为 0，则直接删掉。

## Code

{% asset_code solution.py %}

Test cases for solution inner methods: [solution_inner_test.py](solution_inner_test.py)。

一个小的优化是可以用字典来表示一个多项式，key 是已经排序的自变量元组，value 是系数。可以省去合并同类项时候的排序时间。只需要在输出最终计算的时候对 key 排序一次即可，不过在本题限定的规模下没什么区别。代码参见 [solution2.py](solution2.py)。
