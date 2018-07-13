#/usr/bin/python
# -*- coding: utf-8 -*-

# 递归函数
# 如果一个函数在内部调用自身本身，则这个函数就是递归函数
def fact(x):
    if x == 1:
        return x
    return x * fact(x - 1)

print(fact(1))
print(fact(5))

# 栈溢出
# 在计算机中，函数调用是通过栈(Stack)这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧
# 每当函数返回时，栈就会减少一层栈帧
# 由于栈的大小不是无限的，因此递归调用的次数过多会导致栈溢出。
# print(fact(1000)) 就会导致栈溢出

# 尾递归：使用尾递归优化可以解决递归调用栈溢出的问题
# 尾递归是指，在函数返回的时候，调用自身本身， 并且return语句不能包含表达式。
# 这样编译器或者解释器就可以把尾递归做优化，使递归本身不论被调用多少次，都只占有一个栈帧，从而不会出现栈溢出的情况

# 遗憾的是，大多数编程语言没有针对尾递归作优化，Python解释器也没有。 因此Python中的任何递归函数都存在栈溢出的情况。
def new_fact(n):
    return fact_iterator(n, 1)


def fact_iterator(num, product):
    if num == 1:
        return product
    return fact_iterator(num - 1, num * product)


# 小结
"""
使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
"""


# exercise
# Tower of Hanoi
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)

move(3, 'A', 'B', 'C')
