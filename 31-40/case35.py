# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-07 21:36:29
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-07 21:51:12

# 文本颜色设置
# 说明：
# 前景色         背景色           颜色
# ---------------------------------------
# 30                40              黑色
# 31                41              红色
# 32                42              绿色
# 33                43              黃色
# 34                44              蓝色
# 35                45              洋红
# 36                46              青色
# 37                47              白色
# 显示方式             　 意义
# ----------------------------------
# 0                    终端默认设置
# 1                    高亮显示
# 22　　　　　　　　　　　非高亮显示
# 4                    使用下划线
# 24　　　　　　　　　　　去下划线
# 5                    闪烁
# 25　　　　　　　　　　　去闪烁
# 7                    反白显示
# 27　　　　　　　　　　　非反显
# 8                    不可见
# 28　　　　　　　　　　　可见

# 例：
# \033[1;32;41m   #---1-高亮显示 32-前景色绿色  40-背景色红色---
# \033[0m         #---采用终端默认设置，即缺省颜色---


def print_colorful_text():
    print("\033[1;31;40m")
    print("*"*50)
    print("\033[37;41mPlease Connect Administrator!\033[1;31;40m")
    print("*"*50)
    print("\033[0m")


if __name__ == "__main__":
    print_colorful_text()
