# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 8:19
# @Author  : WuxieYaYa
"""
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:

输入: "abab"

输出: True

解释: 可由子字符串 "ab" 重复两次构成。
示例 2:

输入: "aba"

输出: False
示例 3:

输入: "abcabcabcabc"

输出: True

解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)

链接：https://leetcode-cn.com/problems/repeated-substring-pattern
"""


def repeatedSubstringPattern(s: str) -> bool:
    n = len(s)

    # 第一层循环：初步筛选，并确定字符串区间
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            count = n // i

            # 第二层循环， 在确定字符串区间下，重复了多少次。
            ans = 1
            for j in range(1, count):
                if s[:i] == s[i *j: i*(j+1)]:
                    pass


if __name__ == '__main__':
    Str_ = 'abab'
    print(repeatedSubstringPattern(Str_))
