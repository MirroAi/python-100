# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-08 20:41:35
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-08 20:43:08

# 两个变量值互换


def run():
    a = 1
    b = 2
    print("a = %d, b = %d" % (a, b))
    a, b = b, a
    print("互换变量值后：\na = %d, b = %d" % (a, b))


if __name__ == "__main__":
    run()
