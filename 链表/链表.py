# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 16:20
# @Author  : WuxieYaYa

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(0)
l1.next = ListNode(0.5)
l1.next.next = ListNode(1)
# l2 = ListNode(1)
# l2.val = 3
ll = l1
ll.next = ll.next.next
l1.next.next = None
print(l1.val, l1.next.val, l1.next.next.val)