# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-10 12:06:06
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-10 21:23:54

# 有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下来的是原来第几号的那位


def create_a_list(n):

    l = []
    for i in range(1, n+1):
        l.append(i)

    return l


def function(l):

    length = len(l)
    count = 0

    while length > 1:

        count += 1
        if count == 3:
            l.pop(0)
            count = 0
        else:
            l.append(l.pop(0))
        length = len(l)

    return l[0]


def run():

    n = int(input("请输入人数："))

    print(function(create_a_list(n)))


if __name__ == "__main__":
    run()
