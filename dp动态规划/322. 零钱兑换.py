# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 11:10
# @Author  : WuxieYaYa

"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1

说明:
你可以认为每种硬币的数量是无限的。

链接：https://leetcode-cn.com/problems/coin-change
"""

import math

def coinChange(coins, amount):
    """
    法1 ： 动态规划
        1500ms
    """

    # dp = [float('inf')] * (amount + 1)
    # dp[0] = 0
    # for j in coins:
    #     # for i in range(1, amount+1):
    #     #     dp[i] = min(dp[i - j] + 1 if i - j >= 0 else float('inf'), dp[i])
    #     """此处优化, 避免出现负数情况"""
    #     for i in range(j, amount+1):
    #         dp[i] = min(dp[i - j] + 1, dp[i])
    #
    # return dp[-1] if dp[-1] != float('inf') else -1

    """
    法2 ： dfs
    时间更短，50ms
    """
    n = len(coins)
    coins = sorted(coins, reverse=True)
    res = amount + 1

    def dfs(index, target, count):
        nonlocal res
        this_coin = coins[index]
        if count + math.ceil(target / this_coin) >= res:
            return

        if target % this_coin == 0:
            res = count + target // this_coin

        if index == n - 1:
            return

        for i in range(target // this_coin, -1, -1):
            dfs(index + 1, target - i * this_coin, count + i)

    dfs(0, amount, 0)
    return -1 if res == amount + 1 else res


if __name__ == '__main__':
    coins = [5]
    amount = 11
    print(coinChange(coins, amount))


