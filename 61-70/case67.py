# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-10 11:45:34
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-10 11:55:35

# 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组


def run():

    l = [3, 6, 8, 9, 2, 5]
    max_num = max(l)
    min_num = min(l)
    l[l.index(max_num)], l[0] = l[0], max_num
    l[l.index(min_num)], l[-1] = l[-1], min_num

    print(l)


if __name__ == '__main__':
    run()
