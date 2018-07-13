#/usr/bin/python
# -*- coding: utf-8 -*-

# dict
# dict使用键值对的方式存储数据
dict = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print("Michael's score: %d" % dict['Michael'])

# 避免key不存在的方法
# 1. 使用in判断key是否存在
print('Thomas' in dict)
# 2. 使用get()方法，如果key不存在，则返回None或指定的值
print(dict.get('Thomas'))
print(dict.get('Thomas', -1))

# 删除一个key
print("Before pop, the dict is:", dict)
dict.pop("Tracy")
print("After pop, the dict is:", dict)

# dict与list的比较
#
# dict
# 优点：查找和插入的速度极快（使用索引），不会随着key的增加而变慢
# 缺点：需要占用大量的内存，内存浪费多
#
# list
# 优点：占用空间小，浪费内存少
# 缺点：查找和插入的时间随元素的增加而增加


# set 集合
# 集合中的不存在重复的元素

# 创建一个set需要提供一个list作为输入集合
s = set([1, 2, 3])
print(s)

# 重复元素在set中自动被过滤
s = set([1, 1, 2, 2, 3, 3])

# 使用add()方法向集合中添加元素
print("Before add element, the set is: ", s)
s.add(4)
print("After add element, the set is: ", s)

# 使用remove()方法从集合中删除元素
print("Before remove element, the set is: ", s)
s.remove(4)
print("After remove element, the set is: ", s)

# set可以看做数学意义上无序和无重复元素的集合，因此，两个集合可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print("s1 & s2: ", s1 & s2)
print("s1 | s2: ", s1 | s2)

