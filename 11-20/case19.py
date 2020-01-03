# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-03 22:07:44
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-03 22:19:26

# 一个数如果恰好等于除自身之外所有因子之和，这个数就称为“完数”。
# 例如6=1+2+3，编程找出1000以内的所有完数


def function(x):
    l = []
    for i in range(1, x):
        if x % i == 0:
            l.append(i)

    if x == sum(l):
        return x


def run():
    for i in range(1, 1001):
        result = function(i)
        if result:
            print(result)


if __name__ == "__main__":
    run()
