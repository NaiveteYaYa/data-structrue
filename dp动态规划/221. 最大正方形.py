# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 11:19
# @Author  : WuxieYaYa
"""
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4

链接：https://leetcode-cn.com/problems/maximal-square
"""


def maximalSquare(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    c, r = len(matrix), len(matrix[0])
    dp = [[0] * r for _ in range(c)] #深拷贝
    ans = 0
    for i in range(c):
        for j in range(r):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1

            if dp[i][j] > ans:
                ans = dp[i][j]

    return ans * ans


if __name__ == '__main__':
    ma = [[1, 0, 1, 0, 0],
          [1, 0, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 0, 0, 1, 0]]
    # ma = [[1,1],[1,1]]
    print(maximalSquare(ma))
