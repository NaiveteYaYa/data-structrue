# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 22:50
# @Author  : WuxieYaYa

"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

链接：https://leetcode-cn.com/problems/symmetric-tree
"""
from full_binary_tree import Node, Tree
from collections import deque

def isSymmetric(root):
    """
    笨拙的理解出法1
    :param root:
    :return:
    """
    # l = root.lchild
    # r = root.rchild
    # l_list, r_list = deque([l]), deque([r])
    # while l_list and r_list:
    #     l_node = l_list.popleft()
    #     r_node = r_list.popleft()
    #     if l_node.elem != r_node.elem:
    #         return False
    #
    #     if l_node.rchild is not None or r_node.lchild is not None:
    #         if l_node.rchild is not None and r_node.lchild is not None:
    #             l_list.append(l_node.rchild)
    #             r_list.append(r_node.lchild)
    #         else:
    #             return False
    #
    #     if l_node.lchild is not None or r_node.rchild is not None:
    #         if l_node.lchild is not None and r_node.rchild is not None:
    #             l_list.append(l_node.lchild)
    #             r_list.append(r_node.rchild)
    #         else:
    #             return False
    #
    # return True
    """
    法2：利用递归
    终止条件：
        left 和 right 不等，或者 left 和 right 都为空
        递归的比较 left，left 和 right.right，递归比较 left，right 和 right.left
        链接：https://leetcode-cn.com/problems/symmetric-tree/solution/dong-hua-yan-shi-101-dui-cheng-er-cha-shu-by-user7/
    """
    # TODO: 在熟悉判定，尤其前两个判定 not（left and right） 和not（left or right）
    if not root:
        return True

    def dfs(left, right):
        if not (left or right):
            return True
        if not (left and right):
            return False
        if left.elem != right.elem:
            return False
        return dfs(left.lchild, right.rchild) and dfs(left.rchild, right.lchild)

    return dfs(root.lchild, root.rchild)

if __name__ == '__main__':
    l = [1,2,2,None,3,None,3]
    # l = [1,2,2,3,4,4,3]

    tree = Tree()
    for i in l:
        tree.add(i)

    print(isSymmetric(tree.root))