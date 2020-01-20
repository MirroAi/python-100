# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-20 18:23:46
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-20 18:25:59

# 从键盘输入一个字符串，将小写字母转换成大写字母，然后输出到一个磁盘文件“test”中保存


def run():

    text = input("请输入字符串：")
    with open("test.txt", "a") as f:
        f.write(text)


if __name__ == "__main__":
    run()
