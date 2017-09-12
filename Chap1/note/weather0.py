#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

# 生成字典 >> {'北京': '晴', '海淀': '晴', ...}
def create_dict():
    with open('weather_info.txt', 'r', encoding='utf-8') as f:
        d = {}
        for s in list(f):
            key, value = s.strip('\n').split(',')
            d[key] = value
    return d

# 根据用户输入返回数据
def user_input():
    weather_dict = create_dict()
    input_hishory = []

    while True:
        user_input = input('> ')
        if user_input in weather_dict:
            print(f"{user_input}: {weather_dict[user_input]}")
            input_hishory.append(user_input)
        elif user_input in ['h', 'help']:
            print("输入城市名，返回该城市的天气数据\n"
                  "输入指令（h or help），打印帮助文档\n"
                  "输入指令（quit or exit)，退出程序的交互\n"
                  "退出程序前，会打印查询过的所有城市")
        elif user_input in ['quit', 'exit']:
            print(input_hishory)
            sys.exit()
        else:
            print("你说的我不懂！敲 h 寻求帮助吧~")

def main():
    print("我可以帮你查天气哦！")
    user_input()

if __name__ == '__main__':
    main()
