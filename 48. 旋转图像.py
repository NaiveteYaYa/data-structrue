# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 0:11
# @Author  : WuxieYaYa

"""
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
示例 1:
给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-image
"""


def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    # from copy import deepcopy
    # copy = deepcopy(matrix)
    # n = len(matrix[0])
    # for i in range(n // 2):
    #     for z in range(i, n - i):
    #         matrix[i][z] = copy[n - z - 1][i]  # 第一行
    #         matrix[z][i] = copy[n - i - 1][z]  # 第一列
    #         matrix[n - i - 1][z] = copy[n - 1 - z][n - i - 1]  # 最后一行
    #         matrix[z][n - i - 1] = copy[i][z]  # 最后一列
    # return

    """
    法2：方法 1 ：转置加翻转
    最直接的想法是先转置矩阵，然后翻转每一行。这个简单的方法已经能达到最优的时间复杂度O(N^2)O(N^2)。
    """
    n = len(matrix[0])
    # transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

            # reverse each row
    for i in range(n):
        matrix[i].reverse()


if __name__ == '__main__':
    a = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ]
    """
    [[7,4,1],
     [8,5,2],
     [9,6,3]]
    """
    rotate(a)
    print(a)
