# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-03 13:34:11
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-03 13:36:14


# 暂停一秒输出

import time


def run():

    for i in range(5):
        print(i)
        time.sleep(1)


if __name__ == '__main__':
    run()
