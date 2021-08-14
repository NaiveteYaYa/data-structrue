# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 12:43
# @Author  : WuxieYaYa

"""
https://www.bilibili.com/video/BV1Eb41147dK?from=search&seid=635707466898112087
"""


# 二叉树

class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        node = Node(elem)

        if self.root == None:
            self.root = node

        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)


    """
    二叉树遍历：广度优先遍历，深度优先遍历
                广度优先遍历一般用双端队列， 
                深度优先遍历用递归，一般情况下能用递归实现的大部分也能用堆栈来实现
    """

    # 深度优先遍历
    """
    对于一颗二叉树，深度优先搜索(Depth First Search)是沿着树的深度遍历树的节点，尽可能深的搜索树的分支。
    那么深度遍历有重要的三种方法。这三种方式常被用于访问树的节点，它们之间的不同在于访问每个节点的次序不同。
    这三种遍历分别叫做先序遍历（preorder），中序遍历（inorder）和后序遍历（postorder）。
    我们来给出它们的详细定义，然后举例看看它们的应用。
    """

    # 先序遍历 根节点->左子树->右子树

    def preorder(self, root):
        if root == None:
            return
        print(root.elem)
        self.preorder(root.lchild)
        self.preorder(root.rchild)


    """
    中序遍历 在中序遍历中，我们递归使用中序遍历访问左子树，然后访问根节点，最后再递归使用中序遍历访问右子树
    左子树->根节点->右子树
    """

    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.lchild)
        print(root.elem)
        self.inorder(root.rchild)

    def postorder(self, root):
        """递归实现后续遍历"""
        if root == None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem)


        """堆排序"""

def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # 交换

    heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)





