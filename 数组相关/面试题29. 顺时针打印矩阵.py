# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 18:41
# @Author  : WuxieYaYa

"""输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
"""
from itertools import cycle
from collections import deque

def spiralOrder(matrix):
    "法1：逐层剥离"
    # if not matrix or not matrix[0]:
    #     return []
    # matrix = deque([deque(i) for i in matrix])
    # ans = []
    # suqence = cycle(['left', 'down', 'right', 'up'])
    # m = len(matrix)
    # for i in suqence:
    #     if matrix:
    #         if i == 'left':  # 从左向右
    #             temp = matrix.popleft()
    #             ans.extend(temp)
    #             m -= 1
    #         if i == 'down' and matrix[0]:  # 从上到下
    #             for i in range(m):
    #                 ans.append(matrix[i].pop())
    #
    #         if i == 'right':  # 从右向左
    #             temp = matrix.pop()
    #             while temp:
    #                 ans.append(temp.pop())
    #             m -= 1
    #         if i == 'up' and matrix[0]:  # 从下至上
    #             m = len(matrix)
    #             for i in range(m - 1, -1, -1): # 注意
    #                 ans.append(matrix[i].popleft())
    #     else:
    #         break
    # return ans

    """
    法2：按圈层获取
    
    
    """
    if not matrix or not matrix[0]:
        return []
    m = len(matrix)
    n = len(matrix[0])
    layer_num = (min(m, n)+ 1)>>1
    ans = []
    for lay in range(layer_num):
        for i in range(lay, n - lay):  # 从左到右
            ans.append(matrix[lay][i])

        for i in range(lay+1, m - lay): # 从上到下 TODO: 最后的判断？
            ans. append(matrix[i][n-lay-1])

        for i in range(n - lay - 2, lay-1, -1):
            ans.append(matrix[m - lay -1][i])

        for i in range(m - lay - 2, lay, -1):
            ans.append(matrix[i][lay])

    return ans


if __name__ == '__main__':
    matrix = [[7],[9],[6]]
    print(spiralOrder(matrix))

