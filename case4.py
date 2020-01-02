# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-02 22:10:37
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-02 22:26:11

# 输入某年某月某日，判断这一天是这一年的第几天？

month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def function(year, month, day):

    flag = 0
    if ((year%4==0 and year%100!=0) or (year%400==0)) and month>2:
        flag = 1

    days = 0
    for i in range(month-1):
        days += month_day[i]

    return days + flag + day


def run():

    year, month, day = input("请输入年月日：（格式YYYY-MM-DD）\n").split("-")
    print("该日是当年的第%d天"%function(int(year), int(month), int(day)))


if __name__ == '__main__':
    run()