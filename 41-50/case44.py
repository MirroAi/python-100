# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-08 18:06:54
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-08 18:19:11

# 两个3行3列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵

import random


def create_Matrix(l):
    for i in range(3):
        l.append([])
        for j in range(3):
            l[i].append(random.randint(1, 100))
    return l


def run():

    l1 = create_Matrix([])
    l2 = create_Matrix([])
    l = []

    for i in range(3):
        l.append([])
        for j in range(3):
            l[i].append(l1[i][j] + l2[i][j])

    print(l1)
    print(l2)
    print(l)


if __name__ == "__main__":
    run()
