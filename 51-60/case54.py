# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-08 21:10:42
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-08 21:16:59

# 取一个整数a从右端开始的4~7位


def function(s):
    l = []

    for i in range(3, 7):
        l.append(s[::-1][i])

    return l


def run():

    s = input("请输入一个超过7位的整数：")
    l = function(s)
    for i in range(4):
        print("从右数起，第%d位数字是%s" % (i+4, l[i]))


if __name__ == "__main__":
    run()
