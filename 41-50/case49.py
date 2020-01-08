# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-08 20:50:03
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-08 20:52:19

# 使用lambda来创建匿名函数


def run():

    # def a(x): return x**3
    a = lambda x: x**3

    for i in range(4):
        print(a(i))


if __name__ == '__main__':
    run()
