---
title: Rime 中州韵输入法引擎
notebook: notes
tags:
- software
date: 2024-07-26 21:38:51
updated: 2025-05-18 23:48:03
references:
- '[自由输入法 RIME 简明配置指南 - 少数派](https://sspai.com/post/84373)'
- "[RIME 输入法使用体验 - Hank's Blog](https://zhaohongxuan.github.io/2024/03/20/most-powerful-input-method-rime/)"
- "[Rime 输入法指北 | Jiz4oh's Life](https://jiz4oh.com/2020/10/how-to-use-rime/)"
---
## 基本信息

[RIME | 中州韻輸入法引擎](https://rime.im/)

客户端：

- macOS: [rime/squirrel: 【鼠鬚管】Rime for macOS](https://github.com/rime/squirrel)
  - {% badge_github rime squirrel release:true %}
  - 配置存储路径：`~/Library/Rime`
- iOS: Hamster [仓输入法 on the App Store](https://apps.apple.com/us/app/%E4%BB%93%E8%BE%93%E5%85%A5%E6%B3%95/id6446617683)
  - [欢迎使用「仓输入法」 | 「仓输入法」使用指南](https://ihsiao.com/apps/hamster/docs/)
- Windows: [rime/weasel: 【小狼毫】Rime for Windows](https://github.com/rime/weasel)
  - {% badge_github rime weasel release:true %}
  - 配置存储路径：`%AppData%\Rime` → `C:\Users\<USER>\AppData\Roaming\Rime`
  - ⚠️ 自带的加载三方输入方案的功能有问题，不会拷贝子目录，导致方案无法正常加载。

现成的配置方案：

- ℞ [iDvel/rime-ice: Rime 配置：雾凇拼音 | 长期维护的简体词库](https://github.com/iDvel/rime-ice)
  - {% badge_github iDvel rime-ice release:true %}
  - > 雾凇拼音提供了一套开箱即用的完整配置，包含输入方案（全拼、常见双拼）、长期维护的开源词库及各项扩展功能。
- ℞ [gaboolic/rime-frost: 白霜拼音：蒹葭苍苍，白露为霜](https://github.com/gaboolic/rime-frost)
  - {% badge_github gaboolic rime-frost release:true %}
  - > 白霜拼音使用使用 745396750 字的高质量语料，进行分词，重新统计字频、词频，归一化，打造纯净、词频准确、智能的词库。白霜词库是目前 rime 方案下最好的开源词库，立志于打造不输于商业输入法的输入体验。

> [!tip]
> 关于符号 ℞ 的知识参见 [Medical prescription - Wikipedia](https://en.wikipedia.org/wiki/Medical_prescription)，原本就是用来表示「处方」的。

## 实际使用

### 注意 patch 的用法

[CustomizationGuide · rime/home Wiki](https://github.com/rime/home/wiki/CustomizationGuide)

一定一定注意 `xxx.custom.yaml` 里的 `patch` 是用来覆盖默认配置的，而不是追加的，所以如果要追加，需要把原来的配置也写一遍，或者把 key 写成 `a/b/c` 形式。

比如要自定义一个 color scheme，如果这样写（`squirrel.custom.yaml`）：

``` yaml
patch:
  preset_color_schemes:
    my_scheme:
      background: '#000000'
      foreground: '#ffffff'
```

那么这个配置就只有 `my_scheme`，而没有其他的了，所以应该这样写：

``` yaml
patch:
  'preset_color_schemes/my_scheme':
    background: '#000000'
    foreground: '#ffffff'
```

或者（未验证）：

``` yaml
patch:
  'preset_color_schemes/+':
    my_scheme:
      background: '#000000'
      foreground: '#ffffff'
```

### 管理配置

用「东风破」（plum）进行 Rime 配置管理。

[rime/plum: 東風破 /plum/: Rime configuration manager and input schema repository](https://github.com/rime/plum)
> **東風破** 是 [中州韻輸入法引擎](https://rime.im/) 的配置管理工具。

``` bash
curl -fsSL https://raw.githubusercontent.com/rime/plum/master/rime-install | bash
```

这个操作会：

1. 在执行命令的当前目录，安装 plum，在 `./plum`（实际上就是 `git clone --depth 1`）。
2. 直接更新 Rime 客户端的配置存储目录，安装一系列预设方案，即 `preset-packages.conf` 中的方案，目前有：

- Essentials
- [prelude](https://github.com/rime/rime-prelude): 基礎配置 / the prelude package, providing Rime's default settings
- [essay](https://github.com/rime/rime-essay): 八股文 / a shared vocabulary and language model
- Phonetic-based, Modern Standard Mandarin
- [luna-pinyin](https://github.com/rime/rime-luna-pinyin): 朙月拼音 / Pinyin input method for Traditional Chinese
- [terra-pinyin](https://github.com/rime/rime-terra-pinyin): 地球拼音 / School-taught Pinyin, with tone marks
- [bopomofo](https://github.com/rime/rime-bopomofo): 注音 / Zhuyin (aka. Bopomofo)
- Shape-based
- [stroke](https://github.com/rime/rime-stroke): 五筆畫 / five strokes
- [cangjie](https://github.com/rime/rime-cangjie): 倉頡輸入法 / Cangjie input method

「套装 packages」就是由 conf 文件定义的一组「配方 package」。「配方」又可以包含若干个「输入方案 ℞」或「Rime 配置 ℞」。

或者直接 clone 仓库：

``` bash
git clone --depth=1 https://github.com/rime/plum
```

如果要安装其他方案/配方：

``` bash
cd /path/to/plum/
# bash rime-install [--select] <套装或配方> [<套装或配方>...]
# 如：
bash rime-install gaboolic/rime-shuangpin-fuzhuma@master:recipes/full
```

安装之后，点 squirrel 里的 Deploy，重新部署一下，然后按 ``Ctrl + ` `` 呼出「方案选单」即可选择需要的方案。

想要删除一个方案，直接去配置目录的 `default.custom.yaml`（没有的话就自行创建），通过 `patch.schema_list` 控制需要保留哪些方案，在目录里把对应的配置文件删除，重新部署即可，如：

``` yaml
# default.custom.yaml
patch:
  schema_list:
    - schema: luna_pinyin_simp
```

### Squirrel 样式配置

[LEOYoon-Tsaw/Squirrel-Designer: Squirrel Theme Simulator](https://github.com/LEOYoon-Tsaw/Squirrel-Designer)

[Rime 西米 for Squirrel](https://gjrobert.github.io/Rime-See-Me-squirrel/)

通过工具生成了 theme 设定代码，在 `~/Library/Rime` 里找到 `squirrel.custom.yaml`（没有则自行创建），修改即可。

### 雾凇拼音

[iDvel/rime-ice: Rime 配置：雾凇拼音 | 长期维护的简体词库](https://github.com/iDvel/rime-ice)

通过 `plum` 安装：

``` bash
bash rime-install iDvel/rime-ice:others/recipes/full
```

> [!important]
> 注意这个会修改掉原本的 `default.yaml`。而且也会写入 `squirrel.yaml` 等文件，以更高的版本号覆盖掉客户端内置的配置。

Recipes 里有：

- `full`：全部文件
- `all_dicts`：所有词库文件（包含下面三个）
- `cn_dicts`: 拼音词库文件（ `cn_dicts/` 目录内所有文件）
- `en_dicts`: 英文词库文件（ `en_dicts/` 目录内所有文件）
- `opencc`: opencc（ `opencc/` 目录内所有文件）
- `config:schema=xxxx`: 双拼补丁（会在 `radical_pinyin.custom.yaml` 和 `melt_eng.custom.yaml` 里将 `speller/algebra` 修改为对应的双拼拼写）
  - `flypy`: 小鹤双拼
  - `mspy`: 微软双拼
  - `sougou`: 搜狗双拼
  - `double_pinyin`: 自然码双拼
  - `abc`: 智能 ABC 双拼
  - `ziguang`: 紫光双拼

#### 一些操作技巧

详见 [dotfiles/rime/README.md](https://github.com/calfzhou/dotfiles/blob/master/rime/README.md)

- 数字的各种格式（汉字、人民币大写等）：`R<number>`，如 `R1234.5678`。
- 字母、数字的各种变体：`v<alpha|digit>`，如 `va`、`v1`。
- 其他各种符号：`v<>`，如 `vjt` 各种箭头、`vss` 各种手势 emoji。
- 拆字输入：`uU<各部件拼音>`，如 `uUbuhao` 得到 `孬`。
- 以词定字：输入词组的拼音之后，按 `[` 或 `]` 上屏激活候选项的首字或尾字。
  - 快捷键通过 `default.yaml` 的 `key_binder/select_first_character` 和 `key_binder/select_last_character` 调整。
- Unicode 字符：`Unnnn`（注意 `U` 要大写），如 `U263a`。
- 输入当前日期、时间：`rq` `sj` `xq` `dt` `ts`。
- 公历转阴历：`N<YYYYMMDD>`，如 `N20240726` 得到 `二〇二四年六月廿一` 或 `甲辰年（龙）六月廿一`。

#### 设置中文和英文、数字之间自动加空格

[如何在中英文混合输入情况下，输入后的英文单词前后自动加空格？ · Issue #536 · iDvel/rime-ice](https://github.com/iDvel/rime-ice/issues/536)

效果不太理想，想要类似于搜狗输入法里那样的效果。

### 搜狗输入法用户词库迁移

#### 导出

打开搜狗输入法的设置窗口，点击「我的 → 词库设置 → 中文用户词库 → 导出」，得到词库备份文件，比如叫 `搜狗词库备份_2024_07_26.bin`。

#### 转换

工具：[nopdan/rose: IME User Dictionary Converter. 输入法用户词库转换工具](https://github.com/nopdan/rose)

{% badge_github nopdan rose release:true %}

直接去 releases 中下载最新的版本。注意要下载 `rose.zip` 即预先编译好的二进制程序，还要下载 `data.zip`（目前知道 [v1.3.1](https://github.com/nopdan/rose/releases/tag/v1.3.1) 版本中有）。按照说明把 `data.zip` 解压到 `rose` 目录下。

``` bash
chmod +x rose-darwin-amd64
./rose-darwin-amd64 搜狗词库备份_2024_07_26.bin sogou_bak:rime sougou.dict.yaml
```

可以手动编辑生成的 yaml 文件，删除或调整一些词条。

#### 调整 Rime 词库文件格式

rose 不会自动添加 Rime 词库文件的头部，所以需要手动添加，如：

``` yaml
---
name: sougou
version: '2024.07.26'
sort: by_weight
---
```

#### 引用词库

把上边生成的 `sougou.dict.yaml` 放到 Rime 配置目录下，添加到当前词库的 `import_tables` 中，如：

``` yaml
import_tables:
  - sogou
```

### Lua 脚本

- [Home · hchunhui/librime-lua Wiki](https://github.com/hchunhui/librime-lua/wiki)
- [Scripting · hchunhui/librime-lua Wiki](https://github.com/hchunhui/librime-lua/wiki/Scripting)

四个的关键编程接口：

``` lua
function translator(input, seg, env)
  -- yield Candidate
end

function filter(input, env, cands)
  -- yield Candidate
end

function processor(key_event, env)
  -- return 0 -- kRejected
  -- return 1 -- kAccepted
  -- return 2 -- kNoop
end

function segmentor(segmentation, env)
  -- return true -- 交由下一个 segmentor 处理
  -- return false -- 终止 segmentors 处理流程
end
```

## 多端同步

Rime 客户端里「Sync user data」的同步逻辑是：

- 历史行为数据（动态词频）是双向同步，自动合并
- 用户自定义配置是单向同步，不会下载或合并

可能是因为如果配置文件发生冲突，就必须人工处理，而且不同设备不同系统的配置可能本来也不一样。

用 GitHub 同步配置文件（如 [dotfiles/rime](https://github.com/calfzhou/dotfiles/tree/master/rime)），内置 sync + 云存储（iCloud）同步行为数据。

> Background: macOS 为主电脑（可能多台），iOS 为主移动端（可能多台），Windows 为辅电脑。

### 配置同步

配置文件放在 GitHub 仓库里做版本控制，[dotfiles/rime at master · calfzhou/dotfiles](https://github.com/calfzhou/dotfiles/tree/master/rime)。各端要手动拉取最新代码并部署。

macOS 的 Squirrel：可以直接把仓库目录软链到 `~/Library/Rime`：

``` bash
ln -s $DOTFILES_HOME/rime ~/Library/Rime
```

Windows 的 Weasel：初次安装的时候可以选择数据的存储路径，直接选到仓库所在目录即可。如果已经安装了，也可以再把默认的数据目录改成仓库目录的软链。注意要把 build 等文件和目录从原本的数据目录添加到仓库目录中，否则切换后可能 Weasel 无法使用。

iOS 的 Hamster：一种方式是直接在手机上点开「Wi-Fi 上传方案」，通过电脑浏览器访问，把电脑上仓库目录里的配置文件上传到手机。更方便的方式是开启 iCloud 同步（但不用点「拷贝应用文件至 iCloud」），以后可以通过电脑在 iCloud 里 Hamster 目录（路径是 `~/Library/Mobile Documents/iCloud~dev~fuxiao~app~hamsterapp/Documents`）里的 `RIME/Rime` 子目录中放置所有的配置文件（可以从 GitHub 仓库直接复制过来），然后在 Hamster 里操作「RIME 部署」的时候会自动读取 iCloud 里的配置文件并更新到应用文件目录中。参考 [词库同步 » iCloud 同步 | 「仓输入法」使用指南](https://ihsiao.com/apps/hamster/docs/guides/sync/#icloud-%E5%90%8C%E6%AD%A5) 和 [开启iCloud备份后的使用说明 · imfuxiao/Hamster Wiki](https://github.com/imfuxiao/Hamster/wiki/%E5%BC%80%E5%90%AFiCloud%E5%A4%87%E4%BB%BD%E5%90%8E%E7%9A%84%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E)。

> [!caution]
> 开启 iCloud 同步后，就不要再直接修改应用文件目录中的内容，而是应该修改 iCloud `<Hamster>/RIME/Rime` 目录中的内容。

### 词频数据同步

在各端的 Rime 数据目录里，都会有一个 `installation.yaml` 文件，在文件中添加 `sync_dir` 字段，指向云存储的目录（默认是当前目录）。

iOS 上仓输入法只能访问属于他自己的目录。在应用里进入 RIME 页面，选择同步路径，在 iCloud Drive 里找到 Hamster 目录，可以在里面创建一个目录比如叫 `sync`。该目录在 iOS 里的地址是 `/private/var/mobile/Library/Mobile Documents/iCloud~dev~fuxiao~app~hamsterapp/Documents/sync`，在 macOS 里是 `~/Library/Mobile Documents/iCloud~dev~fuxiao~app~hamsterapp/Documents/sync`。

Windows 上安装 iCloud 客户端，然后找到 `Hamster/sync` 目录的路径，写到 `installation.yaml` 里。

`installation.yaml` 里自动会有 `installation_id` 字段，值是一个 UUID，表示当前设备的唯一标识符。执行 Rime 的数据同步时，会在 `sync_dir` 目录下创建一个 `installation_id` 的子目录，存放当前设备的配置文件和词频数据。

可以把这个值改成统一的 ID，这样不同设备都会读写 `sync_dir` 目录下的同一个子目录，实现多端同步。但受限于云存储的同步机制，可能会导致文件冲突（比如云端的更新还没有同步下来，本地就已经写入的新的内容，导致冲突），越是急着同步反倒越是同步不了。

实际上 Rime 同步的时候，还会检查 `sync_dir` 目录下其他的子目录，如果其他子目录下也有对应的词频数据文件，也是会读取合并进来的。参考 [多设备同步 » 用户词典迁移 | oh-my-rime输入法](https://www.mintimate.cc/zh/guide/deviceSync.html#%E7%94%A8%E6%88%B7%E8%AF%8D%E5%85%B8%E8%BF%81%E7%A7%BB)。另外可以把随机生成的 UUID 改成易懂的值，比如 `mbp-1`、`mbp-2` 等。

比如设备 A 的 `installation_id` 是 `A`，B 的 `installation_id` 是 `B`。设备 A 先同步，其词频数据文件是（`sync_dir` 目录下的）`A/rime_ice.userdb.txt`。设备 B 同步的时候会把 `B/rime_ice.userdb.txt`、`A/rime_ice.userdb.txt` 以及本地 Rime 数据目录里 `rime_ice.userdb` 目录里的信息都合并，然后写入 `B/rime_ice.userdb.txt`，并更新本地 Rime 数据目录里的 `rime_ice.userdb`。

## 其他

### 关于双拼

[也许你该试试双拼输入法 - Hank's Blog](https://zhaohongxuan.github.io/2023/06/30/how-i-learn-shuang-pin/)

推荐：[小鹤双拼](../flypy/index.md)
