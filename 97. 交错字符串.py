# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 10:45
# @Author  : WuxieYaYa

"""
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false

链接：https://leetcode-cn.com/problems/interleaving-string
"""

import typing

def isInterleave(s1: str, s2: str, s3: str) -> bool:
    """动态规划"""
    size1, size2 = len(s1), len(s2)
    if "" in (s1, s2): return s3 in (s1, s2)
    if size1 + size2 != len(s3):
        return False

    dp = [[False] * (size2 + 1) for _ in range(size1 + 1)]
    dp[0][0] = True
    print(dp)
    for i in range(size1 + 1):
        for j in range(size2 + 1):
            p = i + j - 1
            if i > 0:
                # print(f"{i,j}")
                # print(s1[i - 1] == s3[p])
                # print(dp[i][j],f"{i,j}")

                dp[i][j] |= dp[i     - 1][j] and s1[i - 1] == s3[p]
            if j > 0:
                dp[i][j] |= dp[i][j - 1] and s2[j - 1] == s3[p]

    return dp[-1][-1]


if __name__ == '__main__':
    s1 = "db"
    s2 = "b"
    s3 = "cbb"
    print(isInterleave(s1,s2,s3))
