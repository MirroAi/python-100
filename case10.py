# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-03 13:37:16
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-03 13:41:24


# 暂停一秒输出，并格式化当前时间

import time


def run():

    t = time.time()
    print(t)
    time.sleep(1)
    print(time.asctime(time.localtime(t)))


if __name__ == '__main__':
    run()
