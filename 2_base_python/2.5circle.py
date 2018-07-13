#/usr/bin/python
# -*- coding: utf-8 -*-

# 循环方式1: for ... in
sum = 0
for x in range(10):
    sum += x
print(sum)

# 循环方式2: while
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(n)
print(sum)

# break 跳出循环

# continue 提前结束本轮循环并进行下一次循环
