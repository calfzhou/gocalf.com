---
title: Epson L4166 打印机变砖修复
notebook: notes
tags:
  - hardware
date: 2024-05-21 23:40:41
updated: 2024-05-21 23:40:41
references:
  - '[爱普生EPSON L4168 固件在线更新失败修复方法 - 知乎](https://zhuanlan.zhihu.com/p/293894725)'
  - '[Espon L4166 "Printer Mode"成功修复记（2022-04-04） - 知乎](https://zhuanlan.zhihu.com/p/492703200)'
---
爱普生 Epson L416x 喷墨打印机，联网之后，可能是因为自动更新固件，一更新就会变砖（进入 Printer Mode）无法使用。

## 故障情况

开机后显示屏黑屏，显示

``` text
Printer Mode

Set Jig

Push [OK] BT
```

按一下 OK 键，变为红屏，显示

``` text
Flag Check

Inspection:
ON

Initial Charge:
OFF

Push [Power] BT
```

之后就只能关机了，再打开也一样。

## 临时修复

参考：[爱普生EPSON L4168 固件在线更新失败修复方法 - 知乎](https://zhuanlan.zhihu.com/p/293894725)

1. 关闭打印机。
2. 按住主页键（小房子图标），然后同时按住开机键，保持同时按下不松手，屏幕背光亮起也不松手，知道出现模式选择界面。
3. 选择 `4. Normal Mode`。

缺点：

- 每次开机都得用同样的方式操作，否则依然会进入 Printer Mode。
- 第一次临时修复操作完，所有以前的设置都会丢失，语言变为日文，需要手动更改语言，设置 wifi 信息。
- 电脑需要重新添加打印机，型号会变成 ET-2750 之类的。
- Cloud Print 可能会失效（我刚临时修复完还能用，过了几天不行了，重新注册也总是失败）。

## 繁琐但目前看比较完美的修复方法

参考：[Espon L4166 "Printer Mode"成功修复记（2022-04-04） - 知乎](https://zhuanlan.zhihu.com/p/492703200)

需要借助 Windows 系统的电脑，用 USB 线连接打印机和电脑。提前准备几个工具：

- Epson L416x 清零软件（[寂寞的电风扇](https://www.zhihu.com/people/zhengdukai) 提供）
  - [EpsonL416x清零软件.zip | 百度网盘](https://pan.baidu.com/s/1H5q3sqCTZ5IVkDsCzbmsRQ?pwd=8888)
    - 已经保存到我的百度网盘 `Soft/Epson` 目录
  - 压缩包里有个 word 文档，里面包含两大块，最好先通读一遍
- 官方固件升级包
  - [L416x固件升级软件](https://www.epson.com.cn/Apps/tech_support/GuideDriveContent.aspx?ColumnId=31678&ArticleId=44776)
  - 实测过的版本是 2020-07-14 发布的 LW20K4

### 一、将坏固件清零

打印机和电脑连接，开机进入 Printer Mode，用清零软件文档里第一大块（清零操作）执行即可。

### 二、刷「清零软件」中的固件

用清零软件文档里第二大块（刷 ecc 原始固件）操作。

注意文档里 Initial setting 的截图放的位置太靠下了，容易误解，应该是在文档中第 3 步那里。

这步操作完之后，打印机型号恢复为 L4166，但打印出来的文档会有重影。

### 三、刷官方固件（版本号：LW20K4）

按上边知乎的文章操作，运行官方下载的固件升级包（软件）。

### 四、在线升级最新固件

电脑里之前添加打印机时大概率安装了 Epson Software Updater，运行它执行固件升级。

之后在打印机上操作一下「打印头校准」。

修复之后，Cloud Print 设置成功。

PS：做过几次打印头校准，多清洗几次喷头，重影问题没能完全消除，但一般情况看起来还好。

PPS：喷墨打印机真不好用。Epson 喷墨打印机真垃圾。
