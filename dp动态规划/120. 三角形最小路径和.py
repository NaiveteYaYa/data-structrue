# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 8:06
# @Author  : WuxieYaYa

"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

链接：https://leetcode-cn.com/problems/triangle
"""


def minimumTotal(triangle):

    n = len(triangle)
    dp = [[0] *n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        dp[i][0] = triangle[i][0] + dp[i-1][0]
        for j in range(1, i):
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

        dp[i][i] = dp[i-1][i-1] + triangle[i][i]

    return min(dp[-1])


if __name__ == '__main__':
    a = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(minimumTotal(a))
