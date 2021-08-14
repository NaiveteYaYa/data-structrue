# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 18:22
# @Author  : WuxieYaYa

"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]

链接：https://leetcode-cn.com/problems/3sum
"""


def threeSum(nums):
    """
    排序 + 双指针
    本题的难点在于如何去除重复解。

    算法流程：
        1.特判，对于数组长度 n，如果数组为 null 或者数组长度小于 3，返回 []。
        2.对数组进行排序。
        3.遍历排序后数组：
            若 nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 00，直接返回结果。
            对于重复元素：跳过，避免出现重复解
            令左指针 L=i+1，右指针 R=n−1，当 L<R, L<R 时，执行循环：
            当 nums[i]+nums[L]+nums[R]==0    nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。
            并同时将 L,RL,R 移到下一位置，寻找新的解
            若和大于 00，说明 nums[R]nums[R] 太大，RR 左移
            若和小于 00，说明 nums[L]nums[L] 太小，LL 右移

    链接：https://leetcode-cn.com/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
    """
    n = len(nums)
    if n < 3 or not nums:
        return []

    nums.sort()
    ans = []

    for i in range(n):
        l = i + 1
        r = n - 1
        while l < r:
            if sum([nums[i], nums[l], nums[r]]) == 0:
                ans.append([nums[i], nums[l], nums[r]])
                while nums[r] == nums[n - 1]:
                    r -= 1
                while nums[l] == nums[l + 1]:
                    l += 1
                r -= 1
                l += 1
            elif sum([nums[i], nums[l], nums[r]]) < 0:
                l += 1
            else:
                r -= 1

    return ans

    """
    此法有缺陷，会漏掉部分答案。
        半固定两端，然后遍历两端内的元素，根据和的大小移动两端
    nums.sort()
    began = 0
    end = len(nums) - 1
    ans = []

    while began < end:
        flag = 1
        for num in nums[began + 1:end]:
            if nums[began] + nums[end] + num < 0:
                continue
            if nums[began] + nums[end] + num > 0:
                end -= 1
                break
            else:
                tem = [nums[began], nums[end], num]
                if tem not in ans:
                    ans.append([nums[began], nums[end], num])
                end -= 1
                flag = 0
                break
        if flag:
            began += 1
    return ans
    """


if __name__ == '__main__':
    nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    result = threeSum(nums)
    print(result)
