#/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: Ehang Zhang
@file: 5.2_return_function.py
@time: 2018/7/13 14:14
"""

# 函数可以作为返回值
#
# calc_sum()立即求和
def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax

# lazy_sum()返回一个函数，并不立即求和
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax

    return sum

f = lazy_sum(1, 3, 4, 5 ,6)
print(f)
print(f())

# !! 每当调用一次lazy_sum()时，都会返回一个新函数， 即使传入相同的参数
f1 = lazy_sum(1, 3, 4, 5 ,6)
f2 = lazy_sum(1, 3, 4, 5 ,6)
print(f1 == f2)

# !!! 返回的函数并没有立即执行，而是直到调用了f()才执行
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

# !!! 返回闭包时请牢记： 返回函数不要引用任何循环变量，或者后续会发生变化的变量。


# exercise
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def create_counter():
    def helper():
        n = 1
        while True:
            yield n
            n = n + 1

    it = helper()

    def counter():
        return next(it)


    return counter

# 测试:
counterA = create_counter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = create_counter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


