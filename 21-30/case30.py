# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-07 20:46:20
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-07 20:50:05

# 一个5位数，判断它是不是回文数


def function(s):
    return s == s[::-1]


def run():

    s = input("请输入一个正整数：")
    if function(s):
        print("%s是一个回文数(*￣︶￣)"%s)
    else:
        print("%s不是一个回文数[○･｀Д´･ ○]"%s)


if __name__ == "__main__":
    run()
