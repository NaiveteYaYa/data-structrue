# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 14:20
# @Author  : WuxieYaYa

"""
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:

输入: [3,2,3]
输出: [3]
示例 2:

输入: [1,1,1,3,3,2,2,2]
输出: [1,2]

链接：https://leetcode-cn.com/problems/majority-element-ii

摩尔投票法的简单理解
与169. 多数元素的两点区别：
    “多数”是指超过n/3，不是n/2，因此最多会有两个元素是众数，要建立两个candidate
    题目没保证多数元素一定存在，所以最后要对candidate进行检验。因此整个流程分为两步：step1投票阶段，step2检验阶段。
    算法核心：
    对于候选者cand1和cand2：
    如果投cand1，cand1加一票。
    如果投cand2，cand2加一票。
    如果投其他元素，cand1和cand2各减一票。
    理解方法：
        在169. 多数元素中，
        如果candidate是多数元素，那么多数元素（>n/2）与其他元素之和（< n/2）对抗，一定赢。
        如果candidate不是多数元素，那么该元素（< n/2）与多数元素和其他元素之和（>n/2）对抗，一定会被打败。
        本题中，分为A``B``others三个阵营
        如果此刻candidate是A和B，那么A（>n/3）与others（<n/3）对抗稳赢，B（>n/3）与others（<n/3）对抗稳赢。
        如果此刻candidate是A和C（C来自others），那么B``C一定是对抗不了B的。
        时间复杂度O(n)，空间复杂度O(1)


    作者：coldme-2
    链接：https://leetcode-cn.com/problems/majority-element-ii/solution/mo-er-tou-piao-fa-de-jian-dan-li-jie-by-coldme-2/
    """


def majorityElement(nums):
    # cand1, vote1 = None, 0
    # cand2, vote2 = None, 0
    # for i in range(len(nums)):
    #     if cand1 is None and cand2 != nums[i]:
    #         cand1 = nums[i]
    #         vote1 += 1
    #
    #     elif cand2 is None and cand1 != nums[i]:
    #         cand2 = nums[i]
    #         vote2 += 1
    #
    #     else:
    #         if cand1 == nums[i]:
    #             vote1 += 1
    #
    #         elif cand2 == nums[i]:
    #             vote2 += 1
    #
    #         else:
    #             vote1 -= 1
    #             vote2 -= 1
    #             if vote1 == 0:
    #                 cand1 = None
    #             if vote2 == 0:
    #                 cand2 = None
    #
    #
    # vote1, vote2 = 0, 0
    # for num in nums:
    #     if num == cand1:
    #         vote1 += 1
    #     if num == cand2:
    #         vote2 += 1
    #
    # ans = []
    # if vote1> len(nums)//3:
    #     ans.append(cand1)
    # if vote2 > len(nums)//3:
    #     ans.append(cand2)
    #
    # return ans


    # 利用列表性质。
    n = len(nums)
    ans = []
    for i in set(nums):
        if nums.count(i) > n//3:
            ans.append(i)
    return ans

if __name__ == '__main__':
    print(majorityElement([1,1,1,3,3,2,2,2]))




