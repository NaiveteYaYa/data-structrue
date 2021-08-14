# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 11:18
# @Author  : WuxieYaYa

"""
给定两条线段（表示为起点start = {X1, Y1}和终点end = {X2, Y2}），如果它们有交点，请计算其交点，没有交点则返回空值。
要求浮点型误差不超过10^-6。若有多个交点（线段重叠）则返回 X 值最小的点，X 坐标相同则返回 Y 值最小的点。

示例 1：

输入：
line1 = {0, 0}, {1, 0}
line2 = {1, 1}, {0, -1}
输出： {0.5, 0}
示例 2：

输入：
line1 = {0, 0}, {3, 3}
line2 = {1, 1}, {2, 2}
输出： {1, 1}
示例 3：

输入：
line1 = {0, 0}, {1, 1}
line2 = {1, 0}, {2, 1}
输出： {}，两条线段没有交点
 
提示：
坐标绝对值不会超过 2^7
输入的坐标均是有效的二维坐标

链接：https://leetcode-cn.com/problems/intersection-lcci
"""


def intersection(start1, end1, start2, end2):
    """
    法1：执行用时 :40 ms, 在所有 Python3 提交中击败了53.45%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了100.00%的用户

    解题思路
        主要是区分4种情况：

            两条都是垂线，即与y轴平行
            直线1是垂线，直线2不是
            直线2是垂线，直线1不是
            两条都不是垂线
            斜率相同，且截距相同并有交点
            斜率不同，先算出交点，再看交点是否均在两条线段之间

        作者：luanz
        链接：https://leetcode-cn.com/problems/intersection-lcci/solution/pythonzhe-ti-tai-ma-fan-liao-bian-liao-40fen-zhong/
    """
    x1, y1 = start1
    x2, y2 = end1
    x3, y3 = start2
    x4, y4 = end2

    k1 = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else None
    b1 = y1 - k1 * x1 if k1 is not None else None
    k2 = (y4 - y3) / (x4 - x3) if x4 - x3 else None
    b2 = y3 - k2 * x3 if k2 is not None else None

    if k1 is None and k2 is None:
        if x1 == x3 and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            return [x1, sorted([y1, y2, y3, y4])[1]]

    elif k1 is None:
        y = k2 * x1 + b2
        if min(x3, x4) <= x1 <= max(x3, x4):
            return [x1, y]

    elif k2 is None:
        y = k1 * x3 + b1
        if min(x1, x2) <= x1 <= max(x1, x2):
            return [x3, y]

    else:
        if k1 == k2:
            if b1 == b2:
                return [sorted([x1, x2, x3, x4])[1], sorted([y1, y2, y3, y4])[1]]

        else:
            x = (b2 - b1) / (k1 - k2)
            y = k1 * x + b1
            if min(x1, x2) <= x <= max(x2, x1) and min(x3, x4) <= x <= max(x3, x4):
                return [x, y]

    return []


if __name__ == '__main__':
    line1 = {0, 0}, {3, 3}
    line2 = {1, 1}, {2, 2}
    intersection(line1, line2)
