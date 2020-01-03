# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-03 21:02:15
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-03 21:28:26

# 将一个正整数分解质因数，例如输入90，打印90=2*3*3*5


def function(n, l):
    for i in range(2, n+1):
        if n % i == 0:
            l.append(i)
            n = int(n/i)
            function(n, l)
            return l


def run():
    n = int(input("请输入一个正整数："))
    print("%d = "%n, end="")
    for i in function(n, []):
        if i != function(n, [])[-1]:
            print(i, end=" * ")
        else:
            print(i)


if __name__ == '__main__':
    run()
