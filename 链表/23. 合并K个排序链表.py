# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 10:56
# @Author  : WuxieYaYa

"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
"""
from queue import PriorityQueue
import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists):
    """
    1.暴力求解
    2.逐一比较， 改进=>优先队列   (logk N)
    3.分治思想：不断的合并两个序列,  改进： + 二分使得O(logn k)
    :param lists: ListNode
    :return:
    """

    # 优先队列
    if not lists or len(lists) == 0:
        return None
    heap = []
    # 首先 for 嵌套 while 就是将所有元素都取出放入堆中
    for node in lists:
        while node:
            heapq.heappush(heap, node.val)
            node = node.next
    dummy = ListNode(None)
    cur = dummy
    # 依次将堆中的元素取出(因为是小顶堆，所以每次出来的都是目前堆中值最小的元素），然后重新构建一个列表返回
    while heap:
        temp_node = ListNode(heapq.heappop(heap))
        cur.next = temp_node
        cur = temp_node
    return dummy.next

"""
作者：LotusPanda
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/xiong-mao-shua-ti-python3-3chong-jie-fa-bao-li-you/
"""


if __name__ == '__main__':
    l = [[1, 4, 5], [1, 3, 4], [2, 6]]


