#/usr/bin/python
# -*- coding: utf-8 -*-

# 迭代：使用for...in遍历某个list或tuple或dict等

# 遍历list
list = [1, 2, 3, 4, 5]
for value in list:
    print(value)

# 遍历dict的key
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print("key: ", key)

# 遍历dict的value
for value in d.values():
    print("value: ", value)

# 同时遍历dict的key和value
for key, value in d.items():
    print("(key, value): (%r, %r)" % (key, value))


# 判断一个对象是否为可迭代对象
from collections import Iterable
print(isinstance('abc', Iterable)) # string
print(isinstance([1, 2, 3], Iterable)) # list
print(isinstance(123, Iterable)) # integer


# 使用enumerate()方法将list变成键值对
for i, value in enumerate([1, 2, 3]):
    print("(index, value): (%r, %r)" % (i, value))


# exercise
# 使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if L is None or len(L) == 0:
        return None, None
    elif len(L) == 1:
        return L[0], L[0]
    else:
        min = L[0]
        max = L[0]
        for value in L[1:]:
            if value < min:
                min = value
            elif value > max:
                max = value
            else:
                pass

        return min, max


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
