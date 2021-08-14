# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 0:56
# @Author  : WuxieYaYa

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

链接：https://leetcode-cn.com/problems/maximum-subarray
"""
from collections import deque


def maxSubArray(nums):
    # TODO:review
    """

        size = len(nums)
        if size == 0:
            return 0
        # 起名叫 pre 表示的意思是“上一个状态”的值
        pre = nums[0]
        res = pre
        for i in range(1, size):
            pre = max(nums[i], pre + nums[i])
            res = max(res, pre)  # 更新全局最大值
        return res

    链接：https://leetcode-cn.com/problems/maximum-subarray/solution/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-java-dai/
    """
    size = len(nums)
    min_val = 0
    max_val = -float('inf')
    prefix_sum = [0]
    for i in nums:
        prefix_sum.append(prefix_sum[-1] + i)

    for i in range(size):
        max_val = max(prefix_sum[i + 1] - min_val, max_val)
        min_val = min(min_val, prefix_sum[i])

    return max_val


if __name__ == '__main__':
    s = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(s))
