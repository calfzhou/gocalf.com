---
title: Nintendo Switch
tags:
- hardware
date: "2025-02-10T15:11:35+08:00"
lastmod: "2025-02-10T15:11:35+08:00"
---
## 开机进系统

硬破后，开机会进入 Hekate 系统，然后点击「启动」（Launch）图标，再选择「大气层虚拟系统」，这样用的是双系统。不要用「大气层真实系统」，会在正版系统中留下记录。

「大气层真实系统」是正版系统带了破解功能。「大气层虚拟系统」是正版系统的复制品。两个系统怎么操作都不会影响另外一个系统。

> ❗【真实大气层】是等于直接对真实系统也就是正版系统进行破解，没有任何防 ban 措施，没有特殊需求不要进，不会用的容易被 ban。
> ❗不要在【真实大气层】里面安装任何盗版格式的游戏和工具！即，所有的 NSP、NSZ、XCI 都不要装！就虚拟大气层跟机身正版切换就好了。

## DBI

[Switch DBI 图文使用教程](https://shipengliang.com/games/switch-dbi-%E5%9B%BE%E6%96%87%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B.html)

{{< badge_github user="rashevskyv" repo="dbi" release=true >}}

## Android File Transfer / Open MTP

Mac OS，需安装 [Android File Transfer](https://www.android.com/filetransfer/) 才能通过 USB 往 Switch 里装游戏，但不是特别好使，经常遇到提示无法连接设备，还没找到除了重启之外稳定解决的办法。

> 可以考虑退出 Google Drive、Android File Transfer (`ps -ef | grep -i android`)、Dropbox、OneDrive、Preview 等可能会读取 USB 的应用。

## 游戏安装文件格式

目前看到有几种文件格式：

- nsp: 本体、DLC
- nsz: 补丁、DLC
- xci: 整合

NSP 相当于正版系统数字游戏，不管是大气层系统还是 TX 系统都需要安装一下。在相册第三个英文（安装）点击安装后会安装在桌面。

NSZ 是 Nintendo Switch 游戏的一种新格式，该文件的大小比现时的 NSP 小 40-80％。 简单地说，NSZ 是 NS 游戏的高度压缩包。

XCI 相当于正版的卡带，放在 TF 卡里后，我们破解的 TX 系统可以直接打开运行。而且这个格式是可以整合好最新的补丁让我们不需要安装。打开即玩。

XCI 文件名称代表的一些含义，名称里的 `000` 代表含有本体，而 `V131072` 代表目前整合补丁的版本，最后名称里的 `1G` 代表 1 个本体，`1U` 代表是一个升级补丁。

XCI 格式的游戏需要升级时，也可以通过安装 NSP 补丁达到升级游戏的目的。

- 游戏本体（文件名后缀是 XCI）；
- 升级补丁（文件名结尾带 V + 数字或者带 UPD），补丁安装数字最大的即可；
- DLC（文件名一般都会带 DLC 字样）

NSP 补丁或者 DLC 和 XCI 一起放到内存卡根目录，进入相册按 R 键切换到 INSTALLER 目录，按 A 是安装当前选择的游戏。

## Homebrew App Store for Switch

[Homebrew App Store - ForTheUsers](https://apps.fortheusers.org/switch)

## 游戏时长

{{< badge_github user="tallbl0nde" repo="NX-Activity-Log" release=true >}}

[巨好用的游戏时长工具NX-Activity-Log（含软件和使用方法）](https://www.bilibili.com/read/cv18815639/)

🔔 原始的 repo 很久不更新了，在 16.0.0 固件上有些问题，可以用下面这个 fork：

{{< badge_github user="zdm65477730" repo="NX-Activity-Log" release=true >}}

## 金手指 EdiZon SE

{{< badge_github user="tomvita" repo="EdiZon-SE" release=true >}}

[Switch EdiZon SE 金手指插件使用 图文教程](https://shipengliang.com/games/switch-edizon-se-%E9%87%91%E6%89%8B%E6%8C%87%E6%8F%92%E4%BB%B6%E4%BD%BF%E7%94%A8-%E5%9B%BE%E6%96%87%E6%95%99%E7%A8%8B.html)

下载到的金手指代码文件（txt 文本文件）的存放位置，在存储卡根目录的 `/atmosphere/contents/TID/cheats/BID.txt`，其中 TID 是游戏编号，BID 是版本编号，这两个编号可以再 EdiZon 里看到。

## OVL Loader & 特斯拉菜单

{{< badge_github user="WerWolv" repo="nx-ovlloader" release=true >}}

{{< badge_github user="WerWolv" repo="Tesla-Menu" release=true >}}

The Nintendo Switch overlay menu

> The initial overlay menu to be loaded by nx-ovlloader. It's main purpose is to let the user select other overlays to be loaded. The default directory for overlays is `/switch/.overlays` where only .ovl files (Plain old .nro files renamed to .ovl to differentiate them from normal homebrew) get loaded.

- Tesla consists of three individual parts. nx-ovlloader, the Tesla menu and libtesla.
  - [nx-ovlloader](https://github.com/WerWolv/nx-ovlloader) is basically nx-hbloader ported to run as a sysmodule. It runs in the background and loads overlay NROs (.ovl files) given to it.
  - [Tesla Menu](https://github.com/WerWolv/Tesla-Menu) is the equivalent to the hbmenu. It's the initial thing loaded by nx-ovlloader and acts as a hub for you to select all other overlays.
  - [libtesla](https://github.com/WerWolv/libtesla) is where it becomes interesting for developers. It's an easy to use library that handles layer creation, UI drawing and all the overlay UX. It makes it very easy to create a new overlay for anything
- A frontend for sysmodules that before required either a homebrew or a config file to change settings or used sounds or the LED to give the user feedback.

## Amiibo 模拟 Emuiibo

{{< badge_github user="XorTroll" repo="emuiibo" release=true >}}

Virtual amiibo (amiibo emulation) system for Nintendo Switch

需要借助 nx-ovlloader 和 tesla-menu。

## 更换 TF 卡

硬破之后，自制 payload（Hekate）和自制固件（大气层 Atmosphere）都是保存在 TF 卡上的，要换卡的话需要把原卡克隆到新卡。

参考视频：[破解NS换TF卡太麻烦？这种方法完全无损，超级简单有手就行](https://www.youtube.com/watch?v=DjK_0PBaBKs)。

用到的工具是 [DiskGenius](https://www.diskgenius.com/)，用 [免费版](https://www.diskgenius.com/free.php) 就可以（需要使用 Windows 系统）。（对原卡执行「备份分区到镜像文件」，得到 pmf 文件，再对新卡（先格式化成 exFat 格式）执行「从镜像文件还原分区」即可）。
