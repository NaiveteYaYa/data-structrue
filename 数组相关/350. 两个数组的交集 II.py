# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 18:54
# @Author  : WuxieYaYa

"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
 

说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
"""


def intersect(nums1, nums2):
    """
    法1： 利用排序
    :param nums1:
    :param nums2:
    :return:
    """
    # nums1.sort()
    # nums2.sort()
    # n1 = len(nums1)
    # n2 = len(nums2)
    # if n1==0 or n2 == 0:
    #     return []
    # res = []
    # r, l = 0, 0
    # while r < n1 and l < n2 :
    #     if nums1[r] == nums2[l]:
    #         res.append(nums1[r])
    #         r += 1
    #         l += 1
    #     elif nums1[r] < nums2[l]:
    #         r += 1
    #     else:
    #         l += 1
    # return res


    """
    法2 ： 利用hash
    """
    from collections import Counter
    n1 = len(nums1)
    n2 = len(nums2)
    if n2 > n1:
        return intersect(nums2, nums1)

    m = Counter(nums1)
    res = list()
    for num in nums2:
        if m[num] > 0:
            res.append(num)
            m[num] -= 1

    return res


if __name__ == '__main__':
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(intersect(nums1, nums2))
