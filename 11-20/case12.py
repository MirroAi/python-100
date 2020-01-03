# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-03 20:46:42
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-03 20:54:51

# 判断101-200之间有多少个素数，并输出所有素数


def run():

    l = []

    for i in range(101, 201):
        flag = 1
        for j in range(2, i):
            if i % j == 0:
                flag = 0
                continue
        if flag:
            l.append(i)

    print("101到200之间有%d个素数\n分别是：" % len(l))
    for i in l:
        print(i, end="  ")


if __name__ == '__main__':
    run()
