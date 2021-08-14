# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 9:38
# @Author  : WuxieYaYa

"""
你被给定一个 m × n 的二维网格，网格中有以下三种可能的初始化值：

-1 表示墙或是障碍物
0 表示一扇门

INF 无限表示一个空的房间。然后，我们用 231 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 的。
你要给每个空房间位上填上该房间到 最近 门的距离，如果无法到达门，则填 INF 即可。

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

   3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""

def wallsAndGates(rooms) -> None:
    if not rooms or len(rooms) == 0:
        return
    row = len(rooms)
    col = len(rooms[0])

    def bfs(i,j,val):
        if i<0 or i >= row or j < 0 or j >= col:
            return
        if rooms[i][j] < val:
            return
        rooms[i][j] = val

        bfs(i+1, j, val+1)
        bfs(i-1, j, val+1)
        bfs(i, j+1, val+1)
        bfs(i, j-1, val+1)

    for i in range(row):
        for j in range(col):
            if rooms[i][j] == 0:
                bfs(i,j,0)


if __name__ == '__main__':
    INF = float('inf')
    rooms = [[INF, -1, 0, INF],
             [INF, INF, INF, -1],
             [INF, -1, INF, -1],
             [0, -1, INF, INF]]
    wallsAndGates(rooms)
    print(rooms)