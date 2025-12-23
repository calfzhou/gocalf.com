---
title: Tmux (Terminal Multiplexer)
notebook: notes
tags:
  - it/terminal
date: 2025-11-28 20:32:11
updated: 2025-11-30 00:27:49
references:
  - '[Tmux 使用教程 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2019/10/tmux.html)'
---

## 介绍

Tmux 是一个终端复用器（terminal multiplexer）。

类似的终端复用器还有 GNU Screen（见 [Screen 命令](screen-command.md)）。Tmux 与它功能相似，但是更易用，也更强大。

## 基础知识

命令行的典型使用方式是，打开一个终端窗口（Terminal Window，以下简称「窗口」），在里面输入命令。用户与计算机的这种临时的交互，称为一次「会话」（session）。

会话的一个重要特点是，窗口与其中启动的进程是连在一起的。打开窗口，会话开始；关闭窗口，会话结束，会话内部的进程也会随之终止，不管有没有运行完。

为了解决这个问题，会话与窗口可以「解绑」：窗口关闭时，会话并不终止，而是继续运行，等到以后需要的时候，再让会话「绑定」其他窗口。

Tmux 和 screen 都是会话与窗口的「解绑」工具，将它们彻底分离。

进阶：[Welcome to tao-of-tmux’s documentation! — tao-of-tmux v1.0.2 documentation](https://tao-of-tmux.readthedocs.io/en/latest/)

## 常用命令和快捷键

``` bash
tumx new -s session-name # 新建一个叫 session-name 的会话
tumx detach # 将当前会话与窗口分离
tumx ls # 列出当前所有会话
tumx list-session # 同上
tmux attach -t session-name # 重新接入 session-name 这个会话
tmux switch -t session-name # 切换到名为 session-name 的会话
tmux kill-session -t session-name # 杀死名为 session-name 的会话

tmux split-window # 划分上下两个窗格
tmux split-window -h # 划分左右两个窗格
```

Tmux 的快捷键都要通过前缀键唤起。默认的前缀键是 `Ctrl+b`，即先按下 `Ctrl+b`，快捷键才会生效（类似于 screen 的 `Ctrl+a`？）。

``` text
C-b d -> detach，分离当前会话
C-b s -> ls，列出所有会话
C-b $ -> rename-session，重命名当前会话
```

- `Ctrl+b %`：划分左右两个窗格。
- `Ctrl+b "`：划分上下两个窗格。
- `Ctrl+b <↑↓←→>`：光标切换到其他窗格。
- `Ctrl+b ;`：光标切换到上一个窗格。
- `Ctrl+b o`：光标切换到下一个窗格。
- `Ctrl+b {`：当前窗格与上一个窗格交换位置。
- `Ctrl+b }`：当前窗格与下一个窗格交换位置。
- `Ctrl+b Ctrl+o`：所有窗格向前移动一个位置，第一个窗格变成最后一个窗格。
- `Ctrl+b Alt+o`：所有窗格向后移动一个位置，最后一个窗格变成第一个窗格。
- `Ctrl+b x`：关闭当前窗格。
- `Ctrl+b !`：将当前窗格拆分为一个独立窗口。
- `Ctrl+b z`：当前窗格全屏显示，再使用一次会变回原来大小。
- `Ctrl+b Ctrl+<↑↓←→>`：按箭头方向调整窗格大小。
- `Ctrl+b q`：显示窗格编号。
