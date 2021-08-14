# -*- coding: utf-8 -*-
# @Time    : 2021/6/17 15:11
# @Author  : WuxieYaYa


"""
完全二叉树生成节点的顺序是从上往下，从左往右。

"""


def heapfiy(tree, i, n):
    """
    heapipy的过程就是将 这个节点和其孩子节点进行排序。以 上层节点， 左， 右的顺序从大到小排列。
    :param tree: 列表  LIST
    :param i: 需要排序的堆
    :param n: 此参数将二叉树的范围限制在 n 以内。
    :return:
    """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and tree[i] < tree[l]:
        largest = l

    if r < n and tree[i] < tree[r]:
        largest = r

    if largest != i:
        tree[i], tree[largest] = tree[largest], tree[i]

        heapfiy(tree, largest, n)

def heapsort(tree):
    n = len(tree)

    # build a maxheap
    for i in range(n, -1, -1):
        heapfiy(tree, i, n)

    for i in range(n - 1, 0, -1):
        tree[i], tree[0] = tree[0], tree[i]
        # 这里 n=i 表示 heapify的过程中最大为i。即将最大的放在最后，第一次将最大的放在n-1的位置
        # 之后放在n-2, n-3 ... 直到 1. 最后列表就是个递增的序列。
        heapfiy(tree, 0, i)

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    heapsort(arr)
    print(arr)



