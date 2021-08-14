# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 21:31
# @Author  : WuxieYaYa

"""
有 N 种物品和一个容量是 V 的背包。

第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。

输入格式
第一行两个整数，N，V用空格隔开，分别表示物品种数和背包容积。

接下来有 N 行，每行三个整数 vi,wi,si用空格隔开，分别表示第 i 种物品的体积、价值和数量。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N,V≤1000
0<vi,wi,si≤100
"""


def knapsack(N, V, v, w, s):
    """
    二维解法。
    """
    # dp = [[0] * (V + 1) for _ in range(N+1)]
    # v = [0] + v
    # w = [0] + w
    # s = [0] + s
    # for i in range(1, N + 1):
    #     for c in range(v[i], V + 1):
    #         if c <= s[i] * v[i]:
    #             dp[i][c] = max(dp[i-1][c], dp[i][c-v[i]] + w[i])
    #         else:
    #             dp[i][c] = max(dp[i-1][c], dp[i-1][c-s[i]*v[i]] + s[i] *w[i])
    #
    # return dp

    """
    状态压缩：
        将  for c in range(v[i], V + 1)改为循环倒序遍历，则为：
            for c in range(V, v[i]-1, -1):  这样可以避免，v[i]的重复计数，使得v[i]的装袋次数不超过s[i]
                for k in range(s[i]+1)
                dp[c] = max(dp[c], dp[c-K*v[i]]+ k*w[i])
                
                    
                    
    """


if __name__ == '__main__':
    """
    v,  w,  s |1    2   3   4   5   6   7   8   9   10
    1   2   1 |2    2   2   2   2   2   2   2   2   2
    2   3   4 |2    3   5   6   8   9   11  12  12  12
    """
    v = [1, 2, 3, 4, 5]
    w = [2, 3, 7, 7, 9]
    s = [1, 2, 1, 4, 5]
    aa = knapsack(5, 10, v, w, s)
    print(aa)
