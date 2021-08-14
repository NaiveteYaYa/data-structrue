# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 10:46
# @Author  : WuxieYaYa

"""
给出一个区间的集合，请合并所有重叠的区间。
示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

链接：https://leetcode-cn.com/problems/merge-intervals
"""


def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    r, l = 0, 1
    while l < len(intervals):
        if intervals[r][1] >= intervals[l][0]:
            if intervals[r][1] < intervals[l][1]:
                intervals[r][1] = intervals[l][1]
            intervals[l:l + 1] = []

        else:
            r += 1
            l += 1

    return intervals


def merge_2(intervals):
    i = 0
    while i < len(intervals) - 1:
        while i < len(intervals)-1 and intervals[i][1] >= intervals[i + 1][0]:
            intervals[i] = [min(intervals[i][0], intervals[i + 1][0]), max(intervals[i][1], intervals[i + 1][1])]
            del intervals[i + 1]
        i += 1

    return intervals


if __name__ == '__main__':
    l = [[1, 4], [0, 2], [3, 5]]
    # l = [[1,3],[2,6],[8,10],[15,18]]
    # print(merge(l))
    print(merge_2(l))
