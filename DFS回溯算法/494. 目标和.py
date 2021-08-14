# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 23:22
# @Author  : WuxieYaYa

"""
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例：

输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
 

提示：

数组非空，且长度不会超过 20 。
初始的数组的和不会超过 1000 。
保证返回的最终结果能被 32 位整数存下。

链接：https://leetcode-cn.com/problems/target-sum

"""

from time import time
def findTargetSumWays(nums, S):
    # 超时
    # ans = 0
    # n = len(nums)
    # def dfs(idx=0, presum=0):
    #     nonlocal ans
    #     if idx == n:
    #         if presum == S:
    #             ans += 1
    #         return
    #
    #     for i in ('+', '-'):
    #         if i == '+':
    #             dfs(idx + 1, presum+nums[idx])
    #
    #         if i == '-':
    #             dfs(idx + 1, presum-nums[idx])
    # dfs()
    # return ans

    """dp"""
    if sum(nums) < S or (sum(nums) + S) % 2 == 1:
        return 0
    P = (sum(nums) + S) // 2
    dp = [1] + [0 for _ in range(P)]
    for num in nums:
        for j in range(P, num - 1, -1):
            dp[j] += dp[j - num]
    return dp[P]




if __name__ == '__main__':
    b = time()
    print(findTargetSumWays([34,16,5,38,20,20,8,43,3,46,24,12,28,19,22,28,9,46,25,36],0))
    print(time()-b)