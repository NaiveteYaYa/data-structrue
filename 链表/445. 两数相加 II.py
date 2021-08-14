# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 16:00
# @Author  : WuxieYaYa

"""
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。
将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶：
如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7

链接：https://leetcode-cn.com/problems/add-two-numbers-ii
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    # 建立头结点
    re = ListNode(0)
    r = re
    carry = 0
    while (l1 or l2):
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        s = carry + x + y
        carry = s // 10
        r.next = ListNode(s % 10)
        r = r.next
        if (l1 != None): l1 = l1.next
        if (l2 != None): l2 = l2.next
    if (carry > 0):
        r.next = ListNode(1)
    return re.next

if __name__ == '__main__':

    lis1 = [7, 2, 4, 3]
    lis2 = [5, 6, 4]
    l1 = ListNode(lis1[0])
    l2 = ListNode(lis2[0])
    tail = l1  # 尾插法
    for i in lis1[1:]:
        p = ListNode(i)
        tail.next = p
        tail = p

    tail2 = l2  #尾插法
    for j in lis2[1:]:
        p = ListNode(j)
        tail2.next = p
        tail2 = p

    res = addTwoNumbers(l1, l2)
    ll = []
    while res:
        ll.append(res.val)
        res = res.next
        
    print(ll)

    aa = ListNode(None)
    print(aa is None)
        





