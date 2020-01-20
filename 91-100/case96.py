# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-20 18:10:53
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-20 18:16:55

# 计算字符串中子串出现次数


def run():

    s1 = input("请输入一行字符串：")
    s2 = input("请输入需要查找的子串：")

    print('%s 在 %s 中一共出现了 %d 次' % (s2, s1, s1.count(s2)))


if __name__ == '__main__':
    run()
