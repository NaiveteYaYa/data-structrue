# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 14:49
# @Author  : WuxieYaYa

"""
    给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
    你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
    返回获得利润的最大值。

示例 1:

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
注意:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.

链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
"""
"""
利用动态规划:
如果只有连个状态，那么它们必须是互补的
初始化
hold = -prices[0]
sell = 0
遍历
unhold = max[unhold[-1], hold + prices[i] -2]    # 卖出：1.前一个状态不持有，2.前一个状态hold，这个状态不持有
hold = max[hold[-1], unhold[-1] - prices[i]] # 买入：1.前个状态卖出，2 前一个状态不变

"""


def maxProfit(prices, fee):             # [1, 3, 2, 8, 4, 9]
    hold = -prices[0]
    unhold = 0
    for price in prices[1:]:
        pre_unhold = unhold
        unhold = max(unhold, hold + price - fee)    # 0 , 0
        hold = max(pre_unhold - price, hold)  # -1,

    return unhold
"""
fb (n):
for i in range(2:n):

"""


if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    resul = maxProfit(prices, fee)
    print(resul)
