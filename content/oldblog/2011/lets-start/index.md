---
title: 要不就先开始吧
slug: lets-start
date: '2011-06-28T23:33:00+08:00'
lastmod: '2011-08-03T20:04:00+08:00'
tags:
- Hosting
- Blog
categories:
- 建站
summary: GoCalf 博客正式开张，顺带介绍一下建站的初始步骤。
keywords:
- BlueHost
- GoDaddy
- MediaWiki
- WordPress
- htaccess
---

像我这种很懒又很挑剔的人，最大的痛苦就是 to\-do
list 越来越长。然则我已经懒到这所谓的 to\-do
list 只是隐约显于心中，并非实际存在。

唯一的避免方法就是尽快行动起来，切不可一再拖拉。

GoCalf 的 blog 和 wiki 就此开张吧。

今天就先记录一下建站的初始步骤：

1. 在 GoDaddy 购买域名，在 BlueHost 购买空间，去 GoDaddy 里把域名的 ip 地址指向 BlueHost 空间。GoDaddy 域名赠送的小空间留作他用。

2. Default web root: ` $HOME/public_html/ `。

3. 在 web root 中 ` mkdir blog `、` mkdir wiki `。

4. 在 cPanel 中开通子域名 blog、wiki，分别指向相应的目录。

5. 在 GoDaddy 中开通相同的子域名指向 A 地址。

6. 在 cPanel 中安装 WordPress、MediaWiki 至相应目录。

7. 在 cPanel 中添加 redirect：

   - blog\.gocalf\.com \-\> gocalf\.com/blog

   - wiki\.gocalf\.com \-\> gocalf\.com/wiki

   - gocalf\.com \-\> www\.gocalf\.com

8. 为防止 web root 混乱：` mkdir <sitename> `，在 ` .htaccess ` 中添加重定向：

   - www\.gocalf\.com/\* \-\> www\.gocalf\.com/\<sitename\>/\$1

9. ` mkdir ~/local ` 作为安装软件目录。

10. 安装 SVN（略去若干字）。

    - ` mkdir ~/public_html/svn `

    - ` svnserve -d -r ~/public_html/svn `

    - 不过现在外部无法访问此 SVN，需要独立 IP 且开放端口

11. 全站禁止 list directory，在 ` .htaccess ` 中添加：` Options -Indexes `，并禁止访问 svn 目录。

12. Setting Email：Not Finished\.

13. 显示中文界面：Not Started\.
