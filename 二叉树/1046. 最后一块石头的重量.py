# -*- coding: utf-8 -*-
# @Time    : 2020/5/2 23:17
# @Author  : WuxieYaYa

"""
有一堆石头，每块石头的重量都是正整数。
每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。

示例：

输入：[2,7,4,1,8,1]
输出：1
解释：
先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。
 
提示：

1 <= stones.length <= 30
1 <= stones[i] <= 1000

链接：https://leetcode-cn.com/problems/last-stone-weight
"""
import heapq
from collections import deque

def lastStoneWeight(stones):
    """
    法1 ： 用排序算法做，
            时间：40ms， 66%
            空间：13.6， 9%
    """
    # stack = sorted(stones)
    # while len(stack) > 1:
    #     a, b = stack[-2:]
    #     stack = stack[:-2]
    #     if a != b:
    #         stack.append(abs(a - b))
    #         stack.sort()
    #
    # return stack[0] if stack else 0

    """
    法2 ： 用堆
    """
    stones_heap = [-i for i in stones]
    heapq.heapify(stones_heap)
    while len(stones_heap) > 1:
        a = heapq.heappop(stones_heap)
        b = heapq.heappop(stones_heap)
        if a < b:
            heapq.heappush(stones_heap, a - b)
    if stones_heap:
        res = -stones_heap[0]
    else:
        res = 0

    return res


if __name__ == '__main__':
    s = [2,7,4,1,8,1]
    print(lastStoneWeight(s))