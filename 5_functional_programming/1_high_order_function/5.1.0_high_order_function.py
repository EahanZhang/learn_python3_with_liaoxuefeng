#/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: Ehang Zhang
@file: 5.1.0_high_order_function.py
@time: 2018/7/13 9:31
"""

# 高阶函数
# 如果一个函数可以接收另一个函数作为参数，这种函数就称之为高阶函数。
#
# 变量可以指向函数，即函数本身也可以赋值给变量。
b = abs(-10)
print(b)
b = abs
print(b)

# 函数名也是变量
# print(abs)
# abs = 10
# print(abs)
# 此时再调用abs(-10)会报错

# 因为变量可以指向函数，函数的参数能接收变量，因此一个函数就能接收另一个函数作为参数， 该函数被称为高阶函数。


# 传入函数
def add(x, y, f):
    return f(x) + f(y)

print(add)
print(add(-5, 6, abs))