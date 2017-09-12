## 小游戏

学有余力的你，综合运用编程基础技能，尝试实现一个猜数字小游戏吧 ——

- 程序随机生成一个 20 以内的数字，用户有 10 次机会猜测
- 程序根据用户输入，给予一定提示（大了、小了、正确）
- 猜对或用完 10 次机会，游戏结束

代码如下：

```python
import random

random_num = random.randint(10, 20)
print("有个数在 10 与 20 之间，10 次机会给你猜")

input_times = 10

while input_times > 0:
    try:
        guess_num = int(input("> "))
    except ValueError:
        print("要是整数哦！")
        continue

    input_times -= 1

    if guess_num < random_num:
        print(f"小了，还有 {input_times} 次机会 ")
    elif guess_num > random_num:
        print(f"大了，还有 {input_times} 次机会 ")
    else:
        print("对喏")
        break
```

## 大游戏

开发升级版猜数字小游戏，实现以下功能：

- 程序内部用 0-9 生成一个 4 位数，每个数位上的数字不重复，且首位数字不为零，如 1942
- 用户输入 4 位数进行猜测，程序返回相应提示
 - 用 A 表示数字和位置都正确，用 B 表示数字正确但位置错误
 - 用户猜测后，程序返回 A 和 B 的数量
 - 比如：2A1B 表示用户所猜数字，有 2 个数字，数字、位置都正确，有 1 个数字，数字正确但位置错误
- 猜对或用完 10 次机会，游戏结束

代码如下：

```python
import random

def createnum():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    slice1 = random.sample(list1, 1)
    slice2 = random.sample(list2, 3)
    a = slice1[0]
    b = slice2[0]
    c = slice2[1]
    d = slice2[2]
    return a * 1000 + b * 100 + c * 10 + d


random_num = str(createnum())

print("猜一个四位数，四个数不重复，10 次机会给你猜")

input_times = 10

while input_times > 0:
    try:
        guess = int(input("> "))
    except ValueError:
        print("猜一个数字！")
        continue

    input_times -= 1

    a = 0
    b = 0
    guess_num = str(guess)

    if guess_num != random_num:
        for i in range(0, 4):
            if guess_num[i] == random_num[i]:
                a += 1
            elif guess_num[i] in random_num:
                b += 1
        print(f"{a}A{b}B, 还有{input_times}次机会")
    else:
        print("对咯")
        break
```
