# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 12:34
# @Author  : WuxieYaYa


"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。
示例 1:
输入: 2.00000, 10
输出: 1024.00000
示例 2:
输入: 2.10000, 3
输出: 9.26100
示例 3:
输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:
-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

链接：https://leetcode-cn.com/problems/powx-n
"""


def myPow(x, n):
    """
    此法超时
    :param x:
    :param n:
    :return:
    """
    ans = 1
    n = abs(n)
    if n==0:
        return 1
    if x==0 and n!=0:
        return 0
    for i in range(n):
        ans **= x
    return ans if n>0 else 1/ans

