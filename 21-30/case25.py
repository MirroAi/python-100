# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-07 19:53:51
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-07 20:03:45

# 求1!+2!+3!+4!+5!+...+20!的和


def get_factorial(n):
    # 获取n!
    s = 1
    for i in range(1, n+1):
        s *= i

    return s


def add_nums(n):
    # 获取和
    s = 0
    for i in range(1, n+1):
        s += get_factorial(i)

    return s


def run():

    n = int(input("请输入需要求的n值："))
    for i in range(1, n+1):
        if i != n:
            print("%d!+" % i, end="")
        else:
            print("%d!=" % i, end="")
    print(add_nums(n))


if __name__ == "__main__":
    run()
