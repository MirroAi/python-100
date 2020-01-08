# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-08 18:20:04
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-08 18:22:16

# 统计1到100的和


def function(n):

    s = 0
    for i in range(1, n+1):
        s += i

    return s


def run():

    n = int(input("请输入n："))
    print("1到%d之和为：%d" % (n, function(n)))


if __name__ == "__main__":
    run()
