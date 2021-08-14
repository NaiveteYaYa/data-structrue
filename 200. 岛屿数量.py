# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 15:56
# @Author  : WuxieYaYa

"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1:

输入:
11110
11010
11000
00000
输出: 1
示例 2:

输入:
11000
11000
00100
00011
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

链接：https://leetcode-cn.com/problems/number-of-islands
"""

from collections import deque

def numIslands(grid):
    # 此解罗里吧嗦
    # directions = [(0, 1), (1, 0), (-1, 0), (-0, -1)]
    #
    # r = len(grid)
    # if r == 0:
    #     return 0
    # c = len(grid[0])
    # if c == 0:
    #     return 0
    #
    # stack = deque([])
    # n = 0
    # for i in range(r):
    #     for j in range(c):
    #         if grid[i][j] == "1":
    #             if (i, j) not in stack:
    #                 n += 1
    #                 stack.append((i, j))
    #             while stack:
    #                 p = stack.popleft()
    #                 grid[p[0]][p[1]] = 0
    #                 for direction in directions:
    #                     h, v = p[0] + direction[0], p[1] + direction[1]
    #                     if 0 <= h < r and 0 <= v < c:
    #                         if grid[h][v] == "1" and (h,v) not in stack:
    #                             stack.append((h, v))
    #
    # return n

    """BFS"""
    if not grid or len(grid) == 0:
        return 0
    row = len(grid)
    col = len(grid[0])
    count = 0

    def bfs(i, j):
        if i < 0 or j < 0 or i >= row or j >= col:
            return True
        elif grid[i][j] == '0':
            return True
        else:
            grid[i][j] = '0'
            return bfs(i - 1, j) and bfs(i, j - 1) and bfs(i + 1, j) and bfs(i, j + 1)

    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1' and bfs(i, j):
                count += 1

    return count

if __name__ == '__main__':
    g = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    # g = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    # g = [["1","1","1"],["0","1","0"],["1","1","1"]]
    print(numIslands(g))
