# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-08 20:58:49
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-08 21:03:21

# 学习使用按位与 &


def run():

    a = 15
    b = a & 1
    c = a & 3
    d = a & 6
    print("a =", a)
    print("a & 1 = %d" % b)
    print("a & 3 = %d" % c)
    print("a & 6 = %d" % d)


if __name__ == "__main__":
    run()
