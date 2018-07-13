#!/usr/bin/python
# -*- coding:utf-8 -*-


# character encoding
# ascii --> unicode --> utf-8

# python string
# python3 使用unicode编码， 因此支持多语言
#
# ord(Character) 获取字符的整数表示
print(ord('A'))
print(ord('中'))
# chr(Integer) 将编码转换成对应的字符
print(chr(65))
print(chr(25991))
#
# 'ABC'与b'ABC'不一样，前者是string，后者是bytes。bytes的每个字符都只占用一个字符。
#
# len()
str = 'ABC'
# len(str) 计算字符的个数
print(len(str))
# len(bytes) 计算字节的个数
# utf-8编码下，中文一般占3个字节，而一个英文字符只占用一个字节
print(len('中文'.encode('utf-8')))
print(len(b'ABC'))


# 格式化
# 使用%格式化字符串
age = 18
print("He is %s years old." % age)
