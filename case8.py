# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-03 13:11:21
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-03 13:29:59


# 输出9*9乘法口诀表

def run():
    l = []
    for i in range(9):
        l.append(list(""))
        for j in range(i+1):
            l[i].append("%d * %d = %d" % (i+1, j+1, (i+1)*(j+1)))

    for i in range(9):
        for j in range(len(l[i])):
            print(l[i][j], end="  ")
        print("\n")


if __name__ == '__main__':
    run()
