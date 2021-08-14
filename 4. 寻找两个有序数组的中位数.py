# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 20:18
# @Author  : WuxieYaYa

"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
"""


def findMedianSortedArrays(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    mid = (m + n) // 2 + 1
    flag = (m + n) % 2
    combin = []
    i, j = -1, -1

    if nums1:
        i = nums1.pop()
    if nums2:
        j = nums2.pop()
    while 1:

        while i > j and len(combin) < mid:
            combin.append(i)
            if nums1:
                i = nums1.pop()
            else:
                break

        while i < j and len(combin) < mid:
            combin.append(j)
            if nums2:
                j = nums2.pop()
            else:
                j = -1
                break
        if len(combin) == mid:
            break

        while i == j:
            if len(combin) < mid - 1:
                combin += [i] * 2
            else:
                combin.append(i)

            if len(combin) == mid:
                break

            if nums1:
                i = nums1.pop()
            if nums2:
                j = nums2.pop()

        if len(combin) == mid:
            break

    if flag:
        return combin[-1]

    else:
        return (combin[-1] + combin[-2]) / 2


if __name__ == '__main__':
    nums1 = []
    nums2 = [3]
    print(findMedianSortedArrays(nums1, nums2))
