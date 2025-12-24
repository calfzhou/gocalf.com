---
title: 大改站点的目录结构
date: 2025-12-24 20:10:17
---
## 「升级」引发的折腾

前几天把 [Stellar](https://xaoxuu.com/wiki/stellar/) 主题从 1.30.0 升级到 1.33.1。然后发现所有的笔记页内的图片都不显示了。

因为之前笔记页的 URL 格式是 `https://gocalf.com/notes/<note-slug>`，升级之后变成了 `https://gocalf.com/notes/<note-slug>/`，末尾多了「斜线」。而图片的相对路径是基于当前页面地址计算的，所以图片路径都错了。

> 参见 [opt: pretty\_url · xaoxuu/hexo-theme-stellar@fd21ccd](https://github.com/xaoxuu/hexo-theme-stellar/commit/fd21ccd89c50a3bdb96b0e1b50b342089519f493)。

自己之前也没注意，原来博客文章的 URL 是末尾带斜线的，而笔记页的地址没有斜线。感觉不太统一。

本来按我的习惯，文章和笔记页的 URL 末尾应该没有斜线，因为斜线代表「目录」，而不是「文件」。但我看主流的博客系统（比如 Hexo、Hugo）都是默认带斜线的。而且 Stellar 主题从 1.33.0 也「强制」带斜线了。

问了问 Copilot，被它说服了：

> Most blogs treat pages as directories.
>
> Static site generators (Hugo, Jekyll), many CMSs (WordPress), and many web servers default to:
>
> `/about/` → directory → index.html inside it
>
> This makes URLs with `/` more natural and predictable.

我决定随大溜，统一改成末尾带斜线的格式。而且发现现在的一些独立页面就已经是末尾带斜线的，因为它们的源文件一般是 `source/<page-slug>/index.md` 这种目录结构。这个结构还有一个天然的好处，就是可以放置该页面相关的资源文件在同一目录下，更加整洁。

## 重构目录结构

于是我决定把笔记页的源文件也改成这种目录结构。也就是把 `source/notes/<note-slug>.md` 改成 `source/notes/<note-slug>/index.md`。

让 AI 帮忙写了几个脚本来批量处理这些文件，凑活能用。

``` python move_markdown_files.py
import os

def move_and_rename_markdown_files(base_dirs):
    for base_dir in base_dirs:
        for file in os.listdir(base_dir):
            if file.endswith('.md'):
                old_path = os.path.join(base_dir, file)
                new_dir = os.path.join(base_dir, file[:-3])
                new_path = os.path.join(new_dir, 'index.md')

                os.makedirs(new_dir, exist_ok=True)
                os.rename(old_path, new_path)
                print(f"Moved: {old_path} -> {new_path}")

if __name__ == "__main__":
    base_dirs = ["notes", "coding"]
    move_and_rename_markdown_files(base_dirs)
```

``` python move_assets.py
import os
import shutil

def move_assets(base_dirs):
    for base_dir in base_dirs:
        assets_dir = os.path.join(base_dir, 'assets')
        if not os.path.exists(assets_dir):
            continue

        for slug in os.listdir(assets_dir):
            slug_dir = os.path.join(assets_dir, slug)
            if os.path.isdir(slug_dir):
                target_dir = os.path.join(base_dir, slug)
                if os.path.exists(target_dir):
                    for asset in os.listdir(slug_dir):
                        asset_path = os.path.join(slug_dir, asset)
                        if os.path.isfile(asset_path):
                            shutil.move(asset_path, target_dir)
                            print(f"Moved: {asset_path} -> {target_dir}")

if __name__ == "__main__":
    base_dirs = ["notes", "coding"]
    move_assets(base_dirs)
```

``` python update_markdown_links.py
import os
import re

def update_internal_links(base_dirs):
    link_patterns = [
        re.compile(r'(?<!!)\[(.*?)\]\((?!http|https|/|#)(.*?\.md)(#.*?)?\)'),  # Matches slug.md#fragment
        re.compile(r'(?<!!)\[(.*?)\]\((?!http|https|/|#)([^.#)]+)(#.*?)?\)')   # Matches slug#fragment without extension
    ]

    for base_dir in base_dirs:
        for slug in os.listdir(base_dir):
            slug_dir = os.path.join(base_dir, slug)
            if os.path.isdir(slug_dir):
                for file in os.listdir(slug_dir):
                    if file.endswith('.md'):
                        file_path = os.path.join(slug_dir, file)

                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()

                        for pattern in link_patterns:
                            content = pattern.sub(
                                lambda match: f"[{match.group(1)}](../{match.group(2).split('.')[0]}/index.md{match.group(3) or ''})",
                                content
                            )

                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)

                        print(f"Updated links in: {file_path}")

if __name__ == "__main__":
    base_dirs = ["notes", "coding"]
    update_internal_links(base_dirs)
```

还有一些可以直接在 VS Code 里用正则批量替换的，就没再让 AI「帮忙」写脚本了。

## 博客文章的文件路径

博客文章页的处理机制就不太一样，虽然源文件的路径是 `source/_posts/<year>/<post-slug>.md`，但按照现在配置，构建出来的 HTML 页面路径是 `.../<post-slug>/index.html`。这也是之前发现的，用 VS Code 等编辑器编辑源文件时，图片的相对路径不好处理的原因。

试图把博客文章的源文件也改成 `source/_posts/<year>/<post-slug>/index.md` 这种目录结构，但这就得把资源文件放在 `source/_posts/<year>/<post-slug>/index/<index>/` 目录下，否则就会被丢弃，暂时没办法。参见 [How to put post Markdown file into asset folder? · Issue #3245 · hexojs/hexo](https://github.com/hexojs/hexo/issues/3245)。
