# -*- coding: utf-8 -*-
# @Time    : 2021/6/22 19:03
# @Author  : WuxieYaYa

"""
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def anser(root):
    ans = []

    def dfs_node(root: TreeNode):
        if root.left is None:
            ans.append(root.val)

        if root.left:
            return dfs_node(root.left)

        if root.right:
            return dfs_node(root.right)
    dfs_node(root)

    return ans

if __name__ == '__main__':

    K = [34, 76, 45, 18, 26, 54, 92, 38]

    def create_search_tree(l:list):
        start = K.pop()
        tree = TreeNode(start)
        node = tree
        for i in K:
            if tree.val < i and tree.right is None:
                tree.right = i

            else:





