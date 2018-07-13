#/usr/bin/python
# -*- coding: utf-8 -*-

# 定义函数
# def function_name(parameter_list):
def my_abs(x):
    if x < 0:
        return -x
    else:
        return x

a = -1
print("a = %d" % a)
print("my_abs(a) = %d" % my_abs(a))


# 导入函数
# 假设python文件名为file.py，该文件包含一个my_abs()函数，可以通过
# from file import my_abs
# 来导入my_abs()函数

# 空函数
# 使用pass作为占位符， pass还可以用到其他地方（如if语句中）
def null_function():
    pass

# 参数检查
# 可以使用isinstance()函数进行数据类型的检查
def my_abs_new(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 可以使用去掉下面两条语句的注释来观察错误信息的不同
# my_abs('A')
# my_abs_new('A')

# 函数返回多个值其实是返回一个tuple
# 在语法上，返回一个tuple时可以省略括号， 而多个变量可以同时接收一个tuple，按位置赋给对应的值。
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print("(x, y) = (%r, %r)" % (x, y))

"""
定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。
"""

# exercise
# 定义一个函数quadratic(a, b, c)，接收三个参数，返回一元二次方程 ax2 + bx + c = 0 的两个解
import math

def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError("bad operand type")
    if not isinstance(b, (int, float)):
        raise TypeError("bad operand type")
    if not isinstance(c, (int, float)):
        raise TypeError("bad operand type")
    delta = b * b - 4 * a * c
    if delta < 0:
        return None, None
    else:
        solve1 = (-b + math.sqrt(delta)) / (2 * a)
        solve2 = (-b - math.sqrt(delta)) / (2 * a)
        return solve1, solve2

# test quadratc()
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
