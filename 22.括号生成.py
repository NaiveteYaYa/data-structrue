# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 18:06
# @Author  : WuxieYaYa


"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

链接：https://leetcode-cn.com/problems/generate-parentheses
"""


def generateParenthesis(n):
    ans = []

    def dfs(i=1, temp='(', j=0):
        if i == j == n:
            ans.append(temp)
            return
        elif i == n:
            while j<n:
                temp += ")"
                j += 1
            ans.append(temp)

        if i < n:
            dfs(i=i+1, temp=temp+"(", j=j)
        if j < i:
            dfs(i, temp=temp+")", j=j + 1)

    dfs()
    return ans

if __name__ == '__main__':
    res = generateParenthesis(3)
    """
    (()())"""
    print(res)
