# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 16:57
# @Author  : WuxieYaYa

"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
"""
"""
每天可能存在三种状态：

hold：继续持有股票
sold：卖出股票
rest：什么都不做
转换关系如下：

sold：
前一天hold，当日卖出股票
hold： 可由两个情况转换来
前一天hold，当日rest
前一天rest，当日买入股票变为hold
rest：
前一天sold，当日必须rest
前一天rest，当日继续rest
所以

sold[i] = hold[i-1] + price[i];
hold[i] = max(hold[i-1], rest[i-1] - price[i])
rest[i] = max(rest[i-1], sold[i-1])
最后一天最大值情况为要么什么都不做，要么卖出股票，即 max(sold，rest)。

作者：guohaoding
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/309-zui-jia-mai-mai-gu-piao-shi-ji-han-leng-dong-q/
"""


def maxProfit(prices):
    hold = -1e9
    sell = 0
    rest = 0
    for price in prices:
        pre_sold = sell
        sell = hold + price
        hold = max(hold, rest - price)
        rest = max(rest, pre_sold)

    return max(sell, rest)


if __name__ == '__main__':
    a = [1, 2, 3, 0, 2]
    resul = maxProfit(a)
    print(resul)
