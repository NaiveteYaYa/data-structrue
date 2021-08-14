# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 21:56
# @Author  : WuxieYaYa

"""
给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？

链接：https://leetcode-cn.com/problems/linked-list-cycle
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """快慢指针"""
        # slow = head
        # fast = head
        # while f and fast.next:     # 此处fast.next 是因为只有fast.next成立，fast.next.next 才会成立
        #     slow = slow.next
        #     fast = fast.next.next

        #     if not fast:
        #         return False
        #
        # return False
        """哈希表"""
        d = {}
        while head:
            if head not in d:
                d[head] = 1
            else:
                return True
            head = head.next
        return False
