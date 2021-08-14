# -*- coding: utf-8 -*-
# @Time    : 2020/6/14 11:16
# @Author  : WuxieYaYa

"""
给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，使得将数组中所有大于 value 的值变成 value 后，
数组的和最接近  target （最接近表示两者之差的绝对值最小）。

如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。

请注意，答案不一定是 arr 中的数字。

示例 1：

输入：arr = [4,9,3], target = 10
输出：3
解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。
示例 2：

输入：arr = [2,3,5], target = 10
输出：5
示例 3：

输入：arr = [60864,25176,27249,21296,20204], target = 56803
输出：11361
 
提示：

1 <= arr.length <= 10^4
1 <= arr[i], target <= 10^5

链接：https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target
"""
import bisect

def findBestValue(arr, target):
    arr.sort()
    n = len(arr)
    # 判断数组前后两边界
    average = round(target / n)
    if average <= arr[0]:
        return average


    # 判定数组内
    prefix = [0]  # 前缀和
    for i in range(n):
        prefix.append(prefix[-1] + arr[i])

    if prefix[-1] <= target:
        return arr[-1]

    for i in range(0, n):   # [1,2,3,4,5]
        sum_ = prefix[i] + (n - i) * arr[i]
        if sum_ > target:
            pre_average = round((target - prefix[i]) / (n-i))
            # now_average = round((target - prefix[i+1]) / (n - i - 1))
            return pre_average if abs(pre_average*(n-i) + prefix[i] - target) < abs(sum_ - target) else arr[i]



if __name__ == '__main__':
    aa = [1,2,23,24,34,36]
    aa = [1547,83230,57084,93444,70879]
    target = 71237
    # target = 110
    print(findBestValue(aa, target))
