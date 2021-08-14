# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 22:06
# @Author  : WuxieYaYa

"""
给定一个整数的数组，相邻的数不能同时选，求从该数组选取若干整数，使得他们的和最大，
"""

import numpy as np

arr = [1, 2, 3, 1, 7, 8, 3]


# 递归，recursion
def rec_opt(arr, i):
    if i==0:
        return arr[0]
    if i==1:
        return max(arr[0], arr[1])
    else:
        A = rec_opt(arr, i-2) + arr[i]
        B = rec_opt(arr, i-1)
        return max(A, B)

# 动态规划就是递归算法自底向上的
def dp_opt(arr):
    opt = np.zeros(len(arr))
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        A = opt[i-2] + arr[i]
        B = opt[i-1]
        opt[i] = max(A, B)

    return opt[len(arr) - 1]

arr1 = [3,34, 4, 12,5,2]

def rec_subset(arr, i, s):
    if s == 0:
        return True
    elif i == 0:
        return arr[i] == s
    elif arr[i] > s:
        return rec_subset(arr, i-1, s)
    else:
        A = rec_subset(arr, i-1, s-arr[i])
        B = rec_subset(arr, i-1, s)
        return A or B

def dp_subset(arr, S):
    subset = np.zeros((len(arr), S+1),dtype=bool)
    subset[:, 0] = True
    subset[0, :] = False
    subset[0, arr[0]] = True
    for i in range(1, len(arr)):
        for s in range(1, S+1):
            if arr[i] > s:
                subset[i, s] = subset[i-1, s]











if __name__ == '__main__':
    print(rec_opt(arr, 6))
    print(dp_opt(arr))
    print(rec_subset(arr1,len(arr1)-1, 9))
