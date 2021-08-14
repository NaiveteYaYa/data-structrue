# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 9:32
# @Author  : WuxieYaYa

"""
在未排序的数组中找到第 k 个最大的元素。请注意，
你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
"""
from typing import List
import random


def findKthLargest(nums:List, k):
    """
    法1：借助 partition 操作定位到最终排定以后索引为 len - k 的那个元素（特别注意：随机化切分元素）
    """
    size = len(nums)
    target = size - k

    def _partition(nums, left, right):
        random_index = random.randint(left,right)
        nums[random_index], nums[left] = nums[left], nums[random_index]

        pivot = nums[left]
        j = left
        for i in range(left+1, right+1):
            if nums[i] < pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[left], nums[j] = nums[j], nums[left]
        return j


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(findKthLargest(nums, k))
