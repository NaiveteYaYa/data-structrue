# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 18:25
# @Author  : WuxieYaYa

"""
在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
请你返回最终形体的表面积。

示例 1：

输入：[[2]]
输出：10
示例 2：

输入：[[1,2],
      [3,4]]
输出：34
示例 3：

输入：[[1,0],
      [0,2]]
输出：16
示例 4：

输入：[[1,1,1],
      [1,0,1],
      [1,1,1]]
输出：32
示例 5：

输入：[[2,2,2],
      [2,1,2],
      [2,2,2]]
输出：46
 

提示：
1 <= N <= 50
0 <= grid[i][j] <= 50

链接：https://leetcode-cn.com/problems/surface-area-of-3d-shapes
"""

from typing import List


def surfaceArea(grid: List[List[int]]):
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    r, c = len(grid), len(grid[0])
    N = 0
    for i in grid:
        for j in i:
            N += j * 6

    for i in range(r):
        for j in range(c):
            if grid[i][j] > 0:
                N -= 2*(grid[i][j]-1)
            for h, v in direction:
                h, v = i+h, v+j
                if -1< h < r and -1< v < c and grid[h][v] > 0:
                    min1 = min(grid[h][v], grid[i][j])
                    N -= min1
    return N


if __name__ == '__main__':
    a = [[2, 2, 2],
         [2, 1, 2],
         [2, 2, 2]]
    print(surfaceArea(a))

