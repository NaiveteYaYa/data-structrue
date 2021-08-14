# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 19:22
# @Author  : WuxieYaYa

"""
    有N件物品和一个容量为V的背包。第i件物品的费用（即体积，下同）是w[i]，价值是val[i]。
求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。
"""


def bagAllocte(V, w, val):
    """
    :param V:  knapsack 容量
    :param w:  物品质量 list
    :param val: 物品价值
    :return:
    """
    n = len(val)
    # B = [[0] * (V+1) for i in range(n)]  # 此处容易出现浅拷贝问题（若用：[[0]*(V+1)]*n,则出现浅拷贝问题）从而使结果有误。
    #
    # for i in range(1, n):
    #     for c in range(1, V+1):
    #         if c < w[i]:
    #             B[i][c] = B[i - 1][c]
    #         else:
    #             B[i][c] = max(B[i - 1][c - w[i]] + val[i], B[i - 1][c])
    #
    # return B[-1][-1]

    """
    状态压缩
    """
    dp = [0] * (V + 1)
    for i in range(1, n):
        for j in range(w[i], V + 1):
            dp[i] = max(dp[i], dp[i - w[i]] + val[i])

    ret


if __name__ == '__main__':
    w = [0, 2, 3, 4, 5, 9]
    val = [0, 3, 4, 5, 8, 10]
    V = 20
    aa = bagAllocte(20, w, val)
    print(aa)
