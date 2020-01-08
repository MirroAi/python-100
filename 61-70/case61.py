# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-08 21:47:36
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-08 22:19:24

# 打印出杨辉三角，至少10行


def get_Pascal_Triangle(n):

    l = []

    for i in range(1, n+1):
        L = []
        for j in range(1, i+1):
            L.append(0)   # 占位
        L[0] = 1
        L[-1] = 1
        l.append(L)
        if i > 2:  # 从第3行开始，除了首位，其余均为上一行两个数的和
            for k in range(i):
                if 0 < k < i-1:
                    l[-1][k] = l[-2][k-1] + l[-2][k]

    return l


def run():

    n = int(input("请输入输出杨辉三角的行数："))

    l = get_Pascal_Triangle(n)
    for i in l:
        for j in i:
            print("%d" % j, end=" ")
        print()


if __name__ == "__main__":
    run()
