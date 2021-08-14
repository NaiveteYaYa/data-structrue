# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 13:43
# @Author  : WuxieYaYa


"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
 
图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49

链接：https://leetcode-cn.com/problems/container-with-most-water
"""

def maxArea(height):
    """
    明显不能用暴力法
    :param height:
    :return:
    """
    n = len(height)
    Area = 0
    l, r = 0, n-1
    while l != r:
        temp = abs((r-l)*min(height[l], height[r]))
        if temp > Area:
            Area = temp
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return Area


if __name__ == '__main__':
    nums = [2,3,4,5,18,17,6]
    print(maxArea(nums))
