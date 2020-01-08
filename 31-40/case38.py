# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-08 17:44:38
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-08 17:47:23

# 求一个3*3矩阵主对角线元素之和


def run():

    l = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    s = 1
    for i in range(len(l)):
        for j in range(len(l[i])):
            if i == j:
                s *= l[i][j]

    print(s)


if __name__ == "__main__":
    run()
