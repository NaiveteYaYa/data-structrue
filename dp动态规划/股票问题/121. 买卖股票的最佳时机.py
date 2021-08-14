# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 14:35
# @Author  : WuxieYaYa


"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
"""

def text(prices):
    ans = 0
    min_v = 1e9
    for p in prices:
        if p < min_v:
            min_v = p
        if p > min_v and ans < (p - min_v):
            ans = p - min_v

    return ans




def maxProfit(prices):
    """
    暴力法：此法超时
    """
    # top = 0
    # for idx, price in enumerate(prices):
    #     for i in range(idx+1, len(prices)):
    #         if top < prices[i]-price:
    #             top = prices[i] - price
    #
    # return top

    """
    一次遍历法
    """
    # minprice = 1e9
    # max_profit = 0
    #
    # for price in prices:
    #     minprice = min(minprice, price)
    #     max_profit = max(max_profit, price - minprice)
    #
    # return max_profit

    """
    dp:动态规划
    方法二：动态规划
        动态规划一般分为一维、二维、多维（使用状态压缩），对应形式为 dp(i)dp(i)、dp(i)(j)dp(i)(j)、二进制dp(i)(j)二进制dp(i)(j)。
        
        1. 动态规划做题步骤
        明确 dp(i)dp(i) 应该表示什么（二维情况：dp(i)(j)dp(i)(j)）；
        根据 dp(i)dp(i) 和 dp(i-1)dp(i−1) 的关系得出状态转移方程；
        确定初始条件，如 dp(0)dp(0)。
        2. 本题思路
        
        其实方法一的思路不是凭空想象的，而是由动态规划的思想演变而来。这里介绍一维动态规划思想。
        dp[i]dp[i] 表示前 ii 天的最大利润，因为我们始终要使利润最大化，则：
                dp[i] = max(dp[i-1], prices[i]-minprice)
            
        作者：z1m
        链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/gu-piao-wen-ti-python3-c-by-z1m/
    """
    n = len(prices)
    if n == 0:
        return 0  # 边界条件
    dp = [0] * n
    minprice = prices[0]

    for i in range(1, n):
        minprice = min(prices[i], minprice)
        dp[i] = max(prices[i] - minprice, dp[i - 1])

    return dp[-1]


if __name__ == '__main__':
    a = [7, 1, 5, 3, 6, 4, 8]
    print(maxProfit(a))
