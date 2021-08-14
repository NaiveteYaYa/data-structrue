# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 16:02
# @Author  : WuxieYaYa

"""
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

链接：https://leetcode-cn.com/problems/edit-distance
"""


def minDistance(word1, word2):
    n_1, n_2 = len(word1), len(word2)

    D = [[0] * (n_2+1) for _ in range(n_1+1)]

    for i in range(n_1+1):
        D[i][0] = i
    for j in range(n_2+1):
        D[0][j] = j

    for i in range(1, n_1+1):
        for j in range(1, n_2+1):
            if word1[i-1] != word2[j-1]:
                # todo 这部分还没有完全清楚
                D[i][j] = min(D[i-1][j], D[i-1][j-1], D[i][j-1]) + 1
            else:
                D[i][j] = D[i-1][j-1]

    return D[-1][-1]

if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    print(minDistance(word1, word2))




