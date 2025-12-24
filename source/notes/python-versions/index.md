---
title: Python 各版本变化
notebook: notes
tags:
  - it/python
date: 2024-05-15 23:17:06
updated: 2024-05-15 23:17:06
references:
  - '[Python各版本的差异总结\_python版本-CSDN博客](https://blog.csdn.net/qq_35952638/article/details/103101820)'
---
## Python 3.12 in 2023

[Python Release Python 3.12.0 | Python.org](https://www.python.org/downloads/release/python-3120/)

- f-string 增强。
  - 花括号 `{}` 内：可以包含担任定界符的引号；可以嵌套多层 f-string；可以换行和加注释；可以包含反斜杠 `\` 进行转义。
- 简化定义泛型的语法。
- 可以用 type 关键字定义类型别名，如 `type Point = tuple[float, float]`。
- 在 Python 进程中创建子 Python 解释器时，可以让每个解释器不共享同一个 GIL。

## Python 3.11 in 2022

[Python Release Python 3.11.0 | Python.org](https://www.python.org/downloads/release/python-3110/)

- CPython 解释器优化，比 3.10 快 10~60%。
- 增加 BaseExceptionGroup 和 ExceptionGroup，用于将多个异常打包为一组。需要使用 `except*` 捕捉。
- 打印 tracebacks 信息时，可以准确指出引发异常的代码位置。

## Python 3.10 in 2021

[Python Release Python 3.10.0 | Python.org](https://www.python.org/downloads/release/python-3100/)

- match-case 模式匹配（类似于 switch-case）。
  - [8.6. The `match` statement](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement)
  - [PEP 636 – Structural Pattern Matching: Tutorial](https://peps.python.org/pep-0636/)
  - [PEP 634 – Structural Pattern Matching: Specification](https://peps.python.org/pep-0634/)
  - [17. Structural Pattern Matching | Python Tutorial](https://python-course.eu/python-tutorial/structural-pattern-matching.php)

``` python
match <expression>
    case <pattern>:
        <block>
    case <pattern>:
        <block>
```

- 用 `|` 运算符连接多个类型，表示 Union 类型。

``` python
isinstance(x, int | str)
```

- `open()` 支持参数 `encoding='locale'`，等价于 `encoding=None`，表示用当前平台默认编码。

## Python 3.9 in 2020

[Python Release Python 3.9.0 | Python.org](https://www.python.org/downloads/release/python-390/)

- dict 增加运算符 `|` 和 `|=`。
- str 增加 `removeprefix()` 和 `removesuffix()`。
- 支持将大部分内置类型的类名用作函数实参。
  - [PEP 585 – Type Hinting Generics In Standard Collections](https://peps.python.org/pep-0585/)

``` python
def func(x: dict[str, list[int]]):
    pass
```

## Python 3.8 in 2019

[Python Release Python 3.8.0 | Python.org](https://www.python.org/downloads/release/python-380/)

- 增加赋值表达式 `:=`，用于给表达式中的变量赋值。
- 增加语法：定义函数时，在正斜杆 `/` 之前的参数都会被视作位置参数。
  - [PEP 570 – Python Positional-Only Parameters](https://peps.python.org/pep-0570/)
- 在 f 字符串中用 `变量=` 的格式打印变量的值，方便于调试。

## Python 3.7 in 2018

[Python Release Python 3.7.0 | Python.org](https://www.python.org/downloads/release/python-370/)

- 增加 Data Classes.
  - Data Classes can be thought of as “mutable namedtuples with defaults”.
  - [dataclasses — Data Classes](https://docs.python.org/3/library/dataclasses.html)
  - [PEP 557 – Data Classes](https://peps.python.org/pep-0557/)

## Python 3.6 in 2016

[Python Release Python 3.6.0 | Python.org](https://www.python.org/downloads/release/python-360/)

- dict 中的元素会按插入顺序存储。
- 在数字中插入下划线作为分隔符，提高可读性。

``` python
>>> 1_000_111_000
1000111000
>>> '{:_}'.format(1000000) # 格式化字符串时也可输出下划线
'1_000_000'
```

- 给字符串加上前缀 f 之后，就会执行花括号 `{}` 内的语句。
- 给类定义 `__init_subclass__()` 方法，用于初始化子类。

``` python
class TestBase:
    subclasses = []

    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)
        cls.subclasses.append（cls）
```

- 增加标准库 `secrets`，用于生成安全的随机数。

## Python 3.5 in 2015

[Python Release Python 3.5.0 | Python.org](https://www.python.org/downloads/release/python-350/)

- 扩展了迭代拆包运算符 `*`、字典拆包运算符 `**` 的语法。
- 增加关键字 `async`、`await`，用于定义协程。
- 增加类型注释（type annotations）。
  - 对于函数，可以用冒号 `:` 添加形参的注释，用 `->` 添加返回值的注释。这些注释会存储在函数的 `__annotations__` 属性中。
  - 对于变量，可以用冒号 `:` 添加注释。
- 增加标准库 `typing` ，定义了一些类型，常用于类型注释。
- 增加标准库 `zipapp` ，用于将 Python 脚本打包成可执行的归档文件，扩展名为 `.pyz` 。
  - [zipapp — Manage executable Python zip archives](https://docs.python.org/3/library/zipapp.html)
  - 可以把源代码打成 zip 压缩包，直接用 Python 运行。可以把依赖的扩展也都打进来。但使用者还是需要本地安装了适当版本的 Python 才能运行。

## Python 3.4 in 2014

[Python Release Python 3.4.0 | Python.org](https://www.python.org/downloads/release/python-340/)

- 采用 `pip` 作为 Python 包的默认安装方式。
- 增加标准库 `pathlib`，用于按面向对象的方式操作文件路径。
  - [pathlib — Object-oriented filesystem paths](https://docs.python.org/3/library/pathlib.html)
  - [Correspondence to tools in the `os` module](https://docs.python.org/3/library/pathlib.html#correspondence-to-tools-in-the-os-module)
- 增加标准库 `enum`，用于定义枚举类。
- 增加标准库 `asyncio`，用于实现异步 IO。
  - [asyncio — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- 增加标准库 `statistics`，提供了求平均值、中位数、方差等运算的函数。
  - [statistics — Mathematical statistics functions](https://docs.python.org/3/library/statistics.html)
- 增加标准库 `tracemalloc`，用于跟踪内存分配的情况，方便调试。

## Python 3.0 in 2008

[Python 3.0 Release | Python.org](https://www.python.org/download/releases/3.0/)

## Python 2.7 in 2010

[Python Release Python 2.7.0 | Python.org](https://www.python.org/downloads/release/python-270/)

这是 Python 2 的最后一个子版本。
