# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 15:49
# @Author  : WuxieYaYa


"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

链接：https://leetcode-cn.com/problems/3sum-closest
"""


def threeSum(nums, target):
    diff = 1e9
    ans = []
    nums.sort()

    for i in range(len(nums) - 2):
        r = len(nums) -1
        l = i + 1
        while l < r:
            s = target - nums[i] - nums[l] - nums[r]
            temp = abs(s)
            if temp < diff:
                ans = [nums[i], nums[l], nums[r]]
                diff = temp
            if s > 0:
                l += 1
            elif s < 0:
                r -= 1
            else:
                return [nums[i], nums[l], nums[r]]

    return ans


if __name__ == '__main__':
    a = [-1, 2, 1, -4]
    result = threeSum(a, target=1)
    print(result)
