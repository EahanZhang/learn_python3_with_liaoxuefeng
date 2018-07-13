#/usr/bin/python
# -*- coding: utf-8 -*-

# 切片： 用于快速取得指定范围内的值
L = ['Michael', 'Kobe', 'James', 'Lebron', 'Tracy']
print(L[0:3])
print(L[:3])
print(L[-3:-1])
print(L[-3:])

# 按频率为t取数 list[a:b:c]表示在a到b的区间内以c为间隔取数
print(L[::2])

# 什么都不写，可以复制一个list: list[:]
print(L[:])

# tuple也是一种list, 只不过tuple不可变。 因此也可以对tuple进行切片操作， 只是操作的结果仍为tuple
print((0, 1, 2, 3, 4, 5)[:3])

# sing也是一种list，每个元素就是一个字符。 因此sing也可以进行切片操作
print('ABCDEFGH'[:3])


# exercise
# 利用切片操作，实现一个trim()函数。 不要使用s的sip()方法
def trim(s):
    if s is None or len(s) == 0:
        return s

    len_s = len(s)

    i = 0
    while s[i] == ' ' and i < len_s - 1:
        i += 1
    start_index = i

    i = len_s - 1
    while s[i] == ' ' and i >= start_index:
        i -= 1
    end_index = i

    return s[start_index:end_index + 1]

print(trim(''))
print(trim('hello     '))
print(trim('     hello'))
print(trim('    hello     '))
print(trim('  '))

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
