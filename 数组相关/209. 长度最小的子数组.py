# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 23:25
# @Author  : WuxieYaYa

"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，
并返回其长度。如果不存在符合条件的连续子数组，返回 0。

示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的连续子数组。
 

进阶：

如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
"""

def minSubArrayLen(s, nums):
    if nums == []:
        return 0
    prefix = [0]
    for i in range(len(nums)):
        prefix.append(prefix[-1] + nums[i])

    ans = len(nums) + 1

    l, r = 0, 1
    while r <= len(nums):
        sum_ = prefix[r] - prefix[l]
        if sum_ < s:
            r += 1
        if sum_ >= s:
            if r - l < ans:
                ans = r - l
            l += 1

    return ans if ans < len(nums) else 0

if __name__ == '__main__':
    s = 7
    nums = []
    print(minSubArrayLen(s, nums))

