# -*- coding: utf-8 -*-
# @Time    : 2020/6/14 18:06
# @Author  : WuxieYaYa

"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

链接：https://leetcode-cn.com/problems/subsets-ii
"""


def subsetsWithDup(nums):
    n = len(nums)
    nums.sort()
    ans = []

    def dfs(all_N=n, k=n, res=[]):
        pass


    for i in range(n):
        dfs(all_N=i, i, res=[])






if __name__ == '__main__':
    nums = [1,2,2]
    print(subsetsWithDup(nums))