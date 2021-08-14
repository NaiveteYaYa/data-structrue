# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 15:42
# @Author  : WuxieYaYa

import time

#
# def merge(num1, num2):
#     org_n1 = len(num1)
#     p1, p2 = 0, 0
#     while p2 != len(num2) and (p1 - p2 != org_n1):
#         if num1[p1] >= num2[p2]:
#             num1 = num1[:p1] + [num2[p2]] + num1[p1:]
#             p1 += 1
#             p2 += 1
#         else:
#             p1 += 1
#     num1 = num1 + num2[p2:]
#
#     return num1
#
#
#
# if __name__ == '__main__':
#     a = [1, 3, 5, 7, 9, 33, 55]
#     b = [3, 4, 6, 8, 9, 22, 44]
#     print(merge(a, b))


sentences = [['苹果', '香蕉', '榴莲', '梨', '芒果'], ['苹果', '李子', '榴莲', '虾米', '榴莲'], ['猕猴桃', '李子', '西瓜', '香瓜', '南瓜', '冬瓜']]
foods = list(set([food for sent in sentences for food in sent]))
dic = {}
window = 2
top = 3

for sent in sentences:
    for l in range(len(sent)):
        if dic.get(sent[l]) is None:
            dic[sent[l]] = dict()

        start = 0 if l - window < 0 else l - window
        end = len(sent) if l + window >= len(sent) else l + window + 1

        for j in [sent[i] for i in range(start, end) if i != l]:
            dic[sent[l]].setdefault(j, 0)
            dic[sent[l]][j] += 1

for food in foods:
    t = list(sorted(dic[food].items(), key=lambda x: x[1], reverse=True))
    while len(dic[food]) > top:
        t.pop()
        dic[food] = dict(t)

print(dic)
