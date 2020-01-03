# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-03 13:45:56
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-03 20:44:27

# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？
# [1, 1, 2, 3, 5, 8, 13, ...]


def function(n):
    l = [1, 1]
    if n == 1 or n == 2:
        return l[n-1]
    else:
        for i in range(2, n):
            l.append(l[i-1] + l[i-2])
        return l[n-1]


def run():
    n = int(input("请输入想要获得兔子总数的月份："))
    print("%d月共有兔子%d对" % (n, function(n)))


if __name__ == "__main__":
    run()
