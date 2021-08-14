# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 15:13
# @Author  : WuxieYaYa

"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
"""

def text(prices):
    ans = 0

    min_v = 1e9
    ...

def maxProfit(prices):
    """
    该解决方案:
        我们可以简单地继续在斜坡上爬升并持续增加从连续交易中获得的利润，而不是在谷之后寻找每个峰值。
        最后，我们将有效地使用峰值和谷值，但我们不需要跟踪峰值和谷值对应的成本以及最大利润，
        但我们可以直接继续增加加数组的连续数字之间的差值，如果第二个数字大于第一个数字，
        我们获得的总和将是最大利润。这种方法将简化解决方案。

    链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-ii-by-leetcode/

    """
    n = len(prices)
    max_profit = 0

    for i in range(1, n):
        if prices[i] >= prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    return max_profit


if __name__ == '__main__':
    a = [7, 1, 5, 3, 6, 4, 8]
    print(maxProfit(a))
