## 实践中的异同

LPTHW 的任务都完成了吧？如果敲完了 Python2 和 Python3 两个版本，你应该会发现下面这几个明显的异同：

> 1. Python3 中，print 不再是语句，而是函数
> 2. 格式化字符串发生了很大变化，%...全没了，取而代之的是 `f"{var}"` & `"{}".format(var)`
> 3. raw_input 消失了，Python3 中只有 input()
> 4. Python3 中，可以给 end 赋值 `' '` ，这样 print 函数不会在字符串末尾添加一个换行符，而是添加一个空字符串


## 官方文档

[wiki](https://wiki.python.org/moin/Python2orPython3)

> Short version: Python 2.x is legacy, Python 3.x is the present and future of the language
>
> Python 3.0 was released in 2008. The final 2.x version 2.7 release came out in mid-2010, with a statement of extended support for this end-of-life release. The 2.x branch will see no new major releases after that. 3.x is under active development and has already seen over five years of stable releases, including version 3.3 in 2012, 3.4 in 2014, 3.5 in 2015, and 3.6 in 2016. This means that all recent standard library improvements, for example, are only available by default in Python 3.x.
>
> Guido van Rossum (the original creator of the Python language) decided to clean up Python 2.x properly, with less regard for backwards compatibility than is the case for new releases in the 2.x range. The most drastic improvement is the better Unicode support (with all text strings being Unicode by default) as well as saner bytes/Unicode separation.
>
> Besides, several aspects of the core language (such as print and exec being statements, integers using floor division) have been adjusted to be easier for newcomers to learn and to be more consistent with the rest of the language, and old cruft has been removed (for example, all classes are now new-style, "range()" returns a memory efficient iterable, not a list as in 2.x).
>
> The [What's New in Python 3.0](http://docs.python.org/py3k/whatsnew/3.0.html) document provides a good overview of the major language changes and likely sources of incompatibility with existing Python 2.x code. Nick Coghlan (one of the CPython core developers) has also created a [relatively extensive FAQ](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html) regarding the transition.
>
> However, the broader Python ecosystem has amassed a significant amount of quality software over the years. The downside of breaking backwards compatibility in 3.x is that some of that software (especially in-house software in companies) still doesn't work on 3.x yet.