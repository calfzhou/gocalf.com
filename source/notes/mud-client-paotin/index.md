---
title: Mud Client PaoTin++
notebook: notes
tags:
  - software
date: 2025-11-27 23:23:12
updated: 2025-12-01 20:13:37
---
## Info

[mudclient/paotin at beta](https://github.com/mudclient/paotin/tree/beta)

{% badge_github mudclient paotin branch:beta %}

PaoTin++ 是一个基于 [TinTin++](https://github.com/scandum/tintin) 的定制发行版。包括一些尚未被合并进官方 TinTin++ 版本的 patch 和一些基础性的框架代码，企图能够对 TinTin++ 的功能有所增强。

> 特别适合玩儿 [北大侠客行 MUD](https://pkuxkx.net/)。

TinTin++ is a client program specialized to help playing muds: [TinTin++ MUD client](https://tintin.mudhalla.net/index.php)

## Install & Run

立即开始：

```
docker run --rm -it --name tt --hostname tt mudclient/paotin:beta
```

> [!caution]
> `beta` tag 持续在更新，`latest` 很久不更新了。

长期挂机：

``` bash
# 创建游戏主目录，该目录可以自定义
mkdir -p $HOME/my-paotin/

# 创建游戏目录结构
mkdir -p $HOME/my-paotin/{ids,etc,data,log,plugins}

docker pull mudclient/paotin:beta
docker run -d -it --name tt --hostname tt -v $HOME/my-paotin:/paotin/var mudclient/paotin:beta daemon
```

以后每次上线的时候，只需要用下面的命令就可以连接到 UI：

```
docker exec -it tt start-ui

# or
alias paotin='docker exec -it tt start-ui'

paotin
```

用 `Ctrl+a d` 组合键退出游戏。

## Knowledge

- [【Paotin++】入门系列之一: 客户端基础 - 技术园地 - 北大侠客行MUD论坛 - Powered by Discuz!](https://pkuxkx.net/forum/thread-49356-1-1.html)
- [【Paotin++】入门系列之二: 机器基础 - 技术园地 - 北大侠客行MUD论坛 - Powered by Discuz!](https://pkuxkx.net/forum/thread-49375-1-1.html)
- [【Paotin++】入门系列之三: 最常用内置变量,别名。 - 技术园地 - 北大侠客行MUD论坛 - Powered by Discuz!](https://pkuxkx.net/forum/forum.php?mod=viewthread&tid=49451&page=1&extra=#pid552290)
- [【Paotin++】入门系列之四: 最常用内置函数 - 技术园地 - 北大侠客行MUD论坛 - Powered by Discuz!](https://pkuxkx.net/forum/forum.php?mod=viewthread&tid=49456&page=1&extra=#pid552319)
- [【Paotin++】入门系列之五: 事件驱动编程 - 技术园地 - 北大侠客行MUD论坛 - Powered by Discuz!](https://pkuxkx.net/forum/forum.php?mod=viewthread&tid=49406&page=1#pid552034)

## Tips

### 选取和复制文本

按住 Option 键就可以选取了，选取到的文本自动被复制（iTerm2）。

按住 Option + Command 可以矩形选择。

### 窗口管理

[paotin/docs/tmux.md at master · mudclient/paotin](https://github.com/mudclient/paotin/blob/master/docs/tmux.md)

PaoTin++ 用 [Tmux (Terminal Multiplexer)](../tmux/index.md) 管理 UI，切分屏幕，创建多窗口画面，同时挂机多个 ID。PaoTin++ 的 tmux 前缀键已经被修改为 `<Ctrl+a>`。

PaoTin++ 常用的快捷键：

- `<ctrl+a> d` 退出界面，但并不退出游戏。
- `<ctrl+a> -` 横着划一道，将屏幕分成上下两部分。继续按可以继续分。
- `<ctrl+a> |` 竖着划一道，将屏幕分成左右两部分。继续按可以继续分。
- `<ctrl+a> c` 打开一个新窗口。
- `<ctrl+a> 0` 回到 0 号窗口。`<ctrl+a> 1` 回到 1 号窗口。十个数字都可以用。

用 `tmux list-keys` 查看所有的 tmux 快捷键。

- `<ctrl+a> <option+↑>` 或 `<ctrl+a> <option+↑>` 按箭头方向（上或下）调整窗格大小。

TODO: 左右调整窗格大小的快捷键。

### 用单独窗口查看游戏内聊天信息

用 tmux 新开一个 shell（`<ctrl+a> |`），然后在其中输入 `mtail`，即可获得进一步指引：

``` text
用法: mtail <id> [<log1> <log2>...]
日志名称不用加路径和 .log 后缀，只要文件名就好。
可以同时显示多个日志，默认显示日志: chat qq jh helpme fullsk quest job tell
```

Ctrl+N/Ctrl+P 切换，Ctrl+CC 退出。

### 使用 iTerm2 的 `imgcat` 功能

iTerm2 支持直接在终端显示图片（[Images - Documentation - iTerm2 - macOS Terminal Replacement](https://iterm2.com/documentation-images.html)），但在 Tmux 里不太好使。

下载 `imgcat`：

``` bash
curl -O https://iterm2.com/utilities/imgcat
chmod +x imgcat
```

> [!tip]
> 如果是 Docker 版本的 PaoTin++，也可以把 `imgcat` 放到 `/var` 里面使用。

但是在 Tmux 里运行 `imgcat` 无法显示图片。

虽然可以尝试 Python 版本的 `imgcat`：

``` bash
pip install imgcat
python -m imgcat ...
```

但在 Tmux 里也不一定能用。

可以考虑使用 integration mode（参考：[iTerm2 与 Tmux 的集成 - KChen's Blog](https://kchen.cc/2016/11/17/iterm2-and-tmux-integration/)），即 `tmux -CC`。在这里执行 iTerm2 的 `imgcat` 可以显示图片。但在 integration mode 下，tmux 的快捷键失效。不过可以直接用 iTerm2 的分屏功能，还能用鼠标直接改变窗口大小。

想要以 integration mode 运行 PaoTin++：

``` bash
docker exec -it -e TMUXCMD="tmux -CC -S /paotin/tmux/sock" tt start-ui
```

会打开一个新的 Window（或 Tab，取决于 iTerm2 » Settings » General » tmux 里的设置），而执行上述命令的地方会显示：

``` text
正在打开终端...
** tmux mode started **

Command Menu
----------------------------
esc    Detach cleanly.
  X    Force-quit tmux mode.
  L    Toggle logging.
  C    Run tmux command.
Detached
正在连接 UI...
** tmux mode started **

Command Menu
----------------------------
esc    Detach cleanly.
  X    Force-quit tmux mode.
  L    Toggle logging.
  C    Run tmux command.
```

在这里按 ESC 键可以 detach。

## Bot Development

参考 [TinTin++ Manual index](https://tintin.mudhalla.net/manual/)

### HELP load-module

规范的模块加载方法。假设模块名称是 `foo/bar`，则 `load-module foo/bar`。

模块文件查找顺序（如果前面的某个位置找到了，则不再继续查找）：

| No. | File                                        | Description           |
| --- | ------------------------------------------- | --------------------- |
| 1   | `var/mud/$MUD/plugins/foo/bar.tin`          | 玩家为某个 MUD 自定义的特别定制版位置 |
| 2   | `var/plugins/foo/bar.tin`                   | 一般玩家的自定义位置            |
| 3   | `mud/$MUD/plugins/foo/bar.tin`              | MUD 定制版位置             |
| 4   | `plugins/foo/bar.tin`                       | 默认脚本位置                |
| -   |                                             |                       |
| 5   | `var/mud/$MUD/plugins/foo/bar/__init__.tin` | 玩家为某个 MUD 自定义的特别定制版位置 |
| 6   | `var/plugins/foo/bar/__init__.tin`          | 一般玩家的自定义位置            |
| 7   | `mud/$MUD/plugins/foo/bar/__init__.tin`     | MUD 定制版位置             |
| 8   | `plugins/foo/bar/__init__.tin`              | 默认脚本位置                |
| -   |                                             |                       |
| 9   | `var/mud/$MUD/plugins/foo/bar/__main__.tin` | 玩家为某个 MUD 自定义的特别定制版位置 |
| 10  | `var/plugins/foo/bar/__main__.tin`          | 一般玩家的自定义位置            |
| 11  | `mud/$MUD/plugins/foo/bar/__main__.tin`     | MUD 定制版位置             |
| 12  | `plugins/foo/bar/__main__.tin`              | 默认脚本位置                |

其中 `$MUD` 代表当前选择的游戏服务器，可通过 `#var gCurrentMUDLIB` 查看。

### HELP load-file

规范的脚本文件加载方法。假设文件名是 `foo/bar.tin`，则 `load-file foo/bar`。

文件查找顺序（如果前面的某个位置找到了，则不再继续查找）：

| No. | File                       | Description           |
| --- | -------------------------- | --------------------- |
| 1   | `var/mud/$MUD/foo/bar.tin` | 玩家为某个 MUD 自定义的特别定制版位置 |
| 2   | `var/foo/bar.tin`          | 一般玩家的自定义位置            |
| 3   | `mud/$MUD/foo/bar.tin`     | MUD 定制版位置             |
| 4   | `foo/bar.tin`              | 默认脚本位置                |

另外，除了文件的覆盖式重载机制之外，PaoTin++ 还提供了一种文件的继承式修改机制。

即：对于 `foo/bar.tin` 来说，不论最终加载的是前述哪个路径，加载之后，如果发现存在以下文件，则会继续按顺序进行补充式加载：

| No. | File                             | Description           |
| --- | -------------------------------- | --------------------- |
| 1   | `mud/$MUD/foo/bar.extra.tin`     | MUD 定制版位置             |
| 2   | `var/foo/bar.extra.tin`          | 一般玩家的自定义位置            |
| 3   | `var/mud/$MUD/foo/bar.extra.tin` | 玩家为某个 MUD 自定义的特别定制版位置 |


和前面所述重定位方式不同，补充式加载不会中途停止，而是会按上面顺序全部检查一遍路径。最终加载结果类似于将上述文件的内容合并在一起之后的效果。

## Problems

### 反显段落

在 macOS iTerm2 里通过 docker 跑 PaoTin++，房间描述会有这种反显的段落：

![房间描述的异常反显](20251127-231718.png)

解决：换 `beta` 版本（2025-11-27）的 image。
