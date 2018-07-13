#/usr/bin/python
# -*- coding: utf-8 -*-


# 位置参数
# 调用函数时根据函数定义的参数位置来传递参数
# 如，调用power1()方法时，需要按位置传入两个参数x和n，其中x和n就是位置参数。
def power1(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power1(2, 2))


# 默认参数
# 调用power1()时，如果只传入一个参数时，会因为缺少另一个参数值而产生错误
# 默认参数的作用就是使得调用函数时，如果参数值为默认值，则不需要传入该参数
# 默认参数降低了函数调用的难度，
# **** 定义默认参数要牢记：默认参数必须指向不变对象
def power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power2(5))
print(power2(5, 2))


# 可变参数
# 即，传入的参数个数是可变的，可以是0个到多个
# 在参数前加一个*号即可定义可变参数，函数内部接收到的numbers为一个tuple。
# 因此函数内部的实现细节可以不变，但是可以传入任意非负个数的参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc())
print(calc(1, 2))

# 可以在list或tuple变量前加*号作为参数传入
a = [1, 2, 3]
print(calc(*a))


# 关键字参数
# 关键字参数允许你传入0个或任意多个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。使用**param_name
# 函数person可以通过kw传入任意不受限制的关键字参数，至于判断传入了哪些参数就需要在函数内部通过kw检查。但仍然可以传入不收控制的关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Ehang', 24, city='Beijing')
# 可以使用**dict_name将dict传入到函数中
extra = {'city': 'Beijing', 'job': 'Student'}
person('Ehang', 24, **extra)


# 命名关键字参数
# 用于限制传入的关键字参数的名称
# 命名关键字参数需要用一个特殊的分隔符*，*后面接的参数被视为命名关键字参数
# 如果函数定义中已经有一个可变参数，则后面的命名关键字参数不需要再额外添加*分隔符
# 如下例所示
def person(name, age, *, city, job):
    print(name, age, city, job)

person('Ehang', 24, **extra)


# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，但参数定义的顺序有要求：
# 必选参数 > 默认参数 > 可变参数 > 命名关键字参数 > 关键字参数
# ex
def f1(a, b, c=0, *args, **kw):
    print('a = ', a, 'b = ', b, 'c = ', c, 'args = ', args, 'kw = ', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a = ', a, 'b = ', b, 'c = ', c, 'd = ', d, 'kw = ', kw)

f1(1, 2)
f1(1, 2, 3)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')

# 对于任意函数， 都可以通过类似func(*args, **kw)的形式调用它， 无论其参数时如何定义的
args = (1, 2, 3)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
f2(*args, **kw)


"""
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
"""
