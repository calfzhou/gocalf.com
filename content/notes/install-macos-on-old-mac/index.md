---
title: 给 Mac 老机器装新的 macOS
date: 2026-10-19T23:10:59+08:00
lastmod: 2026-10-19T23:10:59+08:00
tags:
  - software/mac
---
## macOS Patcher

[dosdude1's Personal Web Server - Software](https://dosdude1.com/software.html)

这个网站提供了 macOS Sierra 到 Catalina 的 patcher，easy-to-use tool that allows anyone to install macOS VERSION on unsupported Macs.

安装了之后，可能会遇到 chrome 等软件无法运行的问题：

[Chrome crashes before opening in Mac Os Catalina - Google Chrome Community](https://support.google.com/chrome/thread/95128075?hl=en&msgid=95294466)

> That was a bug affecting third-part applications on old Macs using patches to run Catalina, several - not only Chrome - programs were affected, displaying codesign errors.
>
> Run that on terminal: `sudo nvram boot-args=amfi_get_out_of_my_way=0x1`
> Reboot, life is good again.

[macOS 10.15 Catalina on Unsupported Macs | Page 383 | MacRumors Forums](https://forums.macrumors.com/threads/macos-10-15-catalina-on-unsupported-macs.2183772/page-383?post=28325409#post-28325409)

> I have just released version 1.3.6 of Catalina Patcher, which should fix the issue where some third-party applications wouldn't launch. If you have been having this issue, you can either use the latest Catalina Patcher version, or run `sudo nvram boot-args=amfi_get_out_of_my_way=0x1` in Terminal, and then reboot.
