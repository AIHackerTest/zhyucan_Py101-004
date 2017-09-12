```python
import sys

t = open('test.txt')

# '北京,晴\n' >> [北京, 晴]
def conver(s):
    l = []
    s1 = s[:-1]
    comma = 0
    for i in range(len(s1)):
        if s1[i] == ',':
            comma = i
    city = s1[:comma]
    weather = s1[comma+1:]
    l.append(city)
    l.append(weather)
    return l

# 生成字典 >> {'北京': '晴', '海淀': '晴', ...}
def weather_list(t):
    l1 = []
    d = {}
    f = list(t)
    for line in f:
        l1.append(conver(line))
    for i in l1:
        d[i[0]] = i[1]
    return d


# 根据用户输入返回数据
def user_input():
    dic = weather_list(t)
    city_input = []
    user = input('> ')
    while not ((user == 'quit') or (user == 'exit')):
        if user in dic:
            print(f"{user}: {dic[user]}")
            city_input.append(user)
            user = input('> ')
        elif (user == 'h') or (user == 'help'):
            print("输入城市名，返回该城市的天气数据\n"
                  "输入城市名，返回该城市的天气数据\n"
                  "输入指令（h or help），打印帮助文档\n"
                  "输入指令（quit or exit)，退出程序的交互")
            user = input('> ')
        else:
            print("你说的我不懂！")
            user = input('> ')
    print(city_input)
    sys.exit()

if __name__ == '__main__':
    print("我可以帮你查天气哦！")
    user_input()

```