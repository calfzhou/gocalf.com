---
title: 在苹果系统上打造舒服的开发环境
slug: make-mac-better-for-development
date: '2014-07-26T11:00:00+08:00'
lastmod: '2014-07-26T11:00:00+08:00'
tags:
- Mac Develop
- Homebrew
categories:
- 程序开发
summary: 对 Mac OS X 做一番处理，使之更加适合程序开发。
keywords:
- Mac OS X
- iTerm
- Solarized Color
- Homebrew
- goagent
- python
- virtualenv
- GNU
- coreutils
- bash prompt
- dircolors
- vim
- Sublime Text
- git
- git flow
- svn
- hostname
- maven
- develop environment
---

用苹果系统已经有一段时间了，越来越喜欢这个系统，不管是一般的使用、做设计、做开发，都非常适合。最近也对系统做了一些调整，使得开发环境更加的舒服，记录下来，免得忘了。

实际的过程是漫长而曲折的，跟下面所写的顺序完全没有关系。如果按照下面的步骤操作，中间难免会遇到一些问题（大多是由于墙导致的），那时再自行 Google 吧。

## 基础设施

### iTerm

对于几乎离不开 shell 的开发者来说，一款优秀的终端程序是基础的基础。

毫无疑问，我用的是 [iTerm2](http://www.iterm2.com/)。如果说访问互联网世界的入口是 Chrome，那么访问程序世界的入口就是 iTerm 了。

{{< image src="iterm2_logo.png" alt="iterm2_logo" caption="" >}}

字体选择一款好看的等宽字体即可，比如常用的 Consolas、 Curier New 等。我用的是 [Source Code Pro](https://github.com/adobe/source-code-pro)。中文使用 Microsoft YaHei 字体。

配色当然首选 [Solarized](https://github.com/altercation/solarized) 的暗色系，在 Github 上可以找到专门提供给 iTerm2 用的配色文件 [Solarized Dark\.itemcolors](https://github.com/altercation/solarized/blob/master/iterm2-colors-solarized/Solarized%20Dark.itermcolors)。

### Homebrew

[Homebrew](http://brew.sh/) installs the stuff you need that Apple didn\'t\.

我电脑上的大部分工具都是通过 homebrew 安装和管理的，非常方便。虽然提供类似功能的还有 [Fink](http://www.finkproject.org/) 和 [macports](http://www.macports.org/)，但我认为 Homebrew 是最方便的。具体的就不在这里比较了，大家可以自行调研。当然，至少选择一个来帮助自己安装盒管理软件包，会让很多事情变得更容易。

安装 Homebrew 非常方便，首先要安装 [Command Line Tools for Xcode](https://developer.apple.com/downloads/index.action)，然后运行

```bash {linenos=false}
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
```

在使用 Homebrew 的过程中，要注意经常更新它。在 brew 的世界中，24 小时就已经是非常久了。所以在安装某个包或者做其他操作之前，一般都要运行 ` brew update ` 和 ` brew doctor `，前者用于更新 Homebrew 自身和各个软件包，后者用于排查可能会遇到的问题。我之前没注意这个（也是因为那时候还没太依赖于 Homebrew），有一次安装一个程序，总是提示我有一个依赖没有装，但那个依赖明明就在那儿，百思不得其解，还跑到 github 上发 issue 去问，被拍了一顿。其实只要 brew update 一下就知道，我安装的那个依赖包太老了，升级了就好了。

在安装某个程序前，我一般也要先 ` brew info $FORMULA ` 一下看看，了解一下有没有什么值得注意的参数，安装后有什么需要手动进行的后续操作。

Homebrew 默认会掌控系统中的 ` /usr/local ` 目录，目前我这个目录也就只是给 Homebrew 用了，其他的东西都不往里放。在使用 Homebrew 的过程中，一般都避免使用 sudo 进行操作，实际上现在的版本用了 sudo 也就没法使了。

### Python

苹果系统自带了好几个版本的 Python，装在 /Library/Python 中。不过版本都不新，为了便于维护，还是自己装一个 Python 吧。用 ` brew install python ` 可以安装最新的 Python 2\.x，用 ` brew install python3 ` 可以安装最新的 Python 3\.x。

Homebrew 的 Python 已经安装了 pip，用于管理 Python 的软件包。根据 ` brew info python ` 提供的提示，运行下列命令对 pip 进行更新：

```bash {linenos=table}
pip install --upgrade setuptools
pip install --upgrade pip
```

我现在使用 [virtualenv](http://virtualenv.readthedocs.org/en/latest/) 来管理 Python 的环境，用 [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) 来方便地使用 virtualenv。分别用 pip 进行安装：

```bash {linenos=table}
pip install virtualenv
pip install virtualenvwrapper
```

virtualenvwrapper 提供了很多方便的命令，还支持命令的 tab completion，这些都包含在 virtualenvwrapper\.sh 文件中。在 ` ~/.bash_profile ` 中引入该文件来激活相关的命令和功能：

```bash {linenos=table}
export VIRTUAL_ENV_DISABLE_PROMPT=1
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/projects
[ -f "/usr/local/bin/virtualenvwrapper.sh" ] && source "/usr/local/bin/virtualenvwrapper.sh"
```

准备好后就可以用 ` mkvirtualenv ENVNAME ` 来创建一个新的 virtualenv，用 ` workon ` 命令来切换环境，用 ` deactive ` 退出虚拟环境。更多的命令可以查看 [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) 的文档。

另外，[ipython](http://ipython.org/) 是非常好用的 Python 的交互式终端，比 Python 自身的命令行提供了更丰富和方便的功能，建议使用。通过 ` pip install ipython ` 即可安装。不过目前我还没想清楚要不要把它装在某个虚拟环境中。按理说应该是要在任何一个虚拟环境中都能用 ipython 的，否则就要给每个虚拟环境都装一次，岂不是很浪费空间？这个问题以后再考虑吧。

ipython 除了 shell console 外，还提供 Qt console，详细的信息查看官方的介绍吧。

## 友好的 Shell

有了 iTerm 还不够，要让 shell 变得好用，还需要再做一些配置。

### Bash Profile

` ~/.bash_profile ` 的作用就不用我多说了，在这里可以对 shell 进行很多的个性化配置。参考 [mathiasbynens 的 dotfiles](https://github.com/mathiasbynens/dotfiles) 项目，我也为自己打造了舒适的 shell 环境，相关的配置保存在 [GitHub \- calfzhou \- dotfiles \- bash](https://github.com/calfzhou/dotfiles/tree/master/bash) 里面，对 Mac 和 Linux 都是可以的，让我在不同的服务器上也有相同的操作体验。涉及到的内容很多，就不逐一介绍了，比较重要的几点下面会提到。

### Dir Colors

虽然 iTerm 本身已经设置好了 Solarized 配色，但是 ls 的时候并不一定有颜色。ls 没有颜色绝对是让人难以忍受的，在 [bash\_inc/alias](https://github.com/calfzhou/dotfiles/blob/master/bash/bash_inc/aliases) 里除了根据系统中 ls 支持的参数让 ls 的输出显示出颜色外，还通过配置 ` LS_COLOR ` 让色彩更丰富，可以让不同类型的文件有不同的颜色，看起来非常的清晰。推荐使用 [dircolors\-solarized](https://github.com/seebi/dircolors-solarized) 提供的配色文件，在 Mac OS X 的采用了 Solarized Dark 配色的 iTerm2 里看起来会是这个样子：

{{< image src="dircolors_solarized_dark.png" alt="dircolors-solaized-dark" caption="iTerm2 中 Solarized Dark 系的 dircolors 效果" >}}

### Bash Prompt

在使用 shell 的过程中，命令提示符会一直陪伴着我们，是时候扔掉默认的提示符了。[我的命令提示符](https://github.com/calfzhou/dotfiles/blob/master/bash/bash_inc/bash_prompt) 用不同的颜色分别显示出当前时刻、当前用户、当前主机（通过颜色标识是否通过是通过 SSH 登录的）、当前使用的 Python virtualenv（如果有的话）、当前目录、当前目录所在的 git 分支和状态（如果是 git 项目的目录的话）。

关于主机名，Mac 系统下默认应该是 localhost，可以通过 scutil 命令修改成想要的值：

```bash {linenos=table}
$ sudo scutil --set HostName MYNAME
$ hostname
MYNAME
```

配合上 iTerm 的配色、ls 的颜色等，我的 shell 看起来是这样的：

{{< image src="my-shell-demo.png" alt="my-shell-demo" caption="我的 iTerm2 的效果" >}}

### Bash Completion

在 shell 里面输入命令的时候，如果只记得开头几个字母，后面的记不清楚了也没关系，输入几个字母后，按 TAB 键就可以自动补全或者提示出所有可行的命令。在输入文件名的时候也可以通过 TAB 键自动补全或者提示出有效的文件文来，这个功能是非常方便的。Homebrew 又额外提供了一些 bash completion 功能，可以通过 ` brew install bash-completion ` 进行安装，并会生成 ` /usr/local/etc/bash_completion ` 文件，在 ` ~/.bash_profile ` 中 source 一下这个文件，就可以把 Homebrew 提供的命令补全包含进来。如果通过 Homebrew 安装了别的工具包，比如 git、svn 等，它们也会有各自相应的命令补全文件，存放在 ` /usr/local/etc/bash_completion.d ` 目录中，都会被刚才那个文件自动引入。

### Shell Commands

用惯了 Linux（CentOS）里面的 shell 命令，就无法忍受 Mac 系统中那些落后的 shell 命令了，像 ls、date、ps、echo、grep 等等，功能都特别少。在忍无可忍之后，终于决定用 [GNU Coreutils](http://www.gnu.org/software/coreutils/) 替换它们。用 ` brew install coreutils ` 就可以搞定了，安装完成后，根据提示，将 ` /usr/local/opt/coreutils/libexec/gnubin ` 和 ` /usr/local/opt/coreutils/libexec/gnuman ` 分别添加到 ` $PATH ` 和 ` $MANPATH ` 中即可。

grep 命令不在 coreutils，可以通过 ` brew install grep --default-names ` 搞定（如果说找不到 grep 可以先 ` brew tap homebrew/dupes `）。当然还有很多其他特别有用的命令，就不一一细说了，反正想到什么，只要用 ` brew info ` 或者 ` brew search ` 找找看就行。

## 编辑器和 IDE

### VIM

其实我也不是 VIM 重度使用者，现在写超过两个文件的 Python 代码、Java 代码等都会使用专门的 IDE。我看很多人都喜欢用 VIM 来写复杂的项目代码，但他们的 VIM 都没有做任何额外的设置，自身对 VIM 的快捷键和命令也不熟悉，只是把 VIM 当成一个连移动光标都很费劲的编辑器来用，写代码的效率可想而知。而且像 Python 这种脚本语言，很多错误只有到运行到那句话的时候才会有效果，VIM 没有足够的只能针对某一个语言做太多的静态分析。

` ~/.vimrc ` 用于对 VIM 进行各种设置，如果没有这个文件，赶紧创建一个吧。复杂的语法高亮、配色、插件等都可以放在 ` ~/.vim ` 里面。VIM 自身对插件没有很好地管理，我选择了 [vim\-pathogen](https://github.com/tpope/vim-pathogen) 来管理所需要的 VIM 扩展。只要把 [pathogen\.vim](https://github.com/tpope/vim-pathogen/blob/master/autoload/pathogen.vim) 放在 ` ~/.vim/autoload ` 目录中，把所需的扩展包放在 ` ~/.vim/bundle ` 目录下即可。

同样地，我也把自己的 VIM 设置和依赖放在 GitHub 上（[GitHub \- calfzhou \- dotfiles \- vim](https://github.com/calfzhou/dotfiles/tree/master/vim)），在别的 server 上直接 clone 下来保持一致的操作体验。

我现在使用 [riv\.vim](https://github.com/Rykka/riv.vim) 扩展来写 reStructuredText 文件（\.rst），操作起来非常方便。

如果不满意苹果系统自带的较低版本的 VIM，或者想用 GUI 界面的 VIM，可以利用 Homebrew 进行安装，Formula 是 ` vim ` 和 ` macvim `。

### Sublime Text

[Sublime Text](http://www.sublimetext.com/) 是我现在主要使用的 GUI 编辑器，但看其首页的动画演示就会觉得非常 cool。以前还经常用 Ultra Edit 和 Notepad\+\+，现在基本都不用了。在 GUI 程序中，我一般会使用 Solarized Light 配色方案，总感觉大部分 GUI 程序用暗色系就很丑（PyCharm 系列除外）。

具体的配置也就不多说了。注意 Sublime Text 原生不支持 GBK 编码的文件，需要安装扩展包，即使这样，在编辑 GBK 编码的文件时，它会生成一个临时文件进行操作，保存的时候再写回去，体验上还是有些不爽。

还有一个地方我也一直没搞清楚，就是中文字体不是刚刚好跟两个英文字母一样宽。在编辑 reStructuredText 文件的时候，还是会比较麻烦的。

### Python IDE

以前一直用 VIM 做 Python 开发，是因为没找到好用的 Python IDE，现在我用 [JetBrains](http://www.jetbrains.com/) 出的 [PyCharm](http://www.jetbrains.com/pycharm/)。不要跟我争，这绝对是世界上最好用的 Python IDE，没有之一。

PyCharm 里强烈推荐自带的 Darcula 配色，感觉在 GUI 界面中，这个配色比 Solarized Dark 要舒服一些。PyCharm 的默认配置基本就很好用了，它对 Python 代码的可读性检测方面要求还是比较严格的，空行、空格不合适都会有提示。如果 Python 项目中包含其他类型的文件（如 shell 脚本、html 页面等），它也有相应的插件可以对这些文件进行语法高亮。

一直觉得如果 JetBrains 出一个通用的编辑器，应该能把 Sublime Text 甩出好几条街去。

### Java IDE

好多人都用 Eclipse 写 Java 代码（包括 Android 开发），真想不通为什么那么难用的 IDE 还那么受欢迎。可能学校里交 Java 的时候都用的 Eclipse 吧，就像直到现在都还有很多人用 VS6 做 C\+\+ 开发一样。对于 Android 开发，可能跟之前 Google 推 Eclipse with ADT 有关吧。不过现在 Google 也认识到了 Eclipse 的不足，转身投入 [JetBrains](http://www.jetbrains.com/) 的 [IntelliJ IDEA](http://www.jetbrains.com/idea/) 的怀抱了。JetBrains 出品的个个都是精品啊，微软里面很多项目组也都在使用 JetBrains 出的 [ReSharper](http://www.jetbrains.com/resharper/)。

我现在也是用 IntelliJ IDEA 来做 Java 开发，使用体验跟 PyCharm 类似。Java 项目的依赖管理用 Maven，Homebrew 里也提供了安装。建议目前使用 Maven 3\.0\.\*：

```bash {linenos=table}
brew tap homebrew/versions
brew install maven30
```

当然如果要用最新的 3\.2\.\*，可以直接 ` brew install maven `。

## 版本控制

### Git

用 Homebrew 可以方便地安装最新的 Git。如果像上面介绍的那样，用 Homebrew 安装并使用了 bash\-completion，那么装好 git 后，git 指令也会按 TAB 键补全了，再也不动担心记不住 git 指令。

` ~/.gitconfig ` 可以用来定义很多个性化的设置，可以直接编辑或者通过 ` git config --global ` 进行设置。类似的，我也把我的配置文件保存在 GitHub 上（[GitHub \- calfzhou \- dotfiles \- git](https://github.com/calfzhou/dotfiles/tree/master/git)），以便在不同的地方有同样的操作体验。

顺便提一下，用 git 管理项目版本的话，推荐使用 [git\-flow](https://github.com/nvie/gitflow) 管理分支和版本，通过 Homebrew 可以直接安装它，同样也会带有 TAB 自动补全功能。关于这种分支管理的模型，可以阅读 [A successful Git branching model](http://nvie.com/posts/a-successful-git-branching-model/)。

如果想在公开的 git 仓库中保存一些比较隐私的信息，可以利用 [git\-encrypt](https://github.com/shadowhand/git-encrypt) 来加密其中的一部分文件。这个也可以直接通过 Homebrew 安装。大致的介绍在之前的文章 [用 Git 和云存储保存隐私信息](../../2013/git-encrypt/index.md) 中略有介绍。

如果还想用个 GUI 的 Git 客户端，我用的是 [GitX\-dev](http://rowanj.github.io/gitx/)，主要用来直观地观察分支的演化情况。

{{< image src="gitx-dev.png" alt="gitx-dev" caption="GitX-dev 界面演示" >}}

### SVN

用了 Git，就再也不想用 SVN 了。不过有时候也难免会需要用，用 Homebrew 安装个新版本的 SVN 吧，同样也会有 TAB 键补全哦。
