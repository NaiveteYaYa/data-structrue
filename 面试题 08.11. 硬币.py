# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 10:40
# @Author  : WuxieYaYa

"""
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。
(结果可能会很大，你需要将结果模上1000000007)

示例1:

 输入: n = 5
 输出：2
 解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1
示例2:

 输入: n = 10
 输出：4
 解释: 有四种方式可以凑成总金额:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1
说明：

注意:

你可以假设：

0 <= n (总金额) <= 1000000

链接：https://leetcode-cn.com/problems/coin-lcci
"""


def waysToChange(n):
    # TODO:jixu
    if n==0:
        return 0
    d = [0] * (n+1)
    for i in range(1,n+1):
        d[i] = d[i]


if __name__ == '__main__':
    n = 45
    print(waysToChange(n))
