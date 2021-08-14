# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 11:27
# @Author  : WuxieYaYa

"""
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

链接：https://leetcode-cn.com/problems/add-binary
"""
def addBinary(a, b):

    # 法1： 逐位计算
    # 费空间13.7MB， 时间也不是最快:48ms
    # n = max(len(a), len(b))
    # a, b = a.zfill(n), b.zfill(n)
    # ans = ''
    # carry = 0
    # for i in range(n-1, -1, -1):
    #     if a[i] == '1':
    #         carry += 1
    #     if b[i] == '1':
    #         carry += 1
    #     ans += str(carry%2)
    #     carry //= 2
    #
    # if carry == 1:
    #     ans += str(carry)
    #
    # return ans[::-1]



    # 法2：
    # · 位运算
    a, b = int(a, 2), int(b, 2)
    while b:
        answer = a ^ b
        carry = (a & b) << 1
        a, b = answer, carry
    return bin(a)[2:]




if __name__ == '__main__':
    a = "1010"
    b = "1011"
    print(addBinary(a,b))

