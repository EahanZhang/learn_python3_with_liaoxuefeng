#/usr/bin/python
# -*- coding: utf-8 -*-

# 列表生成式： 用于快速的创建list

# 使用for循环生成1*1，2*2, 3*3，... ，10*10
L = []
for i in range(1, 11):
    L.append(i * i)

print(L)

# 使用列表生成式生成上述列表
L1 = [x * x for x in range(1, 11)]
print(L1)

# for循环后还能加上if判断
L2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L2)

# 使用多层循环生成全排列
a = 'ABC'
b = 'DEF'
L3 = [x + y for x in a for y in b]
print(L3)
# 一般不使用三层循环以上的列表生成式
L4 = [x + y + z for x in a for y in a for z in a if x != y and x != z and y != z]
print(L4)


# 使用列表生成式列出当前目录下的所有文件和目录名
import os
L5 = [d for d in os.listdir('.')]
print(L5)

# 列表生成式还可以使用两个甚至多个变量来生成list
d = {'a': 1, 'b': 2, 'c': 3}
L6 = [k + '=' + str(v) for k, v in d.items()]
print(L6)

# 将一个list中的所有字符串变成小写
string_list = ['Abstract', 'INTRODUCTION', 'CONCLUSION']
L7 = [x.lower() for x in string_list]
print(L7)


# exercise
# 如果list中既包含字符串又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错，请修改列表生成式使其能正常运行
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L1)
print(L2)
