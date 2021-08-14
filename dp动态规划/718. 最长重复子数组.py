# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 18:14
# @Author  : WuxieYaYa

"""
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例：

输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。
 

提示：

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def findLength(A, B):
    """法1： dp"""
    # a = len(A)
    # b = len(B)
    # dp = [[0] * (a + 1) for _ in range(b + 1)]
    # ans = 0
    # for i in range(1, a + 1):
    #     for j in range(1, b + 1):
    #         if A[i - 1] == B[j - 1]:
    #             dp[i][j] = dp[i - 1][j - 1] + 1
    #         else:
    #             continue
    #
    #         ans = max(ans, dp[i][j])
    #
    # return ans

    """法2： 滑动窗口"""
    a = len(A)
    b = len(B)
    if a < b:
        return findLength(B, A)

    