# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-07 20:29:38
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-07 20:34:02

# 给一个不多于5位的正整数，要求：
# 1. 求它是几位数
# 2. 逆序打印出各位数字


def function(s):
    return len(s), s[::-1]


def run():
    s = input("请输入一个正整数：")
    print("1. %s是%d位数\n2. 逆序为%s" % (s, function(s)[0], function(s)[1]))


if __name__ == "__main__":
    run()
