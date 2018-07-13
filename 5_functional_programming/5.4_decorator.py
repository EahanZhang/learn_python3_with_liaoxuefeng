#/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: Ehang Zhang
@file: 5.4_decorator.py
@time: 2018/7/13 16:26
"""

# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数


def now():
    print("2018-07-13")


f = now
f()

# 函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)
print(f.__name__)

# 假设我们需要增强now()的功能，又不想修改now()的定义，这种在代码运行期间动态增加功能的方式就叫做装饰器(Deractor)
# 本质上，decorator就是一个返回函数的高阶函数。


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 使用decorator时，需要借助Python的@语法，将decorator置于函数的定义处：
# 将@log放置到hello()函数的定义处，相当于执行了语句hello = log(hello)
@log
def hello():
    print('Hello World')


hello()

# decorator需要传入参数，则需要编写一个返回decorator的高阶函数


def logs(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@logs('execute')
def hello_again():
    print("Hello, new world")


hello_again()
# 经过decorator装饰的函数，其自带属性已经发生了变化
# 比如hello_again的__name__属性已经从hello_again变成了wrapper
print(hello_again.__name__)
# 因此需要将原始函数的自带属性复制到wrapper中， Python中内置的functools.wraps就是干这个的
# 因此一个完整的装饰器如下：
import functools


def logs_complete(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@logs_complete('execute')
def hello_world():
    print('Hello World')


hello_world()
print(hello_world.__name__)


# exercise
# 请设计一个decorator，它可以作用于任何函数上，并且打印该函数的执行时间
import time, functools


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('%s executec in %s ms' % (fn.__name__, time.time()))
        return fn(*args, **kw)
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
