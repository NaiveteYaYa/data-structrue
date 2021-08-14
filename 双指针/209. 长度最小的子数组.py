# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 20:56
# @Author  : WuxieYaYa

"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，
并返回其长度。如果不存在符合条件的连续子数组，返回 0。
示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
"""


def minSubArrayLen(s, nums):
    """双指针：TODO：review"""
    start = 0   # 起始位置
    ans = len(nums)
    sum_ = 0
    for i in range(len(nums)):
        sum_ += nums[i]     # 加上新元素
        while (sum_ >= s):      # 不断删除起始位置来确定最短子序列。
            ans = min(ans, i-start+1)
            sum_ -= nums[start]   # 试探去除起始元素的和
            start += 1             # 起始位置右移一位

    return ans if sum(nums) >=s else 0


if __name__ == '__main__':
    s = 4
    nums = [1,1]
    print(minSubArrayLen(s,nums))