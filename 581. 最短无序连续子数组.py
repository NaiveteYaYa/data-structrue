# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 9:54
# @Author  : WuxieYaYa

"""
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
"""


def findUnsortedSubarray(nums):
    """
    法1：
    时间复杂度：nlogn
    空间复杂度：O(n)
    时间和空间都完败。
    :param nums:
    :return:
    """
    # sorted_nums = sorted(nums)
    #
    # start = 0
    # for i in range(len(nums)):
    #     if nums[i] != sorted_nums[i]:
    #         start = i-1
    #         break
    # end = 0
    # for j in range(len(nums)-1, -1, -1):
    #     if nums[j] != sorted_nums[j]:
    #         end = j
    #         break
    # return end - start


    # 改进：一次遍历
    # start = 100000
    # end = 0
    # for i in range(len(nums)):
    #     if sorted_nums[i] != nums[i]:
    #         start = min(start, i)
    #         end = max(end, i)
    # return end - start + 1 if (end - start + 1>0) else 0


    # 在优化代码量
    # diff = [i for i, (a, b) in enumerate(zip(nums, sorted(nums))) if a != b]
    #     # return len(diff) and max(diff) - min(diff) + 1

    """
    方法 5：不使用额外空间
    算法
    
    这个算法背后的思想是无序子数组中最小元素的正确位置可以决定左边界，最大元素的正确位置可以决定右边界。
    因此，首先我们需要找到原数组在哪个位置开始不是升序的。我们从头开始遍历数组，一旦遇到降序的元素，我们记录最小元素为 min。
    类似的，我们逆序扫描数组 nums，当数组出现升序的时候，我们记录最大元素为 max。
    然后，我们再次遍历 nums 数组并通过与其他元素进行比较，来找到 min 和 max 在原数组中的正确位置。
    我们只需要从头开始找到第一个大于 min 的元素，从尾开始找到第一个小于 max 的元素，它们之间就是最短无序子数组。
    
    链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/zui-duan-wu-xu-lian-xu-zi-shu-zu-by-leetcode/
    
    TODO:细品
    """
    n=len(nums)
    max_num=nums[0]
    right=0
    for i in range(n):
        if(nums[i]>=max_num):
            max_num=nums[i]
        else:
            right=i
    left=n
    min_num=nums[-1]
    for i in range(n-1,-1,-1):
        if(nums[i]<=min_num):
            min_num=nums[i]
        else:
            left=i
    return right-left+1 if(right-left+1 >0) else 0



if __name__ == '__main__':
    a = [2, 6, 6, 4, 8, 10, 9, 15]
    # a = [1,2,3,4]
    # a = [2, 1]
    print(findUnsortedSubarray(a))


