# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 16:28
# @Author  : WuxieYaYa

"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head, n):
    num = 0
    node = head
    while node.next is not None:
        num += 1
    num -= n + 1

    node = head
    if num == -1:
        head = head.next
    else:
        while num:
            node = node.next
            num -= 1
        node.next = node.next.next

    return head