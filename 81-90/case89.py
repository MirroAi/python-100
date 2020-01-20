# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-20 17:31:12
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-20 17:56:41

# 某公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
# 每个数字都加上5，然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和
# 第三位交换


def encrypt_code(s):

    for i in range(4):
        s += str((int(s[i]) + 5) % 10)

    return s[:3:-1]


def decrypt_code(s):

    for i in range(4):
        if 5 <= int(s[i]) <= 9:
            s += str(int(s[i]) - 5)
        else:
            s += str(int(s[i]) + 10 - 5)

    return s[:3:-1]


def run():

    s1 = input("请输入四位整数：")
    print("加密后为"+encrypt_code(s1))
    s2 = input("请输入加密后的四位整数：")
    print("解密后为"+decrypt_code(s2))


if __name__ == "__main__":
    run()
