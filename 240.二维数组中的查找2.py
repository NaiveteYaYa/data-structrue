# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 15:30
# @Author  : WuxieYaYa

"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
 
示例:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。

限制：
0 <= n <= 1000
0 <= m <= 1000

链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof

"""
"""
解题思路：
    若使用暴力法遍历矩阵 matrix ，则时间复杂度为 O(N*M)。暴力法未利用矩阵 “从上到下递增、从左到右递增” 的特点，显然不是最优解法。
本题解利用矩阵特点引入标志数，并通过标志数性质降低算法时间复杂度。

标志数引入： 此类矩阵中左下角和右上角元素有特殊性，称为标志数。

        - 左下角元素： 为所在列最大元素，所在行最小元素。
        - 右上角元素： 为所在行最大元素，所在列最小元素。
        - 标志数性质： 将 matrix 中的左下角元素（标志数）记作 flag ，则有:

若 flag > target ，则 target 一定在 flag 所在行的上方，即 flag 所在行可被消去。
若 flag < target ，则 target 一定在 flag 所在列的右方，即 flag 所在列可被消去。
    本题解以左下角元素为例，同理，右上角元素 也具有行（列）消去的性质。
算法流程： 根据以上性质，设计算法在每轮对比时消去一行（列）元素，以降低时间复杂度。

从矩阵 matrix 左下角元素（索引设为 (i, j) ）开始遍历，并与目标值对比：
当 matrix[i][j] > target 时： 行索引向上移动一格（即 i--），即消去矩阵第 i 行元素；
当 matrix[i][j] < target 时： 列索引向右移动一格（即 j++），即消去矩阵第 j 列元素；
当 matrix[i][j] == target 时： 返回 truetrue 。
若行索引或列索引越界，则代表矩阵中无目标值，返回 falsefalse 。
算法本质： 每轮 i 或 j 移动后，相当于生成了“消去一行（列）的新矩阵”， 索引(i,j) 指向新矩阵的左下角元素（标志数），因此可重复使用以上性质消去行（列）。

复杂度分析：
时间复杂度 O(M+N) ：其中，NN 和 MM 分别为矩阵行数和列数，此算法最多循环 M+NM+N 次。
空间复杂度 O(1): i, j 指针使用常数大小额外空间。

作者：jyd
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/solution/mian-shi-ti-04-er-wei-shu-zu-zhong-de-cha-zhao-zuo/
"""


def findNumberIn2DArray(matrix, target):
    # n = len(matrix)-1
    # r, c = n, 0
    # while r>=   0 and c<len(matrix[0]):
    #     if matrix[r][c] < target:
    #         c += 1
    #     elif matrix[r][c] > target:
    #         r -= 1
    #     else:
    #         return True
    # return False

    """
    解法2：
        从对角线开始比较
        todo:此法有瑕疵
    """
    if target < matrix[0][0]:
        return False
    r = len(matrix) - 1
    c = len(matrix[0]) - 1
    i, j = 0, 0
    diagonal_max = 0
    diagonal_min = 0

    while i <= r or j <= c:
        if matrix[i][j] < target:
            i += 1
            j += 1
        else:
            diagonal_max = r if i==r else i+1
            diagonal_min = i
            break
    if target < matrix[0][0]:
        return False
    if diagonal_max == diagonal_min == 0:
        test = matrix[0][:]
    else:
        test = matrix[diagonal_min][diagonal_min:] + matrix[diagonal_max][:diagonal_max]

    begin = 0
    end = len(test) - 1
    while begin <= end:
        mid = (begin + end) // 2
        if test[mid] == target:
            return True
        elif test[mid] > target:
            end = mid - 1
        else:
            begin = mid + 1
    return False


if __name__ == '__main__':
    a = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

    t = 20
    res = findNumberIn2DArray(a, t)
    print(res)
