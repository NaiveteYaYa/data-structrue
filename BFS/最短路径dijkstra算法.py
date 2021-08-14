# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 14:53
# @Author  : WuxieYaYa

"""
https://www.bilibili.com/video/av25763384/?spm_id_from=trigger_reload
"""
import heapq
import math

graph = {
    "A": {'B': 5, 'C': 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}

def init_distance(graph, s):
    distance = {s: 0}
    for vertex in graph:
        if vertex != s:
            distance[vertex] = math.inf
    return distance

def dijkstra(graph, s):
    pqueue = list()
    heapq.heappush(pqueue, (0, s))
    ans = set()
    parent = {s: None}
    distance = init_distance(graph,s)
    while pqueue:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        ans.add(vertex)

        nodes = graph[vertex].keys()
        for node in nodes:
            if node not in ans:
                if dist + graph[vertex][node] < distance[node]:
                    heapq.heappush(pqueue, (dist + graph[vertex][node], node))
                    parent[node] = vertex
                    distance[node] = dist + graph[vertex][node]

    return parent, distance


if __name__ == '__main__':
    p, d = dijkstra(graph, "A")
    print(p)
    print(d)
    v = 'F'
    while v!=None:
        print(v)
        v = p[v]

