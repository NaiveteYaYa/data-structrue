# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 13:43
# @Author  : WuxieYaYa

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: TreeNode) -> List[int]:
    """
    法1 ：
    利用栈的特性，先进后出，让右子树先进左子树后进。
        第一轮，后进的左子树先出，拿到val， 在将这一层的右子树压栈，左子树压栈，
        第二轮，第二层的左子树依然先出，拿到val后，。。。
        直到其左子树为None， 开始循环右子树。

    :param root:
    :return:
    """
    if root is None:
        return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def preorder_traversal_rec(root: TreeNode) -> List[int]:
    """
    法 2： 递归形式
    :param root:
    :return:
    """
    res = []

    def preorder(Node: TreeNode):
        if Node:
            nonlocal res
            res.append(Node.val)
            preorder(Node.left)
            preorder(Node.right)

    preorder(root)

    return res
