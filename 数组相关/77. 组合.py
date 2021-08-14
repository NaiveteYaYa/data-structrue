# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 23:35
# @Author  : WuxieYaYa

"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

链接：https://leetcode-cn.com/problems/combinations
"""

def combine(n, k):
    l = [i + 1 for i in range(n)]
    ans = []
    def dfs(li=l, p=k, res=[]):
        if p == 0:
            t = [i for i in res]
            ans.append(t)
            return
        length = len(li)
        for i in range(length-p+1):
            res.append(li[i])
            dfs(li[i + 1:], p-1, res)
            res.pop()

    dfs(li=l, p=k, res=list())
    return ans



if __name__ == '__main__':
    print(combine(4,2))