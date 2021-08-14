# -*- coding: utf-8 -*-
# @Time    : 2021/3/27 10:16
# @Author  : WuxieYaYa

"""
总体思想：
    - 有点类似dp的思想
        - 即，只保证当下是最优策略。之后加进来的数字 p 放在队尾，数字 p 依次与前边的元素进行比较后插入其正确的位置

    二代目比初代目时间复杂度好很多。
"""


# 初代目
def insert_sort(alist):
    n = len(alist)
    for i in range(1, n):  # 从第二个元素开始，向前插入。
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
    return alist


# 二代目
def insert_sort_2v(alist):
    n = len(alist)

    for i in range(1, n):
        j = i
        while alist[j] < alist[j-1]:
            alist[j], alist[j-1] = alist[j-1], alist[j]

    return alist

if __name__ == '__main__':
    import random, time
    alist = random.choices(range(10000), k=10000)
    alist_copy = [i for i in alist]
    # print(alist)

    a = time.time()

    print(alist[:10])
    insert_sort(alist)
    b = time.time() - a
    print(f"v1:  {b}")

    print(alist_copy[:10])
    insert_sort_2v(alist_copy)
    c = time.time() - b - a
    print(f"v2:  {c}")

    """
    [1839, 8448, 5491, 5116, 3315, 5907, 2247, 8954, 3018, 7969]
    v1:  0.0029921531677246094
    [1839, 5491, 5116, 3315, 5907, 2247, 8448, 3018, 7969, 2905]
    v2:  8.80943489074707
    """


