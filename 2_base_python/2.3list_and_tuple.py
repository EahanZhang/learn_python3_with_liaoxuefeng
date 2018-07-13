#/usr/bin/python
# -*- coding: utf-8 -*-

# list 一种有序的集合，可以随时添加和删除其中的元素
classmates = ['Michael', 'Bob', 'Tracy']
#
# len(list) 获取list中元素的个数
print("classmates' length: %d" % len(classmates))
# 索引从0开始
for i in len(classmates):
    print("index %d: %d" % (i, classmates[i]))
# 可以使用list[-1]来获得最后一个元素
print("index -1: %d" % classmates[-1])
# 可以使用list[-n]来获得倒数第n个元素
#
# list.append() 用于添加元素到list中
classmates.append("Ehang")
print("After append, ", classmates)
# list.insert(i, element) 将元素element添加到指定位置i中
classmates.insert(len(classmates), "Zhang")
print("After insert, ", classmates)
#
#
# list.pop() 删除list末尾的元素
classmates.pop()
print("After pop, ", classmates)
# list.pop(i) 删除指定位置的元素
classmates.pop(len(classmates) - 1)
print("After pop(i), ", classmates)
#
# list[i] = value 直接给指定的索引位置赋值
classmates[-1] = "Kobe"
print("After give value directly, ", classmates)

# list中元素的类型可以不一样
variable_list = ['Bryant', 123, True]
print("A list can contain different types of element, ", variable_list)

# list中还可以包含list
embedded_list = [1, 2, [3, 4], 5]
print("A list can contain another list, ", embedded_list)


# tuple 元组
# tuple与list类似，但tuple一旦初始化后就不能再更改(更底层的解释是，tuple的每个元素，其指向永远不变)
simple_tuple = (1, 2, 3)

# tuple没有append()和pop()以及insert()等函数
# 由于tuple不能被修改，因此比list安全， 所以能用tuple应该尽量避免使用list

# 定义单个元素的tuple, 如果使用 t = (1), 则t实际上保存的一个数1而不是元组
tuple_have_only_one_element = (1,)

# 可变的元组
changeable_tuple = (1, 2, [3, 4], 5)
print("Before change, the tuple is: ", changeable_tuple)
changeable_tuple[2][0] = 88
changeable_tuple[2][1] = 99
print("After change, the tuple is: ", changeable_tuple)


# Exercise
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])


