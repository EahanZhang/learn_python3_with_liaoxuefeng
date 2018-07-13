#/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: Ehang Zhang
@file: 5.5_partial_function.py
@time: 2018/7/13 17:26
"""

# 偏函数，通过设定参数的默认值，来简化函数调用的难度
# functools.partial(func_name, param_value)
import functools
int2 = functools.partial(int, base=2)
print(int2('10010'))
print(int2('11111'))
