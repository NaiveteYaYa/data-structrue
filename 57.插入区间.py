# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 14:03
# @Author  : WuxieYaYa

"""
给出一个无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠
（如果有必要的话，可以合并区间）。

示例 1：

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

注意：输入类型已在 2019 年 4 月 15 日更改。请重置为默认代码定义以获取新的方法签名。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-interval
"""
from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    TODO: 重做
    :param intervals:
    :param newInterval:
    :return:
    """
    left, right = newInterval
    placed = False
    ans = []
    for li, ri in intervals:
        if li > right:
            if not placed:
                ans.append([left, right])
                placed = True
            ans.append([li, ri])
        elif ri < left:
            ans.append([li, ri])
        else:
            left = min(left, li)
            right = max(right, ri)

    if not placed:
        ans.append([left, right])

    return ans



if __name__ == '__main__':
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [14, 18]
    print(insert(intervals, newInterval))

