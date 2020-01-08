# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-08 20:28:06
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-08 20:40:24

# 求输入数字的平方，如果平方运算后小于50则退出


def function(n):
    return n*n


def run():

    result = 50
    while result >= 50:
        n = int(input("请输入一个数字："))
        result = function(n)
        print("%d的平方为%d" % (n, function(n)))


if __name__ == "__main__":
    run()
