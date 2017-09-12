## CLI

[CLI](https://en.wikipedia.org/wiki/Command-line_interface) 是一个与 [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface) 相对的概念，指不依靠图形界面，使用命令直接与计算机对话。

学习 CLI 有什么好处呢？给你贴两段话：

> If you want to learn to code, then you must learn this(CLI). Programming languages are advanced ways to control your computer with language. The command line is the baby little brother of programming languages. Learning the command line teaches you to control the computer using language. Once you get past that, you can then move on to writing code and feeling like you actually own the hunk of metal you just bought.
> 
> 摘录来自: Learn Python 3 the Hard Way
> 
> Many people speak of “freedom” with regard to Linux, but I don’t think most people know what this freedom really means. Freedom is the power to decide what your computer does, and the only way to have this freedom is to know what your computer is doing. Freedom is a computer that is without secrets, one where everything can be known if you care enough to find out.
> 
> 摘录来自: The Linux Command Line

## 终端配置

终端就是你使用命令行与计算机对话的地方，在终端顺序输入以下命令：

**安装 Homebrew**

```xcode-select --install```

```ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"```

**安装 Homebrew-Cask**

```brew tap caskroom/cask```

**安装 iTerm2**

```brew cask install iterm2```

**更新 zsh**

```brew install zsh```

**默认 shell 改为 zsh**

```chsh -s /bin/zsh```

## CLI 小练习

LPTHW 有附录 Command Line Crash Course，快对着它从头到尾敲一遍！

#### The Setup

> 需要记住的常用命令
> 
> - **pwd** print working directory
> - **hostname** my computer's network name
> - **mkdir** make directory
> - **cd** change directory
> - **ls** list directory
> - **rmdir** remove directory
> - **pushd** push directory
> - **popd** pop directory
> - **cp** copy a file or directory
> - **mv** move a file or directory
> - **less** page through a file
> - **cat** print the whole file
> - **xargs** execute arguments
> - **find** find files
> - **grep** find things inside files
> - **man** read a manual page
> - **apropos** find which man page is appropriate
> - **env** look at your environment
> - **echo** print some arguments
> - **export** export/set a new environment variable
> - **exit** exit the shell
> - **sudo** DANGER! become super user root DANGER!

### Paths, Folders, Directories(pwd)

```
192% pwd
/Users/Yucan
192%
```

#### If You Get Lost

```
192% pwd
/Users/Yucan/documents/github
192% cd ~
192% pwd
/Users/Yucan
```

#### Make a Directory(mkdir)

```
192% pwd
/Users/Yucan/documents/github
192% cd ~
192% mkdir temp
192% mkdir temp/stuff
192% mkdir temp/stuff/things
192% mkdir -p temp/stuff/things/orange/apple/pear/grape
192% mkdir "I Have Fun"
```

#### Change Directory(cd)

```
192% cd temp
192% pwd
/Users/Yucan/temp
192% cd stuff
192% pwd
/Users/Yucan/temp/stuff
192% cd things
192% pwd
/Users/Yucan/temp/stuff/things
192% cd orange/
192% pwd
/Users/Yucan/temp/stuff/things/orange
192% cd apple/
192% pwd
/Users/Yucan/temp/stuff/things/orange/apple
192% cd pear/
192% pwd
/Users/Yucan/temp/stuff/things/orange/apple/pear
192% cd grape/
192% pwd
/Users/Yucan/temp/stuff/things/orange/apple/pear/grape
192% cd ..
192% cd ..
192% pwd
/Users/Yucan/temp/stuff/things/orange/apple
192% cd ..
192% cd ..
192% pwd
/Users/Yucan/temp/stuff/things
192% cd ../../..
192% pwd
/Users/Yucan
192% cd temp/stuff/things/orange/apple/pear/grape
192% pwd
/Users/Yucan/temp/stuff/things/orange/apple/pear/grape
192% cd ../../../../../../../
192% pwd
/Users/Yucan
192% cd temp/stuff/things/orange/apple
192% pwd
/Users/Yucan/temp/stuff/things/orange/apple
192% cd ../../../../
192% pwd
/Users/Yucan/temp
192% cd ~
192% pwd
/Users/Yucan
192% cd documents
192% pwd
/Users/Yucan/documents
192% cd ~
192% cd downloads
192% pwd
/Users/Yucan/downloads
```

#### List Directory(ls)

```
192% cd temp
192% ls
stuff
192% cd stuff
192% ls
things
192% cd things
192% ls
orange
192% cd orange
192% ls
apple
192% cd apple
192% ls
pear
192% cd pear
192% ls
grape
192% cd grape
192% ls
192% cd ..
192% ls
grape
192% cd ../../../
192% ls
orange
192% cd ../../
192% ls
stuff
192% cd ~
192% cd temp
192% ls -lR
total 0
drwxr-xr-x  4 Yucan  staff  136  8 12 11:21 stuff

./stuff:
total 0
drwxr-xr-x  4 Yucan  staff  136  8 12 11:26 things

./stuff/things:
total 0
drwxr-xr-x  4 Yucan  staff  136  8 12 11:26 orange

./stuff/things/orange:
total 0
drwxr-xr-x  4 Yucan  staff  136  8 12 11:26 apple

./stuff/things/orange/apple:
total 0
drwxr-xr-x  4 Yucan  staff  136  8 12 11:46 pear

./stuff/things/orange/apple/pear:
total 0
drwxr-xr-x  2 Yucan  staff  68  8 12 11:26 grape

./stuff/things/orange/apple/pear/grape:
```

#### Remove Directory(rmdir)

```
192% cd temp
192% ls
stuff
192% cd stuff/things/orange/apple/pear/grape/
192% cd ..
192% rmdir grape
192% cd ..
192% rmdir pear
192% cd ..
192% ls
apple
192% rmdir apple
192% cd ..
192% ls
orange
192% rmdir orange
192% cd ..
192% ls
things
192% rmdir things
192% cd ..
192% ls
192% stuff
192% rmdir stuff
192% pwd
/Users/Yucan/temp
```

#### Moing Around(pushd, popd)

```
192% cd temp
192% mkdir -p i/like/icecream
192% pushd i/like/icecream
~/temp/i/like/icecream ~/temp
192% popd
~/temp
192% pwd
/Users/Yucan/temp
192% pushd i/like
~/temp/i/like ~/temp
192% pwd
/Users/Yucan/temp/i/like
192% pushd icecream
~/temp/i/like/icecream ~/temp/i/like ~/temp
192% pwd
/Users/Yucan/temp/i/like/icecream
192% popd
~/temp/i/like ~/temp
192% pwd
/Users/Yucan/temp/i/like
192% popd
~/temp
192% pushd i/like/icecream
~/temp/i/like/icecream ~/temp
192% pushd
~/temp ~/temp/i/like/icecream
192% pwd
/Users/Yucan/temp
192% pushd
~/temp/i/like/icecream ~/temp
192% pwd
/Users/Yucan/temp/i/like/icecream
```

#### Making Empty Files(Touch)

```
192% cd temp
192% touch iamcool.txt
192% ls
iamcool.txt
```

#### Copy a File(cp)

```
192% cd temp
192% cp iamcool.txt neat.txt
192% ls
iamcool.txt	neat.txt
192% cp neat.txt awesome.txt
192% ls
awesome.txt	iamcool.txt	neat.txt
192% cp awesome.txt thefourthfile.txt
192% ls
awesome.txt		neat.txt
iamcool.txt		thefourthfile.txt
192% mkdir something
192% cp awesome.txt something/
192% ls
awesome.txt		something
iamcool.txt		thefourthfile.txt
neat.txt
192% ls something
awesome.txt
192% cp -r something newplace
192% ls newplace
awesome.txt
```

#### Moving a File(mv)

```
192% cd temp
192% ls
awesome.txt		newplace
iamcool.txt		something
neat.txt		thefourthfile.txt
192% mv awesome.txt uncool.txt
192% ls
iamcool.txt		something
neat.txt		thefourthfile.txt
newplace		uncool.txt
192% mv newplace oldplace
192% ls
iamcool.txt		something
neat.txt		thefourthfile.txt
oldplace		uncool.txt
192% mv oldplace newplace
192% ls
iamcool.txt		something
neat.txt		thefourthfile.txt
newplace		uncool.txt
```

#### View a File(less, MORE)

```
192% cd desktop
192% cp test.txt ../temp
192% cd ~
192% cd temp
192% ls
test.txt
192% less test.txt



b
r
o
test.txt (END)

192% cp desktop/test.txt temp
192% cd temp
192% ls
test.txt
192% less test.txt
```

#### Stream a File(cat)

```
192% less test2.txt
192% cat test2.txt
192% cat test.txt
```

#### Removing a File(rm)

```
192% cd temp
192% ls
test.txt	test2.txt
192% rm test.txt
192% ls
test2.txt
192% cd ~
192% rm temp
rm: temp: is a directory
192% rm -rf temp
```

#### Exiting Your Terminal(exit)

```
192% exit
```



