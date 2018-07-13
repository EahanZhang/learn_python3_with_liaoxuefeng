#/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: Ehang Zhang
@file: 5.1.2_filter.py
@time: 2018/7/13 11:17
"""

# filter()函数用于过滤序列
# filter(function_name, iterable)
# filter()函数把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定是否保留该元素。
# filter()函数返回的也是一个惰性序列Iterator
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, range(20))))


# 用filter求素数
"""
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：

首先，列出从2开始的所有自然数，构造一个序列：

取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：

取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：

取新序列的第一个数5，然后用5把序列的5的倍数筛掉：

不断筛下去，就可以得到所有的素数。
"""

# 1. 构造一个从3开始的奇数序列， 因为所有除2以外的偶数都是非素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 2. 定义一个筛选函数
def _not_divisiable(n):
    return lambda x : x % n > 0 # 这里的x是从53行中的it里得到的

# 3. 定义一个生成器， 不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 取出当前it序列中的第一个数
        yield n
        it = filter(_not_divisiable(n), it) # 过滤掉能整除n的数

for n in primes():
    if n < 30:
        print(n)
    else:
        break


# exercise
# 判断是否为回数
def is_palindrome(n):
    if not isinstance(n, (int)):
        raise TypeError
    str_n = str(n)
    if str_n == str_n[::-1]:
        return True
    else:
        return False

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
