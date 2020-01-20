# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-20 17:08:46
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-20 17:15:57

# 输入一个奇数，然后判断最少几个9除以该数的结果为整数


def function(x):

    i = 1
    while True:

        y = int("9"*i)
        if y % x == 0:
            print("%d 可以被 %d 整除" % (x, y))
            break
        i += 1
        # print(i)


def run():

    x = int(input("请输入奇数："))
    if x % 2 == 0:
        print("输入有误！")
    else:
        function(x)


if __name__ == "__main__":
    run()
