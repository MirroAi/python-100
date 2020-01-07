# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-07 20:20:42
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-07 20:26:57

# 有5个人坐在一起，问第五个人多少岁？他说比第四个人大2岁。问第四个人多少岁？他说比第三个人大2岁。
# 问第三个人多少岁？他说比第二个人大2岁。问第二个人多少岁？他说比第一个人大2岁。问第一个人多少岁，
# 他说是10岁。请问第五个人多大年龄？


def function(n):

    if n == 1:
        return 10
    else:
        return function(n-1) + 2


def run():

    n = int(input("请输入需要求出年龄的人排序数："))
    print("第%d个人的年龄为：%d" % (n, function(n)))


if __name__ == "__main__":
    run()
