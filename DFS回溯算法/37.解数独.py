# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 21:23
# @Author  : WuxieYaYa

"""
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

链接：https://leetcode-cn.com/problems/sudoku-solver

-算法

    现在准备好写回溯函数了
    backtrack(row = 0, col = 0)。

    从最左上角的方格开始 row = 0, col = 0。直到到达一个空方格。

    从1 到 9 迭代循环数组，尝试放置数字 d 进入 (row, col) 的格子。

        如果数字 d 还没有出现在当前行，列和子方块中：

            将 d 放入 (row, col) 格子中。
            记录下 d 已经出现在当前行，列和子方块中。
            如果这是最后一个格子row == 8, col == 8 ：
            意味着已经找出了数独的解。
            否则
            放置接下来的数字。
            如果数独的解还没找到：
            将最后的数从 (row, col) 移除。

链接：https://leetcode-cn.com/problems/sudoku-solver/solution/jie-shu-du-by-leetcode/
"""


def solveSudoku_1(board):
    """
            Do not return anything, modify board in-place instead.
            todo:第一种解法没有完全理顺，代码有误。
    """

    board_1 = []
    board_cube = [[], [], [], [], [], [], [], [], []]
    for i in range(9):
        for j in range(9):
            board_cube[i].append(j)

    for i in range(9):
        temp_1 = []
        for j in range(9):
            temp_1.append(board[j][i])
            board_cube[(i // 3) * 3 + j // 3][(i % 3) * 3 + j % 3] = board[i][j]
        board_1.append(temp_1)

    def index2orig(index):
        h = index // 9
        v = index % 9
        return h, v

    def bool_place(index, ele):
        h, v = index2orig(index)
        return not (str(ele) in board_cube[(h // 3) * 3 + v // 3] or str(ele) in board_1[v] or str(ele) in board[h])

    def place_num(index):
        h, v = index2orig(index)
        board[h][v] = str(i)
        board_1[v][h] = str(i)
        board_cube[(h // 3) * 3 + v // 3][(h % 3) * 3 + v % 3] = str(i)

    def remove_num(index):
        h, v = index2orig(index)
        board[h][v] = "."
        del board_1[v][h]
        del board_cube[(h // 3) * 3 + v // 3][(h % 3) * 3 + v % 3]

    def dfs(index=0):
        nonlocal flag
        if index == 80:
            return
        h = index // 9
        v = index % 9
        if board[h][v] == '.':
            for i in range(1, 10):
                if bool_place(index, i):
                    place_num(index)
                    dfs(index+1)
                    remove_num(index)

        else:
            while board[h][v] != '.':
                dfs(index + 1)
    flag = True
    dfs()
    return


"""
法2：利用集合加速算法。
"""


def solveSudoku(board):
    """
    :param board:
    :return:
    """
    row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
    col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
    block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字

    empty = []  # 收集需填数位置
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':  # 更新可用数字
                val = int(board[i][j])
                row[i].remove(val)
                col[j].remove(val)
                block[(i // 3) * 3 + j // 3].remove(val)
            else:
                empty.append((i, j))

    def backtrack(iter=0):
        if iter == len(empty):  # 处理完empty代表找到了答案
            return True
        i, j = empty[iter]
        b = (i // 3) * 3 + j // 3
        for val in row[i] & col[j] & block[b]:
            row[i].remove(val)
            col[j].remove(val)
            block[b].remove(val)
            board[i][j] = str(val)
            if backtrack(iter + 1):
                return True
            row[i].add(val)  # 回溯
            col[j].add(val)
            block[b].add(val)
        return False

    backtrack()


"""
作者：yybeta
链接：https://leetcode-cn.com/problems/sudoku-solver/solution/pythonsethui-su-chao-guo-95-by-mai-mai-mai-mai-zi/
"""
if __name__ == '__main__':
    a = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    solveSudoku_1(a)
    print(a)
