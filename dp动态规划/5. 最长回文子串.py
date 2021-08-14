# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 15:28
# @Author  : WuxieYaYa

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import typing
from typing import List, Any, Union


def longestPalindrome(s: str):
    """
    todo：
    dp 解法
    """
    n = len(s)
    dp = [False * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][j] = 1





if __name__ == '__main__':
    a = 'b'
    print(longestPalindrome(a))
