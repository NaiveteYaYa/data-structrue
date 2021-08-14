# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 22:51
# @Author  : WuxieYaYa


def quicksort(alist, start, end):
    # 递归退出条件
    if start >= end:
        return

    low = start
    high = end
    key = alist[low]

    while start < end:
        while start < end and alist[end] > key:
            end -= 1
        alist[start] = alist[end]
        while start < end and alist[start] <= key:
            start += 1
        alist[end] = alist[start]
    alist[end] = key
    quicksort(alist, low, end - 1)
    quicksort(alist, end + 1, high)


def quicksort2(arr, low, hig):
    if low == hig:
        return

    pivot = arr[low]

    while low < hig:
        while low < hig and arr[hig] > pivot:
            hig -= 1
        arr[low] = arr[hig]

        while low < hig and arr[low] < pivot:
            low += 1
        arr[hig] = arr[low]




if __name__ == '__main__':
    a = [12, 3, 4, 44, 55, 2, 1, 56, 74, 22, 12, 8, 6, 33]
    quicksort(a, 0, len(a) - 1)
    print(a)

    # if start >= end:
#        return
# pivot = A[0]
# while start < end:
#     while A[end] <= pivot and start < end:
#         end -= 1
#     A[start] = A[end]
#     while A[start] >= pivot and start < end:
#         start += 1
#     A[end] = A[start]
#
# A[start] = pivot
#
# quicksort(A, 0, start-1)
# quicksort(A, start + 1, end)
