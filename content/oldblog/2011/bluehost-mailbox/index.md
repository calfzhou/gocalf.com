---
title: 解决 BlueHost 邮箱无法接收邮件的问题
slug: bluehost-mailbox
date: '2011-07-31T22:04:00+08:00'
lastmod: '2011-08-03T22:33:00+08:00'
tags:
- BlueHost
- Mail Exchanger
categories:
- 建站
summary: 在之前的一篇文章中提到 GoCalf 网站的 Email 部分还没弄好，当时遇到的问题是可以发出邮件，却无法接收邮件。问题根源在于 DNS 没有设置好（空间跟域名来自不同的提供商），今天花了一点儿时间把这个问题解决了。
keywords:
- Hosting
- BlueHost Email
- DNS Manager
- MX
- A 记录
- '@地址'
---

在之前的 [一篇文章](../lets-start/index.md) 中提到 [GoCalf](http://www.gocalf.com/) 网站的 Email 部分还没弄好，当时遇到的问题是可以发出邮件，却无法接收邮件。问题根源在于 DNS 没有设置好（空间跟域名来自不同的提供商），今天花了一点儿时间把这个问题解决了。

我的域名是 [GoDaddy](http://www.godaddy.com) 提供的，而服务器空间则在 [BlueHost](http://www.bluehost.com/) 上，域名解析（DNS）是在 GoDaddy 上进行的。之前已经将二级域名 mail 的 A 记录指向 GoCalf 空间的 IP 地址了，可以登录邮箱，能发出邮件，但怎么都收不到信。在 Gmail（或别的邮件服务器）中给 BlueHost 上的邮件帐户发邮件，会收到无法送达的失败提示：

> Delivery to the following recipient failed permanently:\
>     [xxx@xxxxxxxx\.com](mailto:xxx@xxxxxxxx.com)\
> Technical details of permanent failure:\
> Google tried to deliver your message, but it was rejected by the
> recipient domain\. We recommend contacting the other email provider
> for further information about the cause of this error\. The error
> that the other server returned was: 550 550 \#5\.1\.0 Address rejected
> [xxx@xxxxxxxx\.com](mailto:xxx@xxxxxxxx.com) \(state 14\)\.

看起来应该是 DNS 的问题（跨服务商就是这点比较麻烦啊）。仔细察看了 GoDaddy 上 DNS
Manager 里面的内容，发现 Mail
Exchanger（MX）的配置内容有问题，并没有指向 GoCalf 的空间地址，因此将 MX 记录改为指向 mail\.gocalf\.com。改动大概需要一个小时才能生效，生效之后再次发送邮件就可以在 BlueHost 里收到了。

附 GoDaddy 里面 DNS 设置截图：

{{< image src="godaddy_dns.png" alt="GoDaddy 中 DNS 设置" caption="将二级域名 mail 指向 @ 地址；MX 记录指向 mail.<yourdomain>.com" >}}
