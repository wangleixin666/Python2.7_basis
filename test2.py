# -*- coding: utf-8 -*

# import math
# right

# print math.exp(2)

# -*- coding:utf-8 -*-


def Find(target, array):
    for i in range(0, len(array)):
        for j in range(0, len(array[0])):
            if array[i][j] == target:
                return True

    return False

A = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print Find(11, A)

# write code here

# import exp
# wrong，不能直接导入类

# print ext(2)


