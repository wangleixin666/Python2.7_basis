#!/usr/bin/env python    # -*- coding: utf-8 -*

from sklearn.model_selection import KFold
import numpy as np

X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
y = np.array([1, 2, 3, 4])
kf = KFold(n_splits=2)

"""
print kf.get_n_splits(X) 2
print kf.split(X) <generator object split at 0x0000000017A3C480>

"""

for train_index, test_index in kf.split(X):
    print("TRAIN:", train_index, "TEST:", test_index)

"""
#这里kf.split(X)返回的是X中进行分裂后train和test的索引值
令X中数据集的索引为0，1，2，3；
第一次分裂，先选择test，索引为0和1的数据集为test,剩下索引为2和3的数据集为train；
第二次分裂，先选择test，索引为2和3的数据集为test,剩下索引为0和1的数据集为train。
"""

# split(X, y[, groups])
# Generate indices to split data into training and test set.

# get_n_splits([X, y, groups])
# Returns the number of splitting iterations in the cross-validator


