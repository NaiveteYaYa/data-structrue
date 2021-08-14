# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 12:58
# @Author  : WuxieYaYa

"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。

示例 1:

输入: [7,5,6,4]
输出: 5
 

限制：

0 <= 数组长度 <= 50000

链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
"""


def reversePairs(nums):
    """
    1.利用分治思想，归并算法
    :param nums:
    :return:
    """

    n = 0

    def mergesort(L):
        # 超时：为毛归并也超时？
        nonlocal n
        length = len(L)
        if length <= 1:
            return L
        left = mergesort(L[:length // 2])
        right = mergesort(L[length // 2:])
        l = 0
        r = 0
        res = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
                n += len(left[l:])
        res += left[l:]

        res += right[r:]

        return res

    mergesort(nums)

    return n


from bisect import bisect_right

## 二分查找
class Solution:
    def reversePairs(self, nums):
        ans = 0
        _sorted_ = list()
        for i, j in enumerate(nums):
            idx = bisect_right(_sorted_, j)
            _sorted_[idx:idx] = [j]
            ans += i - idx
        return ans


if __name__ == '__main__':
    ll = [1, 2, 3, 4, 5]
    print(reversePairs(ll))
