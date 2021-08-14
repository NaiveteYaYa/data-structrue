# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 16:37
# @Author  : WuxieYaYa

"""
    给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
    注意：
    答案中不可以包含重复的四元组。

示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

链接：https://leetcode-cn.com/problems/4sum
"""


def fourSum(nums, target):
    """
    法1：利用回溯穷举搜索，此法超出时间限制，时间复杂度太高
    :param nums:
    :param target:
    :return:
    """
    #
    # nums.sort()
    # ans = []
    #
    # def dfs(path=[], cur=0):
    #     if sum(path)>target:
    #         return
    #     if sum(path) == target and len(path)==4 and path not in ans:
    #         ans.append(path)
    #         return
    #     for i, num in enumerate(nums[cur:]):
    #         if len(path)==0 and num>target:
    #             return
    #         if num>0 and sum(path)>target:
    #             break
    #         dfs(path + [num], cur + 1 + i)
    #
    # dfs()
    # return ans

    """
    法2：类似于 三数之和
    todo: 
    """
    """
    class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        if not nums or len(nums) < 4:
            return result
        nums.sort()
        length = len(nums)
        for k in range(length - 3):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            min1 = nums[k] + nums[k+1] + nums[k+2] + nums[k+3]
            if min1 > target:
                break
            max1 = nums[k] + nums [length-1] + nums[length - 2] + nums[length - 3]
            if max1 < target:
                continue
            for i in range(k+1, length-2):  
                if i > k + 1 and nums[i] == nums[i - 1]:
                    continue
                j = i + 1
                h = length - 1
                min2 = nums[k] + nums[i] + nums[j] + nums[j + 1]
                if min2 > target:
                    continue
                max2 = nums[k] + nums[i] + nums[h] + nums[h - 1]
                if max2 < target:
                    continue
                while j < h:
                    curr = nums[k] + nums[i] + nums[j] + nums[h]
                    if curr == target:
                        result.append([nums[k], nums[i], nums[j], nums[h]])
                        j += 1
                        while j < h and nums[j] == nums[j - 1]:
                            j += 1
                        h -= 1
                        while j < h and i < h and nums[h] == nums[h + 1]:
                            h -= 1
                    elif curr > target:
                        h -= 1
                    elif curr < target:
                        j += 1
        return result

        作者：jutraman
    链接：https://leetcode-cn.com/problems/4sum/solution/pythonsi-shu-zhi-he-by-jutraman/
    """

    """
    法3：
    通过散列表：hashmap：将列表中能每两个数能够组成的数做key，相应和位key的是对应的value值。
    todo:python写法的去重操作，目前不会。回头看
    优化前：费时费空间

    作者：wotxdx
    链接：https://leetcode-cn.com/problems/4sum/solution/tong-guo-san-lie-biao-jie-jue-ci-ti-by-wotxdx/
    """

    # n = len(nums)
    # if n < 4:
    #     return []
    # nums.sort()
    # hashmap = {}
    # results = []
    # for i in range(n - 1):
    #     repeat = set()
    #     for j in range(i + 1, n):
    #         sum_ij = nums[i] + nums[j]
    #
    #         if sum_ij not in repeat:
    #             if hashmap.get(sum_ij) is None:
    #                 hashmap[sum_ij] = [[i, j]]
    #             else:
    #                 hashmap[sum_ij].append([i, j])
    #         t = target - sum_ij
    #         repeat.add(t)
    # ans = []
    # temp = list(hashmap.keys())
    # temp.sort()
    # for i in range(len(temp)):
    #     if (target - temp[i]) in temp[i:]:
    #         ans.append([temp[i], target - temp[i]])
    # for a, b in ans:
    #     for i in hashmap[a]:
    #         i_1, i_2 = i
    #         for j in hashmap[b]:
    #             j_1, j_2 = j
    #             tem = {i_1, i_2, j_1, j_2}
    #             if len(tem) != 4:
    #                 continue
    #             aaa = [nums[res] for res in tem]
    #             aaa.sort()
    #             if aaa not in results:
    #                 results.append(aaa)
    #
    # return results

    #     # 优化
    # d={}
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         d.setdefault(nums[i]+nums[j],[]).append((i,j))
    # result=set()
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         for a,b in d.get(target-nums[i]-nums[j],[]):
    #             temp={i,j,a,b}
    #             if len(temp)==4:
    #                 result.add(tuple(sorted(nums[t] for t in temp)))
    # return result

    d = {}
    n = len(nums)
    for i in range(n - 1):
        for j in range(i+1, n):
            d.setdefault(nums[i] + nums[j], []).append([i, j])

    result = []
    for i in range(n):
        for j in range(i+1, n):
            for a, b in d.get(target - nums[i] - nums[j], []):
                temp = {a, b, i, j}
                if len(temp) == 4:
                    ll = sorted(nums[n] for n in temp)
                    if ll not in result:
                        result.append(ll)

    return result


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    nums = [0, 0, 0, 0]
    nums = [-3, -1, 0, 2, 4, 5]
    nums = [1, -2, -5, -4, -3, 3, 3, 5]
    # [
    #     [-1, 0, 0, 1],
    #     [-2, -1, 1, 2],
    #     [-2, 0, 0, 2]
    # ]
    # #
    num = [10, -4, -4, 7, -2, 0, -2, -6, 9, -5, 3, 10, 8, 0, 9, -8, 3, -9, -5]
    target = 8
    result = fourSum(nums, target=-11)
    print(result)
