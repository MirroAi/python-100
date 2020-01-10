# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-09 18:17:27
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-10 11:37:48

# 查找字符串

import re


def run():

    s = "abc de de defg ascdthsd"

    l = re.findall("de", s)

    print("%s 中共有 %d 个 de" % (s, len(l)))


if __name__ == "__main__":
    run()
