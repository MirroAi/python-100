# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-03 21:54:46
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-03 22:06:50

# 求s=a+aa+aaa+aaaa+aa...a的值，其中，a是一个数字。几个数相加由键盘控制


def add_nums(a, times):

    l = []

    for i in range(1, times+1):
        s = ''
        for j in range(1, i+1):
            s += str(a)
        l.append(int(s))

    return l


def run():

    a = int(input("请输入数字："))
    t = int(input("请输入相加次数："))

    l = add_nums(a, t)

    print(sum(l), end=" = ")

    for i in l:
        if i != l[-1]:
            print(i, end=" + ")
        else:
            print(i)


if __name__ == "__main__":
    run()
