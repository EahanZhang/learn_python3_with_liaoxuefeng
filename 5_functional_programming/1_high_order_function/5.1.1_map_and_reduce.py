#/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: Ehang Zhang
@file: 5.1.1_map_and_reduce.py
@time: 2018/7/13 10:03
"""

# map() 函数
# map(function_name, iterable)
# map()函数将function_name所指向的函数作用于iterable中的每一个元素，并返回
def f(x):
    return x * x;

r = map(f, range(10))
print(list(r)) # 由于结果r是一个Iterator, Iterator是惰性序列，所以需要list()函数让其把整个序列都计算出来并返回一个list


# reduce() 函数
# reduce(function_name, iterable)
# reduce()函数把函数function_name()作用于一个序列iterable上
# function_name()必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def fn(x, y):
    return x * 10 + y

print(reduce(fn, range(10)))


# exercise1
# 利用map()函数，把用户输入的不规范的英文名字变为统一格式： 首字母大写，其他字母小写
def normalize(name):
    if name is None or len(name) == 0:
        return name
    else:
        s1 = name[0].upper()
        s2 = name[1:].lower()
        return s1 + s2

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# exercise 2
# 编写一个prod()函数，可以接受一个list并利用reduce求积
def prod(L):

    def multiple(x, y):
        return x * y

    return reduce(multiple, L)

def prod_with_lambda(L):
    return reduce(lambda x, y: x * y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

print('3 * 5 * 7 * 9 =', prod_with_lambda([3, 5, 7, 9]))
if prod_with_lambda([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# exercise 3
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成字符串123.456
def str2float(s):
    if s is None or len(s) == 0:
        return None
    else:
        L1, L2 = s.split('.', 1)
        len_l2 = len(L2)
        f1 = reduce(lambda x, y: x * 10 + y, list(map(int, L1)))
        f2 = reduce(lambda x, y: x * 10 + y, list(map(int, L2)))
        return f1 + (f2 / pow(10, len_l2))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
