# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 9:31
# @Author  : WuxieYaYa

"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

链接：https://leetcode-cn.com/problems/permutations
"""
from collections import deque
from itertools import groupby,permutations
def permute(nums):
    # 解法1：
    # n = len(nums)
    # ans = []
    # seq = [i for i in range(len(nums))]
    #
    # def dfs(alist, head=[], s=seq):
    #     """
    #
    #     :type s: List
    #     """
    #     for i in s:
    #         head.append(alist[i])
    #         if len(head) == n:
    #             ans.append(head[:])
    #             head.pop()
    #             return
    #         else:
    #             ss = s.copy()
    #             ss.remove(i)
    #             dfs(alist, head, ss)
    #             head.pop()
    # dfs(nums, [], seq)
    #
    # return ans

    # 法2：-
    # res = []
    # def backtrack(nums, tmp):
    #     if not nums:
    #         res.append(tmp)
    #         return
    #     for i in range(len(nums)):
    #         backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
    # backtrack(nums, [])
    # return res

    # 法 3：
    return list(permutations(nums))





if __name__ == '__main__':
    print(permute([1,2,3]))
