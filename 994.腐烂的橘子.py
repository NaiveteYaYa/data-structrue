# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 22:03
# @Author  : WuxieYaYa

"""
在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
 
示例 1：

输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：

输入：[[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
示例 3：

输入：[[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
 
提示：
1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] 仅为 0、1 或 2

链接：https://leetcode-cn.com/problems/rotting-oranges
"""


def orangesRotting(grid):
    """
    执行用时 :56 ms, 在所有 Python3 提交中击败了90.58%的用户
    内存消耗 :13.6 MB, 在所有 Python3 提交中击败了9.30%的用户
    :param grid:
    :return:
    """
    # global temp
    # direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # rot_queue = []
    # n = 0
    # r = len(grid)
    # c = len(grid[0])
    # for i in range(r):
    #     for j in range(c):
    #         if grid[i][j]:
    #             n += 1
    #         if grid[i][j] == 2:
    #             rot_queue.append((i, j))
    #
    # if n == len(rot_queue):
    #     return 0
    # T = 0
    # rot = len(rot_queue)
    # while rot_queue:
    #     flag = 0    # 判定循环是否有效
    #     temp = []   # 后添加的需要添加在临时队列中，这次循环完成后添加到rot队列中
    #     for _ in range(len(rot_queue)):
    #         rot_r, rot_c = rot_queue.pop()
    #
    #         for i, j in direction:
    #             if r > rot_r + i > -1 and c > rot_c + j > -1 and grid[rot_r + i][rot_c + j] == 1:
    #                 grid[rot_r + i][rot_c + j] = 2
    #                 temp.append((rot_r + i, rot_c + j))
    #                 flag = 1
    #                 rot += 1
    #                 if rot == n:
    #                     return T + 1
    #     rot_queue += temp  # 循环完毕，添加
    #     if flag:  # 循环有效，说明有新新鲜的被腐败。时间+1
    #         T += 1
    #
    # return T if n == rot else -1

    """
        作者：z1m
        链接：https://leetcode-cn.com/problems/rotting-oranges/solution/yan-du-you-xian-sou-suo-python3-c-by-z1m/
    """
    row = len(grid)
    col = len(grid[0])
    rotten = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}  # 腐烂集合
    fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}  # 新鲜集合
    time = 0
    while fresh:
        if not rotten: return -1
        rotten = {(i + di, j + dj) for i, j in rotten for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)] if
                  (i + di, j + dj) in fresh}  # 即将腐烂的如果在新鲜的集合中，就将它腐烂
        fresh -= rotten  # 剔除腐烂的
        time += 1
    return time



if __name__ == '__main__':
    a = [[2, 1, 1],
         [0, 1, 1],
         [1, 0, 1]]

    # a = [[2, 1, 1],
    #      [1, 1, 0],
    #      [0, 1, 1]]
    # a = [[1], [2], [1], [2]]
    result = orangesRotting(a)
    print(result)
