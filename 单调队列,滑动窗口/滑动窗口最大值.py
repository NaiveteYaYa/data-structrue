# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 18:53
# @Author  : WuxieYaYa


"""
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。
 
示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：
你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

 
进阶：
你能在线性时间复杂度内解决此题吗？

链接：https://leetcode-cn.com/problems/sliding-window-maximum
"""

def maxSlidingWindow(nums, k):
    """
    双向队列：单调队列,滑动窗口
    执行用时 :60 ms, 在所有 Python3 提交中击败了99.23%的用户
    内存消耗 :17.1 MB, 在所有 Python3 提交中击败了100.00%的用户
    """

    from collections import deque
    n = len(nums)

    if n*k==0:
        return []

    if k == 1:
        return nums

    slid = deque()
    maxid = 0

    for j in range(k):
        while slid and nums[j] > nums[slid[-1]]:
            slid.pop()
        slid.append(j)
        if slid and nums[j] > nums[maxid]:
            maxid = j

    ans = [nums[maxid]]

    for i in range(k, n):
        if slid and slid[0] == i - k:
            slid.popleft()
        while slid and nums[i] > nums[slid[-1]]:
            slid.pop()
        slid.append(i)
        ans.append(nums[slid[0]])

    return ans


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    result = maxSlidingWindow(nums, 3)
    print(result)









