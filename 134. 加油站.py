# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 20:29
# @Author  : WuxieYaYa

"""
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。
你从其中的一个加油站出发，开始时油箱为空。
如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

说明: 

如果题目有解，该答案即为唯一答案。
输入数组均为非空数组，且长度相同。
输入数组中的元素均为非负数。
示例 1:

输入:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

输出: 3

解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。
示例 2:

输入:
gas  = [2,3,4]
cost = [3,4,3]

输出: -1

解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。

链接：https://leetcode-cn.com/problems/gas-station
"""

from collections import deque
def canCompleteCircuit(gas, cost):
    """
    法 1：
    此法太耗时：击败 11%
    """
    # if sum(gas) < sum(cost):
    #     return -1
    #
    # n = len(gas)
    # if n == 1:
    #     return 0
    # starts = deque([])
    # for i in range(n):
    #     if gas[i] >= cost[i]:
    #         starts.append(i)
    #
    # while starts:
    #     to_be = starts.popleft()
    #     res = gas[to_be] - cost[to_be]
    #
    #     for i in range(1, n):
    #         step = (to_be + i) % n
    #         res += gas[step] - cost[step]
    #         if res < 0:
    #             break
    #         if i == n - 1:
    #             return to_be
    #
    # return -1

    """
    法2： 一次遍历法
    1. 初始化 total_tank 和 curr_tank 为 0 ，并且选择 0 号加油站为起点。

    2. 遍历所有的加油站：
         每一步中，都通过加上 gas[i] 和减去 cost[i] 来更新 total_tank 和 curr_tank 。
         
         如果在 i + 1 号加油站， curr_tank < 0 ，将 i + 1 号加油站作为新的起点，同时重置 curr_tank = 0 ，让油箱也清空。
    
    3. 如果 total_tank < 0 ，返回 -1 ，否则返回 starting station。
    
    链接：https://leetcode-cn.com/problems/gas-station/solution/jia-you-zhan-by-leetcode/
    """
    n = len(gas)
    total_gas, current_gas = 0, 0
    start_station = 0
    for i in range(n):
        total_gas += gas[i] - cost[i]
        current_gas += gas[i] - cost[i]
        if current_gas < 0:
            current_gas = 0
            start_station += 1

    return start_station if total_gas >= 0 else -1


if __name__ == '__main__':
    # gas = [2, 3, 4]
    # cost = [3, 4, 3]
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(canCompleteCircuit(gas,cost))



