# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-08 17:49:05
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-08 17:55:03

# 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中


def run():
    l = [1, 8, 12, 36, 41, 48, 59, 68, 78, 79, 85, 89, 91, 96]

    x = int(input("请输入一个正整数："))
    for i in range(len(l)):
        if l[i] > x:
            l.insert(i, x)
            break

    print(l)


if __name__ == "__main__":
    run()
