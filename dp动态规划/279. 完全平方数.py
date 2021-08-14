# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 22:28
# @Author  : WuxieYaYa

"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

链接：https://leetcode-cn.com/problems/perfect-squares
"""

def numSquares(n):
    """
    bfs:
    :param n:
    :return:
    """
    from collections import deque
    deq = deque()
    visited = set()

    deq.append((n,0))

    while deq:
        number, step = deq.popleft()
        targets = [number - i**2 for i in range(1, int(number**0.5)+1)]
        for target in targets:
            if target == 0:
                return step + 1
            if target not in visited:
                deque.append((target, step+1))
                visited.add(target)

    return -1




if __name__ == '__main__':
    print(numSquares(44))