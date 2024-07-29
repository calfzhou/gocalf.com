---
title: Rime 中州韵输入法引擎
notebook: notes
tags:
- software
date: 2024-07-26 21:38:51
updated: 2024-07-29 16:40:58
references:
- '[自由输入法 RIME 简明配置指南 - 少数派](https://sspai.com/post/84373)'
- "[RIME 输入法使用体验 - Hank's Blog](https://zhaohongxuan.github.io/2024/03/20/most-powerful-input-method-rime/)"
- '[Rime 输入法指北 | Jiz4oh's Life](https://jiz4oh.com/2020/10/how-to-use-rime/)'
---
## 基本信息

[RIME | 中州韻輸入法引擎](https://rime.im/)

客户端：

- [rime/squirrel: 【鼠鬚管】Rime for macOS](https://github.com/rime/squirrel)
  - {% badge_github rime squirrel release:true %}
  - 配置存储路径：`~/Library/Rime`
- iOS: Hamster（仓）

现成的配置方案：

- ℞ [iDvel/rime-ice: Rime 配置：雾凇拼音 | 长期维护的简体词库](https://github.com/iDvel/rime-ice)
  - {% badge_github iDvel rime-ice release:true %}
- ℞ [gaboolic/rime-shuangpin-fuzhuma: 墨奇音形，打造最强双拼辅助码rime输入方案](https://github.com/gaboolic/rime-shuangpin-fuzhuma)
  - {% badge_github gaboolic rime-shuangpin-fuzhuma release:true %}
  - > 重磅发布：墨奇音形，支持自然码、小鹤、搜狗、微软双拼。墨奇音形是一个基于字形描述信息、递归拆分，最后取首末双形音托的码表开源的方案。详见 [墨奇码拆分规则](https://github.com/gaboolic/rime-shuangpin-fuzhuma/wiki/%E5%A2%A8%E5%A5%87%E7%A0%81%E6%8B%86%E5%88%86%E8%A7%84%E5%88%99)。[墨奇码](https://github.com/gaboolic/moqima-tables) 的拆分码表已开源，目前已经拆分完成全部的通用规范汉字、常用繁体字，总计支持 4 万字（方案选单中支持大字集和小字集切换）。未来准备支持 gb18030-2022 标准的 8 万字。墨奇音形的方案支持 ctrl+p 开关显示墨奇辅助码 + 首末字形，ctrl+l 开关显示墨奇拆字的拆分。
  - > 重磅发布 2：现在词库独立演进维护，改为使用 745396750 字的高质量语料，进行分词，重新统计字频、词频，归一化的 [白霜词库](https://github.com/gaboolic/rime-frost)，白霜词库是目前 rime 方案下最好的词库，在不使用智能模型的情况下可以超越使用智能模型的词库方案。

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

> Squirrel 皮肤设计软件

不用这个也可以，直接在 `~/Library/Rime` 里找到 `squirrel.custom.yaml`（没有则自行创建），修改即可。

### 雾凇拼音

[iDvel/rime-ice: Rime 配置：雾凇拼音 | 长期维护的简体词库](https://github.com/iDvel/rime-ice)

通过 `plum` 安装：

``` bash
bash rime-install iDvel/rime-ice:others/recipes/full
```

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

## 其他

### 关于双拼

[也许你该试试双拼输入法 - Hank's Blog](https://zhaohongxuan.github.io/2023/06/30/how-i-learn-shuang-pin/)

> 这个推荐「[小鹤双拼 flypy](https://flypy.com/)」。
> 小鹤的零声母方案把韵母的首字母当作声母 ：
> 单字母韵母，零声母 + 韵母所在键，如： 啊＝aa 哦=oo 额=ee
> 双字母韵母，零声母 + 韵母末字母，如： 爱＝ai 恩=en 欧=ou
> 三字母韵母，零声母 + 韵母所在键，如： 昂＝ah
> 小鹤方案更加符合直觉，虽然需要记忆，但是要比其他方案顺手。

官方的记忆口诀：[小鹤入门](https://flypy.cc/)
