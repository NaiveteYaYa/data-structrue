# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 16:18
# @Author  : WuxieYaYa

"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

链接：https://leetcode-cn.com/problems/jump-game
"""
from collections import deque
def canJump(nums):
    """
    、法 1：
    虽然进行优化（将前向遍历改为后项遍历才得以通过） 但接近超时： 时间：5%

    """
    # n = len(nums)
    # if n == 1:
    #     return True
    # stack = deque([0])
    # while stack:
    #     cur = stack.popleft()
    #     for i in range(nums[cur]+1,1, -1):
    #         if cur+i not in stack:
    #             if cur+i == n - 1:
    #                 return True
    #             stack.append(cur+i)
    #         else:
    #             break
    # return False

    """
    法2 ： 通过贪心算法：
    """
    n = len(nums)
    right_most = 0
    for i in range(n):
        if i <= right_most:
            right_most = max(right_most, i+nums[i])
            if right_most >= n-1:
                return True

    return False




if __name__ == '__main__':
    print(canJump([1,2]))