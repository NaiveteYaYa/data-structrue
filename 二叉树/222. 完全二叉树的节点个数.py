# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 19:29
# @Author  : WuxieYaYa

"""
给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例:

输入:
    1
   / \
  2   3
 / \  /
4  5 6

输出: 6

链接：https://leetcode-cn.com/problems/count-complete-tree-nodes
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    看题第一眼，就知道本题想玩二分查找，但限于能力不足，先利用栈得到一种解法（即通过计算所有node是否有孩子节点
        来计数，这种解法消耗内存资源太大，所以不是最优解）
    法1：
        递归求解，同样需要遍历所有节点，时间复杂度上并非最优。
            递归求解时：若是最终目的是计数，那么子函数仅仅是一个包含判断并且返回0的函数。
            通过返回值计数可得到结果
    法2：
        二分查找 + 位运算
        TODO：
    """
    def countNodes(self, root: TreeNode) -> int:

        # if not root:
        #     return 0
        # else:
        #     res = 1
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if node.left:
        #         stack.append(node.left)
        #         res += 1
        #     if node.right:
        #         stack.append(node.right)
        #         res += 1

        # return res
        if root is None:
            return 0

        return self.countNodes(root.left) + self.countNodes(root.right) + 1


