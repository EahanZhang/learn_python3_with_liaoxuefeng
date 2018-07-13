#/usr/bin/python
# -*- coding: utf-8 -*-

# python内置了很多有用的函数
# 调用函数需要知道函数的名称和参数

a = -1
print(a)
print(abs(a))

# 数据类型转换
# python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他类型的数据转换为整数
print(int('123'))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋值给一个变量，相当于给这个函数起了一个别名
b = abs
print(abs(a))
print(b(a))