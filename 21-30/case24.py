# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-06 21:58:08
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-06 22:06:37

# 有一分数序列：2/1,3/2,5/3,8/5,13/8,21/13...求出这个数列的前20项之和


def function(n):
    a = 2
    b = 1
    s = 0
    for i in range(n):
        s += a/b
        a, b = a+b, a

    return s


def run():

    n = int(input("请输入需要求出数列前几项和："))
    print("前%d项和为：" % n, end="")
    print(function(n))


if __name__ == "__main__":
    run()
