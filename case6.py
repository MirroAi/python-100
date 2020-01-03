# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-03 12:38:10
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-03 12:58:34

# 斐波那契数列，又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、...
# 在数学上，斐波那契数列是以递归的方法来定义：
# F0 = 0; F1 = 1; Fn = F[n-1] + F[n-2](n>=2)


def function(n):
    l = [0, 1]
    L = []
    if n == 1 or n == 2:
        L = l[:n]
    else:
        for i in range(2, n):
            l.append(l[i-1] + l[i-2])
        L = l
    return L


def run():
    n = int(input("请输入需要输出的斐波那契数列中数字的个数："))
    print(function(n))


if __name__ == "__main__":
    run()
