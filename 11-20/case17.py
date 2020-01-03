# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-03 21:45:57
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-03 21:53:31

# 输入一行字符，分别统计出其中的英文字符、空格、数字和其他字符的个数


def get_nums(s):
    a, b, c, d = 0, 0, 0, 0

    for i in s:
        if i.isdigit():
            a += 1
        elif i.isalpha():
            b += 1
        elif i.isspace():
            c += 1
        else:
            d += 1

    return a, b, c, d


def run():

    s = input("请输入一行字符串：")
    a, b, c, d = get_nums(s)
    print("其中英文有%d个，空格有%d个，数字有%d个，其他字符有%d个" % (b, c, a, d))


if __name__ == "__main__":
    run()
