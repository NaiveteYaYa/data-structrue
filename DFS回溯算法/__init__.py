# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 13:33
# @Author  : WuxieYaYa


"""
回溯算法(backtracking)实际上一个类似枚举的搜索尝试过程，主要是在搜索尝试过程中寻找问题的解，当发现已不满足求解条件时，就“回溯”返回，尝试别的路径。
解题一般步骤：
    （1）针对所给问题，确定问题的解空间：首先应明确定义问题的解空间，问题的解空间应至少包含问题的一个（最优）解。
    （2）确定结点的扩展搜索规则
    （3）以深度优先方式搜索解空间，并在搜索过程中用剪枝函数避免无效搜索。

    亦即：
    choose
    Explore
    un-choose
    同常可以说，分两部分：
        递归 + 限制条件（暴力搜索 + 剪枝）
        1.基本状况
        2.递归状况
"""

"""
    回溯搜索是深度优先搜索（DFS）的一种
    对于某一个搜索树来说（搜索树是起记录路径和状态判断的作用），回溯和DFS，其主要的区别是，
回溯法在求解过程中不保留完整的树结构，而深度优先搜索则记下完整的搜索树。
    为了减少存储空间，在深度优先搜索中，用标志的方法记录访问过的状态，这种处理方法使得深度优先搜索法与回溯法没什么区别了。
"""

"""
深度优先遍历（dfs)的本质是队列栈（stack)，先进先出filo
"""

graph = {
    "A": ['B', 'C'],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def DFS(graph, s):
    stack = list()
    stack.append(s)
    ans = list(s)
    while stack:
        vertex = stack.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in ans:
                stack.append(node)
                ans.append(node)
        print(vertex)
    return ans

"""
    回溯算法中，如果涉及到回溯过程中需要改变内存空间的题目（如：37题求解数独，回溯过程需要将之前填写的数删除，
        因为回溯是一种深度搜索，本身不会改变外在内存状态，所以在回溯过程中对已经改变的外在内存状态无法一起“回溯”）
        则需要在回溯之后将已经改变的外在内存空间再转变成原有状态（如37题中需要将已近填写数删除）
    如78题，39题等，在dfs过程中仅仅需要将符合条件的内容添加到返回值中，无需更改已添加内容。
"""


if __name__ == '__main__':
    a = DFS(graph, 'A')

