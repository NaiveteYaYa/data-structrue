# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 23:19
# @Author  : WuxieYaYa

"""求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45

链接：https://leetcode-cn.com/problems/qiu-12n-lcof
"""

class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(n):
        return n and Solution.sumNums(n-1) + n


if __name__ == '__main__':
    print(Solution.sumNums(9))