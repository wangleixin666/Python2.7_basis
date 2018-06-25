#!/usr/bin/env python    # -*- coding: utf-8 -*


def binarysearch(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) / 2
        # print mid
        if list[mid] > item:
            high = mid
            # print 'big'
        elif list[mid] < item:
            low = mid + 1
            # print 'small'
        else:
            return mid
            # 返回索引
    print 'end'
    return None
    # 也就是说上述while循环判断都没有的话，返回None


A = [1, 3, 4, 7, 9]

print binarysearch(A, 8)
