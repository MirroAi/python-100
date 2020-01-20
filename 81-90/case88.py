# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-20 17:22:11
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-20 17:29:56

# 读取7个数的整数值（1到50），每读取一个值，程序打印出该值个数的*


def run():

    n = 1
    while n < 8:
        try:
            x = int(input("请输入1到50的整数："))
        except ValueError:
            print("输入有误！")
        else:
            print("*"*x)
        n += 1


if __name__ == "__main__":
    run()
