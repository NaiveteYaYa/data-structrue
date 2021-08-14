# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 11:24
# @Author  : WuxieYaYa

"""
广度优先遍历（bfs)的本质是队列queue，先进先出fifo
"""

graph = {
    "A": ['B', 'C'],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def BFS(graph, s):
    queue = list()
    queue.append(s)
    ans = list(s)
    while queue:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in ans:
                queue.append(node)
                ans.append(node)
    return ans


if __name__ == '__main__':
    a = BFS(graph, 'A')
    print(a)
