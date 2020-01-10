# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-10 21:26:14
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-10 21:28:52

# 写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度


def get_length_of_string(s):
    return len(s)


def main():
    s = input("请输入字符串：")
    print("字符串长度为 %d" % get_length_of_string(s))


if __name__ == "__main__":
    main()
