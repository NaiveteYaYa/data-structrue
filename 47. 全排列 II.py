# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 21:25
# @Author  : WuxieYaYa


"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

链接：https://leetcode-cn.com/problems/permutations-ii
"""


def permuteUnique(nums):
    # TODO：
    nums.sort()
    ans = [[]]
    def dfs(nums, counter, k, res=[]): # k从第几个元素开始， counter：计数(计子集的长度）
        if counter == 0:
            ans.append(res.copy())

        for i in range(1, len(nums)+1):
            dfs(nums, counter=i, k=)

        pass

    for i in range(len(nums)):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        num_s = nums[i:]
        dfs(nums=num_s, i)


if __name__ == '__main__':
    print(permuteUnique([1,1,2]))
    float()