# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 15:38
# @Author  : WuxieYaYa

"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
    1.  1 阶 + 1 阶
    2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

链接：https://leetcode-cn.com/problems/climbing-stairs
"""

## 递归解法
# from functools import lru_cache
#
# @lru_cache()
# def climbStairs(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 2
#     else:
#         return climbStairs(n-1) + climbStairs(n-2)
#


"""
动态规划
"""
def climbStairs(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        dp = [1,2] + [0] * (n-2)

        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]


if __name__ == '__main__':
    print(climbStairs(4))