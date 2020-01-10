# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-10 11:56:17
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-10 12:04:44

# 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变为最前面的m个数


def function(n, m):
    l = []
    for i in range(n):
        l.append(i)
    for i in range(m):
        l.insert(0, l.pop(-1))
    return l


def run():

    n = int(input("请输入n："))
    m = int(input("请输入m："))

    print(function(n, m))


if __name__ == '__main__':
    run()
