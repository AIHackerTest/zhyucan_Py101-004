## 程序结构示例

[《极简 Python 上手导念》](http://wiki.zoomquiet.io/pythonic/MinimalistPyStart?from=timeline&isappinstalled=0)

```python
# 导入 os.py
import os

def main():
    print('Hello world!')

    print("This is Alice's greeting.")
    print('This is Bob\'s greeting.')

    foo(5, 10)

    print('=' * 10)
    print('Current working directory is ' + os.getcwd()) # 调用 os 模块中的函式


    counter = 0
    counter += 1


    food = ['apples', 'oranges', 'cats']

    for i in food:
        print(f'I like to eat {i}')


    print('Count to ten:')
    for i in range(10):
        print(i)


def foo(param1, secondParam):
    res = param1 + secondParam

    print(f'{param1} plus {secondParam} is equal to {res}')

    if res < 50:
        print('foo')

    elif (res >= 50) and ((param1 == 42) or (secondParam == 24)):
        print('bar')

    else:
        print('moo')

    return res # This is a one-line comment.
    '''A multi-
line string, but can also be a multi-line comment.'''

# 一般在脚本最后调用主函式 main()；而且使用内置的运行脚本名来判定
# 当且仅当我们直接运行当前脚本时，__name__ 才为 __main__
# 这样当脚本被当作模块进行 import 导入时，并不运行 main()
# 所以，一般这里是进行测试代码安置的...
if __name__ == '__main__':
    main()
```

## Python Style

[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

[Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

[Google Style Guides](https://github.com/google/styleguide)
