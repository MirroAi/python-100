# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-07 20:10:36
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-07 20:20:01

# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
# 递归，是从尾部往前拆，找规律


def print_string(s):
    l = len(s)
    if l == 1:
        print(s, end="")
    else:
        print(s[-1], end="")
        print_string(s[:-1])


def run():

    s = input("请输入字符串：")
    print_string(s)


if __name__ == "__main__":
    run()
