# -*- coding: utf-8 -*-
# @Author: MirrorAi
# @Date:   2020-01-03 21:29:13
# @Last Modified by:   MirroAi
# @Last Modified time: 2020-01-03 21:32:49

# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，
# 60-89分之间的用B表示，60分以下的用C表示


def get_grade_rank(grade):
    if grade >= 90:
        return "A"
    elif grade >= 60:
        return "B"
    else:
        return "C"


def run():

    grade = int(input("请输入学习成绩："))
    print(get_grade_rank(grade))


if __name__ == "__main__":
    run()
