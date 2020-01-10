# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-10 21:58:43
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-10 22:05:03

# 编写一个函数，输入n为偶数时，调用函数1/2 + 1/4 + ... + 1/n，当输入n】为奇数时，调用函数1/1 + 1/3 + ... + 1/n


def function(n):

    s = 0

    if n % 2 == 0:
        for i in range(2, n+1, 2):
            s += 1/i
    else:
        for i in range(1, n+1, 2):
            s += 1/i

    return s


def run():

    n = int(input("请输入n："))
    print("值为：", function(n))


if __name__ == "__main__":
    run()
