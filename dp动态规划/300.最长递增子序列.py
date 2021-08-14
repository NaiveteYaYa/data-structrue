# -*- coding: utf-8 -*-
# @Time    : 2021/4/23 18:41
# @Author  : WuxieYaYa

"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

 
示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1
 
提示：

1 <= nums.length <= 2500
-104 <= nums[i] <= 104

链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
"""

"""
总结：
    归根结底，利用DP算法的思想，不断的增加序列的长度（从1 -- N），每次增长实现当前最优。
"""


def lengthOfLIS(nums):
    dp = [1 for _ in range(len(nums))]
    # dp = [0] + dp
    ans = 1
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j] and dp[i] < (dp[j] + 1):
                dp[i] = dp[j] + 1
                if dp[i] > ans:
                    ans = dp[i]
    return ans

def lol(nums):
    dp = [1 for _ in range(len(nums))]

    ans = 1

    for i in range(1, len(nums)):
        temp_max = 1
        for j in range(i):




if __name__ == "__main__":
    nums = [0, 1, 0, 3, 2, 3]
    print(lengthOfLIS(nums))
