#/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: Ehang Zhang
@file: 4.4_generator.py
@time: 2018/7/12 17:57
"""

# 生成器
# 生成器与列表生成式相比，不需要占用大量的存储空间。

# 列表生成式comprehension与生成器generator的区别
L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)
print(next(g))

# 当生成器不能生成更多的元素时，抛出StopIteration错误
# 但一般在创建完generator后，基本上永远不会调用next(), 而是使用for...in来迭代它，并且不需要关心StopIteration错误。
g = (x * x for x in range(10))
for n in g:
    print(n)


# 函数与生成器
# 如果一个函数定义中包含yield关键字，则这个函数不再是一个普通的函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(6)
print(f)

# generator和函数的执行流程不一样
# 函数是顺序执行，遇到return或最后一行语句就返回。
# 变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回。 并且再次执行时，从上次返回的yield语句处继续执行。
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3

o = odd()
print(next(o))
print(next(o))
print(next(o))


# 使用for循环来迭代函数generator
for n in f:
    print(n)

# 但是使用for循环迭代函数generator时，无法获得generator的返回值
# 要想取得返回值，必须捕获StopIteration错误， 返回值包含在StopIteration的value中
g = fib(6)
while True:
    try:
        x = next(g)
        print('g: ', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

l = [1, 2, 3]


# exercise
# 试写一个generator，用于输出杨辉三角的下一列
def triangles():
    L = [1]
    while True:
        yield L
        L = L[:]
        L.append(0)
        L = [L[i-1] + L[i] for i in range(len(L))]

# test
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

