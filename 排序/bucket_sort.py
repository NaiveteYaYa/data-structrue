# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 12:29
# @Author  : WuxieYaYa

def bucketSort(nums):
    max_num = max(nums)
    bucket = [0] * (max_num + 1)
    for i in nums:
        bucket[i] += 1

    sort_num = []

    for j in range(len(bucket)):
        if bucket[j] != 0:
            for y in range(bucket[j]):
                sort_num.append(j)

    return sort_num
