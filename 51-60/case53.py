# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-08 21:08:21
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-08 21:09:46

# 学习使用按位异或 ^


def run():

    a = 8
    b = a ^ 0
    c = a ^ 3
    d = a ^ 6
    e = a ^ 9
    print("a =", a)
    print("a ^ 0 = %d" % b)
    print("a ^ 3 = %d" % c)
    print("a ^ 6 = %d" % d)
    print("a ^ 9 = %d" % e)


if __name__ == "__main__":
    run()
