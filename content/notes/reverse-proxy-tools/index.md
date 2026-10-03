---
title: 反向代理（内网穿透）工具
notebook: notes
tags:
  - it/network
  - software
date: 2024-05-21 23:00:26
updated: 2024-05-21 23:00:26
---
## frp

{% badge_github fatedier frp release:true %}

> frp is a fast reverse proxy to help you expose a local server behind a NAT or firewall to the Internet. As of now, it supports TCP and UDP, as well as HTTP and HTTPS protocols, where requests can be forwarded to internal services by domain name.
>
> frp 是一个专注于内网穿透的高性能的反向代理应用，支持 TCP、UDP、HTTP、HTTPS 等多种协议。可以将内网服务以安全、便捷的方式通过具有公网 IP 节点的中转暴露到公网。

- {% mark ？ color:yellow %} 重量级/功能强/需要配置
  - 目前在用，一般场景配置挺简单的
- {% mark ✓ color:green %} 支持多种传输协议
- {% mark ✓ color:green %} 老牌工具
- {% mark ✓ color:green %} 客户端自带多种插件，如 socks 代理、http 代理等
  - socks 代理 +1
- {% mark ✗ color:red %} 必须有自己部署的服务端

[Full configuration file for frps (Server)](https://github.com/fatedier/frp/blob/dev/conf/frps_full.ini)

[Full configuration file for frpc (Client)](https://github.com/fatedier/frp/blob/dev/conf/frpc_full.ini)

[CentOS 7 安装配置frp内网穿透服务器端教程 - 腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1808601)

```bash
brew install frps
brew install frpc

brew services list | grep frp
```

## bore

{% badge_github ekzhang bore release:true %}

> A modern, simple TCP tunnel in Rust that exposes local ports to a remote server, bypassing standard NAT connection firewalls. **That’s all it does: no more, and no less.**

- {% mark ？ color:yellow %} 新工具
- {% mark ✓ color:green %} 非常简单（像 ngrok）
- {% mark ✓ color:green %} 有免费的服务端 bore.hub，也可以部署自己的服务端
- {% mark ✓ color:green %} 任何 tcp 协议均可

```bash
brew install ekzhang/bore/bore
bore local 8080 --to bore.pub
#> listening at bore.pub:45865

# Or, run in docker directly.
docker run -it --init --rm --network host ekzhang/bore local 8080 --to bore.pub
```

## Ngrok

[ngrok - Online in One Line](https://ngrok.com/)

> ngrok is the programmable network edge that adds connectivity, security, and observability to your apps with no code changes.
>
> ngrok is a globally distributed reverse proxy fronting your web services running in any cloud or private network, or your machine.

Reverse proxy that creates a secure tunnel from a public endpoint to a locally running web service.

- {% mark ✓ color:green %} 快速试用很方便
- {% mark ✓ color:green %} 支持 TLS、TCP tunnels
- {% mark ✗ color:red %} 贵，免费版只能体验一下，很慢，不稳定

可免费使用，for quick demos。常规版本是 $25 / month。

```bash
brew install ngrok/ngrok/ngrok
ngrok authtoken <token> # Get token after login
ngrok http 80 # To map which port
```

启动后，会在终端显示出服务状态，包括从外网访问的域名信息（免费版本每次的域名随机）。

```text
ngrok by @inconshreveable

Session Status                online
Account                       Your Name (Plan: Free)
Version                       2.3.40
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://8887-114-242-180-2.ngrok.io -> http://localhost:8080
Forwarding                    https://8887-114-242-180-2.ngrok.io -> http://localhost:8080

Connections                   ttl     opn     rt1     rt5     p50     p90
                              6       0       0.03    0.02    5.41    7.50
```

如果要转发的是非 HTTP 类的端口，比如 22 端口：

```bash
# On local machine:
ngrok tcp 22
# Check screen output for forwarding info.

# On another machine outside the local network:
ssh USER@NNN.tcp.ngrok.io -p PORT
```

## nps

{% badge_github ehang-io nps release:true %}

> NPS is a lightweight, high-performance, powerful intranet penetration proxy server, with a powerful web management terminal.
>
> nps是一款轻量级、高性能、功能强大的内网穿透代理服务器。目前支持tcp、udp流量转发，可支持任何tcp、udp上层协议（访问内网网站、本地支付接口调试、ssh访问、远程桌面，内网dns解析等等……），此外还支持内网http代理、内网socks5代理、p2p等，并带有功能强大的web管理端。

- {% mark ✗ color:red %} 很久未更新
- {% mark ✓ color:green %} 轻量级
