#/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: Ehang Zhang
@file: 5.3_anonymous_function.py
@time: 2018/7/13 15:53
"""

# 匿名函数
# 有时为了传入函数更方便，可以不用显示地定义函数，而是直接使用匿名函数

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数

# 匿名函数的限制： 只能有一个表达式，不用写return， 表达式的结果就是返回值。

# 匿名函数的好处： 因为匿名函数没有名字，所以不用担心函数名冲突

# 也可以将匿名函数赋值给变量，
f = lambda x: x * x
print(f)
print(f(5))

# 或者作为函数返回值返回
def build(x, y):
    return lambda: x * x + y * y


# exercise
# 请用匿名函数改造下面的代码
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)

# 改造
L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)
