# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 15:21
# @Author  : WuxieYaYa

""""
有 N种物品和一个容量是 V 的背包，每种物品都有无限件可用。
第 i种物品的体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

输入格式
第一行两个整数，N，VN，V，用空格隔开，分别表示物品种数和背包容积。

接下来有 NN 行，每行两个整数 vi,wivi,wi，用空格隔开，分别表示第 ii 种物品的体积和价值。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N,    V≤1000
0<vi,   wi≤1000
输入样例
4 5
1 2
2 4
3 4
4 5
输出样例：
10
"""


def bagAllocte(V, w, val):
    """
        与0-1背包问题不同点在于：无限可用，其实无限次也是有次数的，空间C，物品重量w[i]，次数 k = c/w[i]
    首先dp数组初始化全为0：给定物品种类有4种，包最大体积为5，数据来源于题目的输入
    w[1] = 1, val[1] = 2
    w[2] = 2, val[2] = 4
    w[3] = 3, val[3] = 4
    w[4] = 4, val[4] = 5

    i = 1 时： j从v[1]到5
    dp[1] = max(dp[1],dp[0]+val[1]) = val[1] = 2 (用了一件物品1）
    dp[2] = max(dp[2],dp[1]+val[1]) = val[1] + val[1] = 4（用了两件物品1）
    dp[3] = max(dp[3],dp[2]+val[1]) = val[1] + val[1] + val[1] = 6（用了三件物品1）
    dp[4] = max(dp[4],dp[3]+val[1]) = val[1] + val[1] + val[1] + val[1] = 8（用了四件物品1）
    dp[5] = max(dp[3],dp[2]+val[1]) = val[1] + val[1] + val[1] + val[1] + val[1] = 10（用了五件物品）

    i = 2 时：j从v[2]到5
    dp[2] = max(dp[2],dp[0]+val[2]) = val[1] + val[1] = val[2] =  4（用了两件物品1或者一件物品2）
    dp[3] = max(dp[3],dp[1]+val[2]) = 3 * val[1] = val[1] + val[2] =  6（用了三件物品1，或者一件物品1和一件物品2）
    dp[4] = max(dp[4],dp[2]+val[2]) = 4 * val[1] = dp[2] + val[2] =  8（用了四件物品1或者，两件物品1和一件物品2或两件物品2）
    dp[5] = max(dp[5],dp[3]+val[2]) = 5 * val[1] = dp[3] + val[2] =  10（用了五件物品1或者，三件物品1和一件物品2或一件物品1和两件物品2）

    i = 3时：j从v[3]到5
    dp[3] = max(dp[3],dp[0]+val[3]) = dp[3] = 6 # 保持第二轮的状态
    dp[4] = max(dp[4],dp[1]+val[3]) = dp[4] = 8 # 保持第二轮的状态
    dp[5] = max(dp[5],dp[2]+val[3]) = dp[4] = 10 # 保持第二轮的状态

    i = 4时：j从v[4]到5
    dp[4] = max(dp[4],dp[0]+val[4]) = dp[4] = 10 # 保持第三轮的状态
    dp[5] = max(dp[5],dp[1]+val[4]) = dp[5] = 10 # 保持第三轮的状态

    上面模拟了完全背包的全部过程，也可以看出，最后一轮的dp[m]即为最终的返回结果。

    作者：polaris
    链接：https://www.acwing.com/solution/acwing/content/3986/
    """
    w = [0] + w
    val = [0] + val
    n = len(w)
    B = [[0] * (V + 1) for _ in range(n)]
    for i in range(1, n):
        for c in range(1, V + 1):
            if c < w[i]:
                B[i][c] = B[i-1][c]
            else:
                """
                B[i][c] = max(B[i - 1][c], B[i - 1][c - w[i]] + val[i]) # 0-1背包问题,状态转移方程。
                不同之处：
                    0-1问题，因为拿了就没了，所以B[i - 1],而完全问题不存在，所以为B[i]。
                """
                B[i][c] = max(B[i - 1][c], B[i][c - w[i]] + val[i])
    return B

    """
    状态压缩
    """
    # dp = [0] * (V + 1)
    # for i in range(1, n):
    #     for j in range(w[i], V + 1):
    #         dp[j] = max(dp[j], dp[j - w[i]] + val[i])
    #
    # return dp


if __name__ == '__main__':
    w = [1, 2, 3, 4, 5]
    val = [2, 3, 7, 7, 9]
    a = bagAllocte(7, w, val)
    print(a)
