# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 23:18
# @Author  : WuxieYaYa

""""
    给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
    candidates 中的数字可以无限制重复被选取。
    说明：

    所有数字（包括 target）都是正整数。
    解集不能包含重复的组合。 

    示例 1:
    输入: candidates = [2,3,6,7], target = 7,
    所求解集为:
    [
      [7],
      [2,2,3]
    ]

    示例 2:
    输入: candidates = [2,3,5], target = 8,
    所求解集为:
    [
      [2,2,2,2],
      [2,3,3],
      [3,5]
    ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
法1. 此法没有设置index，使得重复list的出现。
执行用时 :200 ms, 在所有 Python3 提交中击败了11.10%的用户
内存消耗 :16.4 MB, 在所有 Python3 提交中击败了5.06%的用户
"""

# def combinationSum(candidates, target):
#     temp_list = [i for i in candidates if i <= target]
#     temp_list.sort()
#     if temp_list == 0:
#         return
#     ans = []
#
#     def helper(l=[], t=target):
#         if t == 0:
#             ans.append(l)
#         if target < 0:
#             return
#         for temp in temp_list:
#             pivot = t - temp
#             if pivot < 0:
#                 break
#             helper(l+[temp], pivot)
#
#     helper([], target)
#     result = []
#
#     for i in ans:
#         i.sort()
#         if i not in result:
#             result.append(i)
#
#     return result


"""
法2：函数式编程：归纳推理首选函数式编程，将问题分解成子问题，解决最小子问题就解决了整个问题。
# 作者：zhong-xiao-hao
# 链接：https://leetcode-cn.com/problems/combination-sum/solution/python-han-shu-shi-bian-cheng-jie-fa-san-xing-dai-/
"""


def combinationSum(candidates, target):
    if target < 0 or len(candidates) <= 0:
        return []
    if target == 0:
        return [[]]
    return combinationSum(candidates[1:], target) + \
           [[candidates[0]] + cp for cp in combinationSum(candidates, target - candidates[0])]
    # 此法不用index是因为 其candidates[1:]使得list每次向后推一位。





"""
法3：
回溯
def backtrack(path,summ,index)
    path    表示目前存的数字
    summ    表示目前的和
    index   用来避免重复输出，比如[2,2,3],[2,3,2],[3,2,2]这三种其实只表示一个组合，
            我们只挑选递增排列的。设置index，每次递归的时候只在candidates中当前及之后的数字中选择。

作者：juncao8101
链接：https://leetcode-cn.com/problems/combination-sum/solution/hui-su-fa-python-by-juncao8101/
"""


def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if len(candidates) == 0:
        return []
    ans = []

    def backtrack(path, summ, index):
        if summ == target:
            ans.append(path)
        elif summ > target:
            return
        elif summ < target:
            for i in range(index, len(candidates)):
                backtrack(path + [candidates[i]], summ + candidates[i], i)

    backtrack([], 0, 0)
    return ans


if __name__ == '__main__':
    a = [2, 3, 4, 5, 7, 8]
    b = combinationSum(a, 5)
    print(b)
