# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-02 21:44:31
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-02 22:10:06

# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

import math

def function():

    l = []

    for i in range(-100, 100000):
        x = int(math.sqrt(i + 100))
        y = int(math.sqrt(i + 100 + 168))
        if (x**2==i+100) and (y**2==i+100+168):
            l.append(i)

    return l


def run():
    l = function()
    for i in l:
        print(i)


if __name__ == '__main__':
    run()