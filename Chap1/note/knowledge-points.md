## 读写文件

计算机里的文本、图片、音频、视频以及其他各种类型的文件，都可以通过 Python 读写。这次的小程序只需要了解如何读写文本就可以啦。

在 LPTHW 里，你已经学到了有关文本读写的这些知识：

> - 打开文件：open('filename', mode)
> - 读取文件：read()
> - 读一行: readline()
> - 关闭文件：close()
> - 写入文件：write(stuff)
> - 清空文件：truncate()
> - 归零：seek(0)

查找官方文档——[Input and Output](https://docs.python.org/3.6/tutorial/inputoutput.html#reading-and-writing-files)，下面这些知识点可能会用到这次的小程序中：

```python
# 利用 list(f) or f.readlines()，可以把文本的每一行写到一个列表中
# 可以循环遍历文本对象，读取文本每一行
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file
```

## 字典

字典是一组无序键值对，一个字典里键是唯一的。举几个例子说明用法：

```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel.keys())
['jack', 'guido', 'irv']
>>> sorted(tel.keys())
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

```python
>>> dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
>>> keys = dishes.keys()
>>> values = dishes.values()
>>>
>>> n = 0
>>> for val in values:
...     n += val
...
>>> print(n)
504
>>>
>>> # keys and values are iterated over in the same order
>>> list(keys)
['eggs', 'sausage', 'bacon', 'spam']
>>> list(values)
[2, 1, 1, 500]
>>>
>>> # view objects are dynamic and reflect dict changes
>>> del dishes['eggs']
>>> del dishes['sausage']
>>> list(keys)
['bacon', 'spam']
>>>
>>> # set operations
>>> keys & {'eggs', 'bacon', 'salad'}
{'bacon'}
>>> keys ^ {'sausage', 'juice'}
{'bacon', 'juice', 'spam', 'sausage'}
```

```python
>>> # 循环列表和字典
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
>>>
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
>>>
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}? It is {1}.'.format(q, a))
...
What is your name? It is lancelot.
What is your quest? It is the holy grail.
What is your favorite color? It is blue.
>>>
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
>>>
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> set(basket)
{'orange', 'banana', 'apple', 'pear'}
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
>>>
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

## 退出程序
```python
import sys
sys.exit()
```

## 保存输入

用 input() 提取用户输入，然后保存到列表中。