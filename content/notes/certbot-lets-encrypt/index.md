---
title: Certbot 申请 Let's Encrypt SSL 证书
notebook: notes
tags:
- it/web
date: 2024-07-22 16:28:46
updated: 2024-07-22 16:28:46
references:
- '[CentOS7使用Certbot申请Wildcard证书(letsencrypt,nginx) - 知乎](https://zhuanlan.zhihu.com/p/154377608)'
---
## 安装和使用 Certbot

### 直接安装

```bash
# CentOS
sudo yum install certbot python2-certbot-nginx
# macOS
brew install certbot
```

### 用 Docker

```bash
docker pull certbot/certbot
docker run --rm -it certbot/certbot --version
# certbot 2.11.0

mkdir letsencrypt # To persistent certificates.
docker run --rm -it -v ./letsencrypt:/etc/letsencrypt certbot/certbot certonly ...
```

### Docker Compose（Certbot 和 Nginx 一起）

`compose.yaml`:

```yaml
services:
  nginx:
    image: 'nginx'
    restart: always
    environment:
      TZ: Asia/Shanghai
    network_mode: host
    volumes:
      - './nginx.conf:/etc/nginx/nginx.conf:ro'
      - './letsencrypt:/etc/letsencrypt:ro'

  certbot:
    image: 'certbot/certbot'
    profiles:
      - 'certbot'
    volumes:
      - './data/letsencrypt:/etc/letsencrypt'
    entrypoint: 'certbot certonly'
```

通过 `profiles` 避免平时启动 certbot。

申请/更新证书：

```bash
docker compose run --rm certbot certonly ...
```

启动 nginx：

```bash
docker compose up -d
```

证书更新后重新加载：

```bash
# Assume `nginx-nginx-1` is the container name of the nginx service in compose.yaml.
docker exec -it nginx-nginx-1 nginx -s reload
```

## 用 Certbot 申请或更新证书

> 不管用哪种方式运行 Certbot，以下命令中均以 `certbot` 指代。

### 非通配符证书

非通配符证书在申请过程中，会要求在 web 服务器上放一个文件，以验证域名的所有权。文件的访问路径是 `http://example.com/.well-known/acme-challenge/`。

### 通配符证书

通配符证书不支持 HTTP 验证，只能使用 DNS 验证。在申请过程中，会要求添加一个 DNS TXT 记录。

[FAQ: Does Let’s Encrypt issue wildcard certificates? - Let's Encrypt](https://letsencrypt.org/docs/faq/#does-let-s-encrypt-issue-wildcard-certificates)

> Yes. Wildcard issuance must be done via ACMEv2 using the [DNS-01 challenge](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge). See [this post](https://community.letsencrypt.org/t/acme-v2-production-environment-wildcards/55578) for more technical information.

每个域名都要验证一次 DNS，比如 `*.example.com` 和 `example.com` 要验证两次。

```bash
certbot certonly --manual --preferred-challenges dns-01 --server https://acme-v02.api.letsencrypt.org/directory -d example.com -d '*.example.com'
# Are you OK with your IP being logged?
# y
# Before continuing, verify the record is deployed.
# 此处直接回车
# Before continuing, verify the record is deployed.
# 此处加完 DNS TXT 后回车（增加两条 TXT 记录，一个给 example.com 用，一个是给 *.example.com 用的）
```

DNS 更新需要一些时间，在最后按回车键之前，可以先确认 DNS 记录是否生效：

```bash
dig +short -t txt _acme-challenge.example.com
# OR
nslookup -type=txt _acme-challenge.example.com 8.8.8.8
```

### 证书类型

v2 版本的 Certbot 似乎默认使用了 ECC 证书，可以通过 `--key-type rsa` 指定使用 RSA 证书。

> 阿里云负载均衡不支持 ECC 证书。

### 更新证书

证书有效期为 90 天，需要定时更新证书。

之前申请单域名证书，使用 HTTP 验证的时候，直接定期执行 `certbot renew` 即可。

但是通配符证书需要用 DNS 验证，`certbot renew` 没法自动设置 DNS 解析。

TODO: 通过 `--manual-auth-hook` 和 `--manual-cleanup-hook` 参数自动设置 DNS 解析。

[ywdblog/certbot-letencrypt-wildcardcertificates-alydns-au: certbot'renewing letencrypt certificate plugin - automatic verification aliyun/tencentyun/godaddy dns](https://github.com/ywdblog/certbot-letencrypt-wildcardcertificates-alydns-au)

> 目前支持阿里云 DNS、腾讯云 DNS、华为云 NDS、GoDaddy（certbot 官方没有对应的插件）。

## 使用证书

### 证书文件

共四个文件：

- privkey.pem  : 👍 the private key for your certificate.
- fullchain.pem: 👍 the certificate file used in most server software. = `cert.pem` + `chain.pem`
- chain.pem    : used for OCSP stapling in Nginx >=1.3.7.
- cert.pem     : will break many server configurations, and should not be used without reading further documentation.

### Nginx

参考 [NGINXConfig | DigitalOcean](https://www.digitalocean.com/community/tools/nginx)。

证书更新后需要重新加载 Nginx：

```bash
nginx -s reload
```

### 从远程服务器同步证书

假设在远程服务器 host-1 上申请了证书，想要在 host-2 上使用，可以通过 `rsync` 同步。

> `scp` 也可以，但是如果 host-1 禁止 root 登录，而证书文件仅限 root 用户读取，`scp` 会失败。

```bash
rsync -a --rsync-path="sudo rsync" user@host-1:/etc/letsencrypt/archive/example.com .
```
