# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 12:09
# @Author  : WuxieYaYa
"""
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

链接：https://leetcode-cn.com/problems/binary-tree-right-side-view
"""

from full_binary_tree import Node, Tree
from collections import deque


class Node(object):
    """节点类"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


def rightSideView(root: Node):
    dep_dict = dict()
    max_dep = -1
    stack = [(root, 0)]
    while stack:
        node, deep = stack.pop()
        if node is not None:
            max_dep = max(max_dep, deep)
            dep_dict.setdefault(max_dep, node.elem)
            stack.append((node.lchild, deep+1))
            stack.append((node.rchild, deep+1))

    return [dep_dict[i] for i in range(max_dep)]


if __name__ == '__main__':
    l = [1, 2, 3, None, 5, None, 4]
    tree = Tree()
    for i in l:
        tree.add(i)
    # tree.breadth_travel(tree.root)
    print(rightSideView(tree.root))
