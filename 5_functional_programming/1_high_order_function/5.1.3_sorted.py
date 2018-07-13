#/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: Ehang Zhang
@file: 5.1.3_sorted.py
@time: 2018/7/13 14:03
"""

# sorted()函数 用于排序
# sorted(list, key=function_name, reverse=bool_value)
L = [26, 5, -12, -21, 9]
print(sorted(L))
print(sorted(L, key=abs))
print(sorted(L, key=abs, reverse=True))


# exercise
# 假设我们用一组tuple表示学生名字和成绩：
#
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：
def by_name(t):
    return t[0].lower()

L2 = sorted(L, key=by_name)
print(L2)

# 再按成绩从高到低排序：
def by_score(t):
    return -t[1]

L2 = sorted(L, key=by_score)
print(L2)
