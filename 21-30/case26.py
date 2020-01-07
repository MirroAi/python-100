# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-07 20:04:46
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-07 20:08:41

# 使用递归方法求5!


def function(n):
    if n == 1:
        return 1
    else:
        return function(n-1)*n


def run():

    n = int(input("请输入n："))
    print("%d!=%d" % (n, function(n)))


if __name__ == "__main__":
    run()
