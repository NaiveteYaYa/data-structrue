# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 14:21
# @Author  : WuxieYaYa

"""
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。

示例:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]

说明:

给定矩阵中的元素总数不会超过 100000

链接：https://leetcode-cn.com/problems/diagonal-traverse
"""
from itertools import cycle

def findDiagonalOrder(matrix):
    if matrix == [] or matrix[0] == []:
        return []
    ans = []
    r = len(matrix)
    c = len(matrix[0])
    direct = ['up', 'down']
    i = 0
    j = 0
    for dire in cycle(direct):
        if i == r-1 and j == c - 1:
            ans.append(matrix[-1][-1])
            break
        if dire == 'up':
            ans.append(matrix[i][j])
            while True:
                if i == 0 or j == c-1:
                    break
                else:
                    i -= 1
                    j += 1
                ans.append(matrix[i][j])
            if j != c-1:
                j += 1
            else:
                i += 1
        if dire == 'down':
            ans.append(matrix[i][j])
            while True:
                if i==r-1 or j==0:
                    break
                else:
                    i += 1
                    j -= 1
                ans.append(matrix[i][j])
            if i != r-1:
                i += 1
            else:
                j += 1
    return ans


if __name__ == '__main__':
    ma = [[1,2,3],[4,5,6],[7,8,9]]
    ma = [[]]
    print(findDiagonalOrder([]))