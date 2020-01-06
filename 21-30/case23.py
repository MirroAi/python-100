# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-06 20:43:00
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-06 21:41:14

# 打印出如下图案（菱形）：
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *


def print_Rhombus(n):
    # 打印菱形，输入奇数行
    if n % 2 == 0:
        print("输入错误，退出程序")
        return
    L = []
    mid = int((n+1)/2)

    for i in range(n):
        if i < mid:
            s1 = " " * (mid-i-1)
            s2 = "*" * (i*2 + 1)
            L.append(s1 + s2)
        else:
            L.append(L[n-i-1])

    for i in L:
        print(i)


def run():

    n = int(input("请输入需要打印的菱形行数：（奇数行）"))
    print_Rhombus(n)


if __name__ == "__main__":
    run()
