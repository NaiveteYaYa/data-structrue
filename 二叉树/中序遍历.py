# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 21:13
# @Author  : WuxieYaYa

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode) -> List[int]:
    """
    stack
    :param root:
    :return:
    """
    stack = [root]
    res = []
    while stack:
        while root.left:
            stack.append(root.left)
            root = root.left
        node: TreeNode = stack.pop()
        res.append(node.val)

        if node.right:
            stack.append(root.right)
            root = node.right

    return res


def inorderTraversal_1(root: TreeNode) -> List[int]:
    """
    利用递归方式遍历
    :param root:
    :return:
    """
    if root is None:
        return []

    res = []

    def inorder(node: TreeNode):
        if node.left:
            inorder(node.left)
        res.append(node.val)
        if node.right:
            inorder(node.right)

    inorder(root)

    return res


def inorderTraversal_2(root: TreeNode) -> List[int]:
    """
    另一种利用栈来遍历的方式:
            颜色标记法
            通过
            https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
    :param root:
    :return:
    """
    WHITE, GRAY = 0, 1
    res = []
    stack = [(WHITE, root)]

    while stack:
        color, node = stack.pop()
        if node is None:
            continue

        if color == WHITE:
            stack.append((WHITE, node.left))
            stack.append((GRAY, node))
            stack.append((WHITE, node.right))
        else:
            res.append(node.val)

    return res
