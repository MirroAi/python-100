# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-07 21:32:32
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-07 21:33:35

# 练习函数调用


def hello():
    print("hello world!")


def f(times):
    for i in range(times):
        hello()


if __name__ == "__main__":
    f(5)
