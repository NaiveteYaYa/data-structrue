# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 11:01
# @Author  : WuxieYaYa

"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
    [
      [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]

示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
    [
      [1,2,2],
      [5]
    ]

链接：https://leetcode-cn.com/problems/combination-sum-ii
"""


def combinationSum2(candidates, target):
    """
    执行用时 :112 ms,在所有Python3提交中击败了29.66%的用户
    内存消耗 :13.5 MB, 在所有Python3提交中击败了32.18%的用户
    :param candidates:
    :param target:
    :return:
    """
    temp_list = list(i for i in candidates if i <= target)
    temp_list.sort()
    if temp_list == [] or target < temp_list[0]:  # 此处case的顺序不能变，否则会报错
        return []
    ans = []

    def dfs(path=[], sub=target, index=0):
        if sub == 0 and path not in ans:
            ans.append(path)
        for i, temp in enumerate(temp_list[index:]):
            if sub - temp < 0:
                break
            else:
                dfs(path + [temp], sub=sub - temp, index=index + i + 1)

    dfs()
    return ans


"""
for 循环：
    index = 0， sub = 8， path=[
    
"""

if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    candidates = [2]
    target = 1
    result = combinationSum2(candidates, target=8)
    print(result)
