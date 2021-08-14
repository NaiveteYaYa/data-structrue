# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 22:22
# @Author  : WuxieYaYa

"""
给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

示例 1: 

输入: [5,7]
输出: 4
示例 2:

输入: [0,1]
输出: 0

链接：https://leetcode-cn.com/problems/bitwise-and-of-numbers-range

解题思路：
    1. 相邻两数的二进制最后一位不同，所以相邻两数的
        所以相邻两数的二进制最后一位，按位与必然是0

    2. 因此由端点两数不断向右移动，直到数字相等为止，即得到公共前缀。
            （因为只要断点两数不同，则它们之间至少包含相邻的两数）

    3. 通过将公共前缀向左移动，将零添加到公共前缀的右边以获得最终结果。
"""


def rangeBitwiseAnd(m: int, n: int) -> int:
    # 移动位数
    shift = 0
    while m < n:
        shift += 1
        m >>= 1
        n >>= 1

    return m << shift


if __name__ == '__main__':
    print(rangeBitwiseAnd(3, 9999))
