# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-08 17:39:27
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-08 17:43:10

# 对10个数进行排序


def run():

    l = [1, 2, 5, 7, 3, 9, 2, 10]

    print("降序排列：%s" % sorted(l, reverse=True))
    print("升序排列：%s" % sorted(l))


if __name__ == "__main__":
    run()
