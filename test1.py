#!/usr/bin/env python    # -*- coding: utf-8 -*

day = 345
print day
# 不用声明和定义数据类型，直接赋值

day = 'abc'
print day
# 不同数据类型可以覆盖
print type(day)
# type函数可以输出数据类型

month = []
# 定义一个list
print type(month)
print month

month.append('sads')
print month
# append函数在list中最后添加新的元素

month.append('ssdsa')
print month
# 添加的元素用逗号隔开，不同数据类型也可以添加，同数据类型也要用逗号隔开

month.append(12345)
month.append(234567)
month.reverse()
# list类型中的reverse函数，对list进行翻转
print month
print month[:3]
print month[2:]
# 冒号表示没有边界，:3表示list中从头到第三个，2：表示从第二个到最后
print month[-1]
# list中index索引为负数，代表从后向前找
print len(month)
# len表示长度函数

arr = (1, 2, 3, 1, 6, 7, 2)
print arr.count(1)
# 统计元组中1的个数
print arr.index(2)
# 输出2！第一次！出现的索引下标

print len(arr)
# print arr(1)
print arr[-2]
# 输出元组中index位置的元素和list中一致

print arr[2:]
# 不同的是，输出后仍然是元组，小括号

brr = 1,
print type(brr)
# Python对于有，隔开的输入，默认保存为元组

for i in (1, 2, 3):
    print i
# python中for循环的范围表示为in并且最后为冒号，不是大括号
# 要注意缩进，与javascript一样，有严格的缩进要求

for j in range(5):
    print j

for k in range(1, 5):
    print k

# range的范围左闭右开，不写的话相当于0=<i<5

i = 0

while i < 3:
    i += 1
    print i
# while循环与其他语言类似，不同的是没有括号，最后变成冒号，而不是大括号

# python中没有i++，必须是i+=1 相当于必须是赋值语句，而不是自增操作

print ['a', 'b'] == ['a', 'b']
# list也可以判断内容是否一样，Boolean类型

# if xxx:

# else:
# if和else也是后面加冒号执行
# 而且Python中没有else也可以

# python中0是假，非0就是真

crr = [1, 3, 5, 6, 7, 9]
y = 3 in crr
# 还能这样判断
print y

# 字典用大括号定义
scores = {}
# 先定义一个空字典，然后写入键值对
print type(scores)

scores['a'] = 85
scores['b'] = 80
print scores
print scores['a']
# print scores[1]
# 会跟字典里的key值匹配的
scores[1] = 23
print scores
# 不同数据类型的都能当成key
print 1 in scores
# 判断字典中的key值是否有某一个
print scores.keys()
# 输出字典中所有的key值
data = scores.copy()
# 复制当前字典
print data
scores.clear()
# 清空字典
print scores

# 字典的应用，对有重复的list中统计出现的次数

item = ['abc', 'cda', 'asd', 'sadf', 'abc']
dic = {}

for i in item:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print dic

# python进行文件读写操作

f = open('2016-10-28.log', 'r')
g = f.read()
# r代表read只读，w表示write写入，wr表示读写操作
# 不同的是读取操作前提是目录下必须有该文件，w则可以创建新的文件
# print g
f.close()
# 文件操作结束后要关闭该文件

# 用python的pandas包也能够完成文件操作，不过常用的是to_csv
# csv文件中每一列用逗号分开，所以我们可以按照逗号切分几列的元素

# Python中要有缩进的情况下都有冒号，比如for循环，if，else，或者定义函数def
# 定义函数后还要返回return，其实和其他语言类似的
