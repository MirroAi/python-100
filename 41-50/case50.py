# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-08 20:53:54
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-08 20:57:00

# 输出一个随机数

import random


def run():

    l = input("请输入随机数的上下边界，如 4-50：\n").split("-")

    a, b = int(l[0]), int(l[1])
    print("输出随机数为：%d" % random.randint(a, b))


if __name__ == "__main__":
    run()
