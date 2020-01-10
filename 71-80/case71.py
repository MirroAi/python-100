# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-10 21:29:58
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-10 21:45:38

# 编写输入输出函数，输出5个学生的数据记录


def get_score():
    d = {}

    d["name"] = input("请输入学生姓名：")
    d["Chinese_score"] = int(input("请输入语文成绩："))
    d["Math_score"] = int(input("请输入数学成绩："))
    d["English_score"] = int(input("请输入英语成绩："))

    print("*"*50)

    return d


def run():

    person1 = get_score()
    person2 = get_score()

    print("姓名：%s，语文成绩：%d，数学成绩：%d，英语成绩：%d" % (person1["name"], person1["Chinese_score"], person1["Math_score"], person1["English_score"]))
    print("姓名：%s，语文成绩：%d，数学成绩：%d，英语成绩：%d" % (person2["name"], person2["Chinese_score"], person2["Math_score"], person2["English_score"]))


if __name__ == "__main__":
    run()
