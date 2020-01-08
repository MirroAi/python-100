# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-08 20:44:29
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-08 20:49:09

# 数字比较


def run():

    a, b = input("请输入两个数字，如 1,2：").split(",")
    a, b = int(a), int(b)

    if a > b:
        print("%d > %d" % (a, b))
    elif a == b:
        print("%d = %d" % (a, b))
    else:
        print("%d < %d" % (a, b))


if __name__ == "__main__":
    run()
