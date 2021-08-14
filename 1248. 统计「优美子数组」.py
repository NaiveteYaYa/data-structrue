# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 17:10
# @Author  : WuxieYaYa

"""
给你一个整数数组 nums 和一个整数 k。
如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
请返回这个数组中「优美子数组」的数目。

示例 1：

输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
示例 2：

输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
示例 3：

输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16

链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays
"""


def numberOfSubarrays(nums, k):
    #利用双指针
    length = len(nums)
    pos = []
    width = []
    count = 1
    for i, num in enumerate(nums):
        if num % 2 == 1:
            pos.append(i)
            width.append(count)
            count = 1
        else:
            count += 1
    width.append(count)

    if len(pos) < k:
        return 0

    c = 0
    for i in range(len(pos)-k+1):
        m = width[i]
        n = width[i+k]
        c += m*n

    return c



if __name__ == '__main__':
    nums = [1, 1, 2, 1, 1]
    k = 3
    nums =[2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
    k = 2
    print(numberOfSubarrays(nums, k))
    a = list()

