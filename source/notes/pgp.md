---
title: PGP - Pretty Good Privacy
wiki: notes
menu_id: notes
date: 2024-04-20 11:34:40
updated: 2024-04-20 21:16:54
mermaid: true
references:
  - https://ulyc.github.io/2021/01/13/2021%E5%B9%B4-%E7%94%A8%E6%9B%B4%E7%8E%B0%E4%BB%A3%E7%9A%84%E6%96%B9%E6%B3%95%E4%BD%BF%E7%94%A8PGP-%E4%B8%8A/
  - https://www.rectcircle.cn/posts/understand-and-use-gpg/
  - https://www.lixeon.com/blog/20220621-pgp/
---
{% blockquote Bruce Schneier , - Applied Cryptography %}
There are two kinds of cryptography in this world: cryptography that will stop your kid sister from reading your files, and cryptography that will stop major governments from reading your files.
{% endblockquote %}

## 基本概念

### 名词

- PGP (Pretty Good Privacy): Philip R. Zimmermann 在 1991 年创造的加密信息、保护隐私的商业软件。但现在基本指代 OpenPGP 标准。
- OpenPGP: 与最初 PGP 工具兼容的 IETF 标准。
- GnuPG (Gnu Privacy Guard): 实现了 OpenPGP 标准的自由软件。
  - [The GNU Privacy Guard](https://www.gnupg.org/)
- gpg: GnuPG 的命令行工具。

### 密钥的类型

类型 | 全称 | 缩写
--|--|--
主私钥 | Secret Key | sec
主公钥 | Public Key | pub
子私钥 | Secret Sub Key | ssb
子公钥 | Public Sub Key | sub

### 密钥的用途 Capability

缩写 | 全称 | 说明
--|--|--
C | Certificate | （限主密钥）管理证书，如添加/删除/吊销子密钥/UID，修改过期时间
S | Sign | 签名，如文件数字签名、邮件签名、Git 提交
A | Authenticate | 身份验证，如登录
E | Encrypt | 加密

### 架构

``` mermaid
flowchart LR
  public["公钥\n（主公钥 & 所有子公钥）\n[C][S][A][E]"]
  subgraph private [ ]
    direction TB
    sec["主私钥[C]"]
    ssb_s1["子私钥[S]"]
    ssb_s2["子私钥[S]"]
    ssb_a1["子私钥[A]"]
    ssb_a2["子私钥[A]"]
    ssb_e1["子私钥[E]"]
    ssb_e2["子私钥[E]"]
    sec --- ssb_s1
    sec --- ssb_s2
    sec --- ssb_a1
    sec --- ssb_a2
    sec --- ssb_e1
    sec --- ssb_e2
  end
  revoke[吊销证书]

  public --- sec
  sec --- revoke
```

## 安装 GnuPG

``` bash
brew install gpg
gpg --version
# gpg (GnuPG) 2.4.5
# ...
```

## 密钥管理

{% box color:green %}
注：本文中

- 密钥 = Key，一般指一对公私钥
- 公钥 = Public Key
- 私钥 = Private Key

{% endbox %}

### 生成主密钥

``` bash
gpg --full-generate-key
```

较早的版本 default 算法是 `(1) RSA and RSA`，2.4.x 开始就已经变成 `(9) ECC (sign and encrypt)` 了。

如果选 RSA，建议使用 3072 bits 或者 4096 bits。

不要设置为永久有效。不用担心有效期，在到期前都可以更改。

如果打算使用 PGP 为 git 提交做认证，则要设置跟 git 提交一样的邮箱。

要设置 passphrase，要足够复杂。

### 列出密钥

``` bash
# 列出公钥
gpg -k

# 列出私钥
gpg -K
```

最好创建 `~/.gnupg/gpg.conf` 文件，并输入内容：

``` conf
keyid-format 0xlong
with-fingerprint
```

否则应该在上述命令后边追加两个参数 `--keyid-format long` 和 `--fingerprint`。

### 生成吊销证书

如果不慎失去了对主密钥的掌控（如私钥丢了、密码忘了、被别人拿到了私钥等），可以用吊销凭证对主密钥进行吊销，使其失效。

``` bash
# `revoke.pgp` 是要生成的吊销证书文件名。
gpg --gen-revoke -ao revoke.pgp KEY-ID/UID
```

### 吊销主密钥

可以用吊销证书来吊销主密钥。

``` bash
gpg --import revoke.pgp # 或其他吊销证书文件
```

操作之后再通过 `gpg -k` 或 `gpg -K` 列出密钥，可以看到该证书对应的密钥上会标记 `[revoked]`。

### 添加子密钥

``` bash
gpg --edit-key KEY-ID/UID
# or
gpg --expert --edit-key KEY-ID/UID # 可以生成 A (Authenticate) 用途的子密钥
> addkey
# ...
> save # 重要！否则什么都没变
```

### 删除子密钥

``` bash
gpg --edit-key KEY-ID/UID
> key N # 选择第 N 个密钥（被选中的会标记星号，可以选中多个）
> delkey
# ...
> save
```

### 吊销子密钥

``` bash
gpg --edit-key KEY-ID/UID
> key N # 选择第 N 个密钥（被选中的会标记星号，可以选中多个）
> revkey
# ...
> save
```

### 导出公钥

``` bash
gpg -a [-o public.pub] --export KEY-ID/UID
```

这会导出主公钥和所有的子公钥。

### 导出私钥

``` bash
# 导出主私钥和所有子私钥（不建议）
gpg -a [-o all.pri] --export-secret-keys KEY-ID
# 导出主私钥（要在末尾加感叹号）
gpg -a [-o primary.sec] --export-secret-keys KEY-ID!
# 导出所有子私钥
gpg -a [-o all.ssb] --export-secret-subkeys KEY-ID
# 导出某个指定的子私钥（要在末尾加感叹号）
gpg -a [-o all.ssb] --export-secret-subkeys KEY-ID！
```

### 删除密钥

``` bash
# 删除私钥
gpg --delete-secret-keys KEY-ID/UID
# 删除公钥
gpg --delete-keys KEY-ID/UID
```

### 导入密钥

``` bash
gpg --import <FILE> # 可以是私钥文件，也可以是公钥文件
```

## 最佳实践

### 安全地生成、使用主密钥

最好在断网的机器上生成主密钥，将私钥导出离线保存在全盘加密的 U 盘上，保管好此 U 盘，不作他用。

后续需要使用主私钥时（仅 添加/删除/吊销 子密钥/UID，修改过期时间等），也同样在断网的机器上，通过 U 盘导入主私钥后操作。

注意在机器上要通过 `gpg --delete-secret-keys` 删除已经导出或用毕的主私钥，还需要对磁盘进行清理确保相关信息被彻底抹除。

可以使用 [Tails](https://tails.net/) 操作系统（可能需要用科学的方式访问），做成系统 U 盘或者光盘直接断网运行，它不会在磁盘存储文件信息，省去了擦除私钥的麻烦。

- [Tails - Install Tails from macOS](https://tails.net/install/mac/index.en.html)
- [Tails - Burning Tails on a DVD](https://tails.net/install/dvd/index.en.html)

准备一个 8 GB 的 U 盘或 DVD 刻录盘，用于安装或烧录 Tails 系统。另外准备两个 U 盘，一个用于保存主私钥，存入后就离线保管好，另一个用于保存子私钥，以便导入到正常使用的系统中日常使用。

U 盘上的 Tails 可以直接创建一个加密的持久化存储，详见 [Tails - Persistent Storage](https://tails.net/doc/persistent_storage/index.en.html)。虽然可以但尽量不要在其他系统里操作该持久化存储。

{% box color:red %}
Tails 出于隐私保护等原因，会把系统时区设置为 GMT，导致时间会超前（东半球）或落后（西半球）。

生成的 PGP 密钥在正常的电脑上导入时，可能会报错：

``` text
gpg: key 0xHHHHHHHH was created NNN seconds in the future (time warp or clock problem)
```

可以等几个小时之后再导入……

或者在创建密钥时，把 Tails 系统时区调到地球的另一边（如中国的就把系统时区调成 -8:00）。

Tails 调时区需要输入管理员密码，管理员密码需要在系统刚启动的时候设置，启动之后就无法设置了 [Tails - Administration password](https://tails.net/doc/first_steps/welcome_screen/administration_password/)。
{% endbox %}

### 生成吊销证书并妥善保管

在生成主密钥时，应生成一个吊销证书，并保存在更安全的地方，且最好多保存一份。这是一套密钥的最终兜底。

打印出来存放是个不错的方式，不是很长，需要用到的时候，照着敲一次。

### 绑定 UID

虽然一套密钥可以包含多个 UID（name + email + comment），还是建议为不同的身份创建不同的主密钥，如个人身份、某公司雇员身份应分别使用不同的主密钥。

### 密钥有效期

为每个密钥设置适当的有效期（而不是无限期），在到期前都可以随时调整有效期。

### 加密算法

1. Certificate: RSA 4096 bits / ECC ed25519
2. Encrypt: ECC cv25519 (?)
3. Sign: ECC cv25519 (?) / RSA 3072 bits
4. Authenticate: RSA 3072 bits / ECC cv25519 (?)

### 公布公钥

可以（但不推荐）通过 Key Server 将公钥公布到网络上。或者简单点儿，放在自己所属的网站、GitHub 等地方即可。

{% box color:red %}
有些 Key Server 一旦公布将不能撤销，因此需要注意 UID 是否会泄漏个人隐私。
{% endbox %}

## 使用场景

### Git commit 签名

生成并添加一个仅用于签名（S）的子密钥。

导出公钥，将文本内容配置到 GitHub 账号中 [Managing commit signature verification - GitHub Docs](https://docs.github.com/en/authentication/managing-commit-signature-verification)。TODO: 用子公钥好还是用整体公钥好？

执行 `gpg -k` 获取 S 用途的子密钥的 ID，配置到 git 配置文件中：

``` bash
git config --global user.signingkey SUBKEY-ID
git config --global commit.gpgsign true # 开启默认使用签名（否则需要在 commit 的时候加 `-S` 参数
```

### 签名或验签

用具有 S 用途的子密钥进行签名或验签，用私钥签名，公钥验签。

``` bash
# 签名，输出的文件中同时包含原始文件内容和签名信息。使用自己的私钥。
# `-u` 指定用哪个 USER-ID 进行签名。
gpg -s -o SIGNED-FILE ORIGIN-FILE
# 验签并获取原始文件内容。使用签名者的公钥。
gpg -d -o ORIGIN-FILE SIGNED-FILE

# 签名，输出的文件中同时包含原始文件的原始内容和文本的签名信息。使用自己的私钥。
gpg --clearsign -o SIGNED-FILE ORIGIN-FILE
# 验签方式同上。

# （推荐）签名，只生成签名文件。使用自己的私钥。
gpg -b -o SIGN ORIGIN-FILE # -b = --detach-sign
# 验签，需要同时获取到签名文件和被签名的原始文件。使用签名者的公钥。
gpg --verify SIGN ORIGIN-FILE
```

### 加密或解密文件

用具有 E 用途的子密钥进行文件加密或解密，用公钥加密，私钥解密。

``` bash
# 加密。使用公钥，可以是自己的（以后自己解密），也可以是别人的（发送给对方，对方解密）。
gpg -e -r KEY-ID/UID -o ENCRYPTED-FILE ORIGIN-FILE
# 解密。使用自己的私钥。
# `-u` 指定用哪个 USER-ID 进行解密。
gpg -d -o ORIGIN-FILE ENCRYPTED-FILE
```

如果在加密的同时还要加上签名，可以加 `-s` 参数。解密的时候会同时验证签名。

### 用密码加密或解密文件

即使不生成 PGP 密钥，也可以使用 gpg 命令对文件做加解密。

``` bash
# 加密。执行的时候会提示输入一个加密用的密码。
gpg -c -o ENCRYPTED-FILE ORIGIN-FILE # -c == --symmetric
# 解密。用加密时的密码。
gpg -d -o ORIGIN-FILE ENCRYPTED-FILE
```

### 在公有云上加密保存 git 仓库

把本地仓库推到 GitHub 上，如果是特别敏感的内容，推到 private 仓库也并不安全，可以利用 PGP 密钥结合相关的辅助工具，使得 push 到 GitHub 上面的内容全部都加密过。详情参见 [Git with Encryption](/notes/git-with-encryption)。
