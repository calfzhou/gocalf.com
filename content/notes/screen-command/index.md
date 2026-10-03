---
title: Screen 命令
notebook: notes
tags:
  - it/terminal
date: 2025-11-28 19:53:32
updated: 2025-12-21 20:32:48
references:
  - '[linux screen 命令详解 - David_Tang - 博客园](https://www.cnblogs.com/mchina/archive/2013/01/30/2880680.html)'
---
## 介绍

Screen 可以看作是窗口管理器的命令行界面版本。它提供了统一的管理多个会话的界面和相应的功能。

> 只要 screen 本身没有终止，在其内部运行的会话都可以恢复。这一点对于远程登录的用户特别有用——即使网络连接中断，用户也不会失去对已经打开的命令行会话的控制。只要再次登录到主机上执行 `screen -r` 就可以恢复会话的运行。同样在暂时离开的时候，也可以执行分离命令 `detach`，在保证里面的程序正常运行的情况下让 screen 挂起（切换到后台）。

## 常用参数和快捷键

```bash
screen -S yourname # 新建一个叫 yourname 的 session
screen -US yourname # 新建一个叫 yourname 的 UTF8 编码的 session
screen -ls # 列出当前所有的 session
screen -r yourname # 回到 yourname 这个 session
screen -Ur yourname # 回到 yourname 这个 session（UTF8 编码）
screen -d yourname # 远程 detach 某个 session
screen -d -r yourname # 结束当前 session 并回到 yourname 这个 session
```

在每个 screen session 下，所有命令都以 `Ctrl+a` (C-a) 开始。

```text
C-a d -> detach，暂时离开当前 session，将目前的 screen session (可能含有多个 windows) 丢到后台执行，并会回到还没进 screen 时的状态，此时在 screen session 里，每个 window 内运行的 process（无论是前台/后台）都在继续执行，即使 logout 也不影响。
C-a z -> 把当前 session 放到后台执行，用 shell 的 fg 命令则可回去。
```

```text
C-a ? -> 显示所有键绑定信息

C-a c -> 创建一个新的运行 shell 的窗口并切换到该窗口
C-a n -> Next，切换到下一个 window
C-a p -> Previous，切换到前一个 window
C-a 0..9 -> 切换到第 0..9 个 window
Ctrl+a [Space] -> 由视窗 0 循序切换到视窗 9
C-a C-a -> 在两个最近使用的 window 间切换
C-a x -> 锁住当前的 window，需用用户密码解锁
C-a w -> 显示所有窗口列表
C-a t -> Time，显示当前时间，和系统的 load
C-a k -> Kill window，强行关闭当前的 window
```
