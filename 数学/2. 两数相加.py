# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 15:47
# @Author  : WuxieYaYa

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

链接：https://leetcode-cn.com/problems/add-two-numbers
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    Newnode = ListNode(0)
    ansnode = Newnode
    flag = 0

    while l1 or l2:
        if l1 and l2:
            s = l1.val + l2.val
            l1 = l1.next
            l2 = l2.next
        elif l1:
            s = l1.val
            l1 = l1.next
        else:
            s = l2.val
            l2 = l2.next
        if flag==0:
            ans







