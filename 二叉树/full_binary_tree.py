# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 13:00
# @Author  : WuxieYaYa

""""
二叉树的节点表示以及树的创建
"""
from collections import deque

class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree():
    def __init__(self, root=None):
        self.root = root

    def add(self, item):
        node = Node(item)

        if self.root is None:
            self.root = node

        else:
            queue = deque([])
            queue.append(self.root)
            # 对已有节点层次遍历
            while queue:
                cur = queue.popleft()
                if cur.lchild is None:
                    cur.lchild = node
                    return
                elif cur.rchild is None:
                    cur.rchild = node
                    return
                else:
                    queue.extend(deque([cur.lchild, cur.rchild]))

    def breadth_travel(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.elem,)
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)