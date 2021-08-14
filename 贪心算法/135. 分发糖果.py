# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 14:00
# @Author  : WuxieYaYa

"""
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

示例 1:

输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
示例 2:

输入: [1,2,2]
输出: 4
解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。

链接：https://leetcode-cn.com/problems/candy
"""


def candy(ratings):
    n = len(ratings)
    ans = [1] * n
    if n > 2:
        for i in range(1, n - 1):#【1,2,3,4】
            l = i - 1
            r = i + 1
            if ratings[l] < ratings[i]:
                ans[i] = max(ans[l] + 1,ans[i])
            if ratings[n - i - 1] > ratings[n - l - 1]:
                ans[n - i - 1] = max(ans[n - l - 1] + 1, ans[n-i-1])
    if n >= 2:
        if ratings[0] > ratings[1]:
            ans[0] = ans[1] + 1
        if ratings[-1] > ratings[-2]:
            ans[-1] = ans[-2] + 1

    return sum(ans), ans


if __name__ == '__main__':
    ratings =[0,1,2,5,3,2,7]
    print(candy(ratings))
