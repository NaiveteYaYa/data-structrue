# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 22:06
# @Author  : WuxieYaYa

"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

链接：https://leetcode-cn.com/problems/trapping-rain-water
"""
def trap(height):
    # 单调栈
    n = len(height)
    if n <=2 :
        return 0
    res, idx = 0, 0
    stack = []
    while idx < n:
        while len(stack) > 0 and height[idx] > height[stack[-1]]:
            top = stack.pop()  # index of the last element in the stack
            if len(stack) == 0:
                break
            h = min(height[stack[-1]], height[idx]) - height[top]
            dist = idx - stack[-1] - 1
            res += (dist * h)
        stack.append(idx)
        idx += 1
    return res



if __name__ == '__main__':
    a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap(a))
