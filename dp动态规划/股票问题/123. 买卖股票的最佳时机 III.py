    # -*- coding: utf-8 -*-
# @Time    : 2020/3/10 14:40
# @Author  : WuxieYaYa

"""
    给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。设计一个算法来计算你所能获取的最大利润。你最多可以完成两笔交易。
    注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
 """


def maxProfit(prices):
    """
    法1：遍历法，将分割的两部分相加。
    时间：164ms
    空间：14.4MB
    :param prices:
    :return:
    """
    # n = len(prices)
    # new_p = [ele for ele in prices]
    # for i in range(n-1, -1, -1):            # 将连续下降的子序列留下头尾，从而节约计算时间。
    #     if i == 0 or i == n-1:
    #         continue
    #     if prices[i] < prices[i-1] and prices[i] > prices[i+1]:
    #         new_p.pop(i)
    #
    # gaps = [0]
    #
    # def help(section):              # 嵌套函数，目的是计算一个分割块内的最大利润
    #     minprice = 1e9
    #     max_profit = 0
    #     for sec in section:
    #         minprice = min(minprice, sec)
    #         max_profit = max(max_profit, sec - minprice)
    #     return max_profit
    #
    # for j in range(len(new_p) - 1):      # 添加分割点
    #     if new_p[j] > new_p[j + 1]:
    #         gaps.append(j + 1)
    #
    # if len(gaps) == 1:
    #     return help(new_p)
    # ans = [0] * (len(gaps) - 1)
    #
    # for z in range(1, len(gaps)):             #遍历分割点。
    #     ans[z - 1] = help(new_p[gaps[0]:gaps[z]]) + \
    #                  help(new_p[gaps[z]:])
    #
    # return max(ans)

    """
    法2：动态规划dp
    第 1 步：状态定义
        状态定义：dp[i][j] 表示在 [0, i] 区间里（这个状态依然是前缀性质的），状态为 j 的最大收益。j 的含义如下：
        j = 0：还未开始交易；
        j = 1：第 1 次持有（hold)一支股票；
        j = 2：第 1 次卖出(unhold)一支股票；
        j = 3：第 2 次持有一支股票；
        j = 4：第 2 次卖出一支股票。
    第 2 步：状态转移方程
        “状态转移方程”的特点是：状态要么停留，要么向后面走，状态不能回退。
        具体表示式请见代码注释。
        
    第 3 步：思考初始化
        第 0 天的时候很容易初始化前两个状态，而状态 3 （表示第 2 次持股）只能赋值为一个不可能的数。
        注意：只有在之前的状态有被赋值的时候，才可能有当前状态。
        
    第 4 步：思考输出
        最后一天不持股的状态都可能成为候选的最大利润。
        
    第 5 步： 思考状态压缩
        因为今天的值只参考了昨天的值，可以使用“滚动数组”技巧把行数压缩到 2 行（未写代码）。
        并且还注意到它参考的是其它状态昨天的值，因此直接去掉第 1 维即可（结论未确定，但可以通过测评）。
        说明：我一开始怀疑这种状态压缩方法的合理性（评论去已经有朋友提出了同样的质疑）。不倒着写，
        正着写依然可以通过测评。然后思考可以通过的原因：恰好 dp[i][0] 对于任意的 i 都有 dp[i][0] = 0，
        起点都一样，因此可以这样压缩。后面的几道股票问题，在状态压缩的时候，我测试过，有时候，
        颠倒两个状态的赋值过程，依然可以通过测评，理由未知，属强行解释。
        初始化： first_hold = -prices[0] sec_hold = 1e-9
        循环不从0开始，从1开始
        frist_hold = max(fist_hold[-1], frist_unhold - prices[i])
        frist_unhold
        sec_hold
        sec_hold

        作者：liweiwei1419
        链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/dong-tai-gui-hua-by-liweiwei1419-7/
    """
    # todo:dp算法还是有些没有想明白
    n = len(prices)
    if n<2:
        return 0
    frist_hold = -prices[0]
    sec_hold = float('-inf')
    frist_unhold = 0
    sec_unhold = 0

    for i in range(1, n):
        frist_hold = max(frist_hold, - prices[i])
        frist_unhold = max(frist_hold + prices[i], frist_unhold)
        sec_hold = max(frist_unhold - prices[i], sec_hold)
        sec_unhold = max(sec_hold + prices[i], sec_unhold)

    return max(sec_unhold, frist_unhold)


if __name__ == '__main__':
    a = [3,3,5,0,0,3,1,4]
    b = maxProfit(a)
    print(b)

