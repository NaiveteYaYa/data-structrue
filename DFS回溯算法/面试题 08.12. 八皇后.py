# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 13:34
# @Author  : WuxieYaYa

"""
设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。
    这里的“对角线”指的是所有的对角线，不只是平分整个棋盘的那两条对角线。
注意：本题相对原题做了扩展

示例:

 输入：4
 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
 解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
链接：https://leetcode-cn.com/problems/eight-queens-lcci
"""


def solveNQueens(n):
    """
    法1：
    执行用时 92 ms, 在所有 Python3 提交中击败了60.49%的用户
    内存消耗 :13.6 MB, 在所有 Python3 提交中击败了100.00%的用户
    :param n:
    :return:
    """
    # ans = []
    # index = [i for i in range(n)]
    #
    # def dfs(row=0, an=[]):
    #     for i in index:
    #         temp = ['.'] * n  # temp必须写入for循环之内。
    #         temp[i] = 'Q'
    #         index.remove(i)
    #         an.append(temp)
    #
    #         flag = 0
    #         for j in range(i if i < row else row):
    #             if an[row - j - 1][i - 1 - j] == 'Q':
    #                 flag = 1
    #                 break
    #
    #         for z in range(n - i - 1 if (n - i - 1) < row else row):
    #             if an[row - z - 1][i + 1 + z] == 'Q':
    #                 flag = 1
    #                 break
    #         if flag == 0:
    #             if row == n - 1:
    #                 tem = list(map(lambda q: ''.join(q), an))
    #                 ans.append(tem)
    #                 # 这里添加后，必须remove an最后添加的皇后行。此处与else中remove对应。否则不能回溯到第一行。
    #                 an[-1][i] = '.'
    #                 index.append(i)
    #                 index.sort()
    #                 an.pop()
    #                 return
    #             else:
    #                 dfs(row + 1, an)
    #                 an[-1][i] = '.'
    #                 index.append(i)
    #                 index.sort()
    #                 an.pop()
    #
    #         else:
    #             an[-1][i] = '.'
    #             index.append(i)
    #             index.sort()
    #             an.pop()
    #
    # dfs()
    # return ans

    """
    法2：
    一、思路
        这里运用回溯算法对棋盘进行探索，即当发现目前的棋盘无法继续摆放棋子时，退回到上一状态，重新探索。
    值得注意的是，这里最重要的部分在于判断某一位置能否放置皇后，因此引出了两个解法：
    1. 使用了pos记录无法放置棋子的位置
        pos用于记录无法放置棋子的行row和列col，当pos[row][col]=1时，即说明此处无法放置棋子。
        由于我们是逐行放置棋子的，所以不需要考虑同行的位置，另外也不需要考虑在当前行row之上的位置。
    2. 利用arr记录的皇后列数进行逻辑判断
        arr存放的是放置皇后Q的列数，而其在arr中的下标即为皇后的行数。
        这里我们依旧不需要考虑皇后所在的那一行，只需要考虑皇后所在的列和对角线位置。
        对于arr中第t_row个数，也就是第t_row行的皇后而言，其列数为arr[t_row]。
    
    我们要填入的列数col应该满足以下两个条件：
        col != arr[t_row] 即不和之前的皇后同列
        abs(col-arr[t_row]) != row - t_row 即不在皇后的广义对角线上
    
    作者：heimisa000
    链接：https://leetcode-cn.com/problems/eight-queens-lcci/solution/pythonhui-su-suan-fa-yong-shu-zu-ji-lu-qi-zi-wei-z/
    """
    """
    法2：用额外的pos矩阵记录无法放置棋子的位置
    """
    def arrange(t, row, col):  # 对于第row行第col列放置的棋子
        # 计算因为它而无法放置的位置
        # 并记录在数组t中
        # 由于dfs算法逐行放置棋子
        # 这里不需要考虑同一行的情况
        for i in range(row, n):  # 同一列无法放置的位置
            # 由于dfs算法逐行放置
            # 因此小于row行的位置不予考虑
            t[i][col] = 1
        directions = [(1, 1), (1, -1)]  # 计算对角线和反对角线无法放置的位置
        # 同样不考虑小于row行的位置
        # 即dx都为1

        for dx, dy in directions:
            x = row
            y = col
            while x + dx < n and 0 <= y + dy < n:  # 由于dx都为1
                # 这里不需要考虑x+dx<0的边界条件
                t[x + dx][y + dy] = 1
                x += dx
                y += dy
        return t

    def dfs(row, pos, arr):  # 回溯的主体
        # row为当前考虑的行数
        # pos为表明无法放置位置的矩阵
        # arr是每一行Q所在的列数

        if row == n:  # 行数row为n时，说明已经找到填写的位置
            # 在表示结果的res数组中填写结果
            res.append(['.' * i + 'Q' + '.' * (n - 1 - i) for i in arr])
            return  # 返回

        for col in range(n):
            """
            dfs在循环过程中不用删除已添加元素，是因为在循环开始，就将添加元素重置为原始状态。
            """
            if pos[row][col] == 0:  # 查找当前行可放置棋子的列数
                # 计算在放置该棋子情况下的pos矩阵，即temp

                # 为了放置pos矩阵在调用函数过程中被更改
                # 需要逐行复制原来的pos矩阵,因为此处需要深拷贝。
                temp = arrange([pos_row[:] for pos_row in pos], row, col)
                # 继续对下一行进行计算
                dfs(row + 1, temp, arr + [col])


    res = []  # 初始化参数
    row = 0
    pos = [[0] * n for _ in range(n)]
    arr = []
    # 初始调用dfs函数
    dfs(row, pos, arr)
    return res


if __name__ == '__main__':
    aa = solveNQueens(4)
    print(aa)
