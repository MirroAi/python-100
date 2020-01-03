# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-03 21:33:32
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-03 21:45:24

# 输出指定格式的日期，例如YYYY/mm/dd HH:MM:SS

import time


def print_formatted_date():
    print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))


def run():
    print_formatted_date()


if __name__ == '__main__':
    run()
