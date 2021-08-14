# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 13:17
# @Author  : WuxieYaYa

"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。
示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。
 
说明:
为什么返回数值是整数，但输出的答案是数组呢?
请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
"""


def removeDuplicates(nums):
    """
    删除重复元素法：时间64ms，87%， 空间14.4mb，15%
    :param nums:
    :return:
    """
    # flag = 1
    # # for i in range(1, len(nums)):   # 此处不可使用for循环，因为len（nums)只记录一次，之后删除nums内部元素,for 循环内的长度不变，因此会out of index
    # #     if nums[i] == nums[i-1]:
    # #         nums.pop(i)
    # #         flag -= 1
    # while flag<=len(nums)-1:
    #
    #     if nums[flag] == nums[flag-1]:
    #         del nums[flag]
    #     else:
    #         flag += 1
    # return flag

    """
    双指针法: 40ms, 97%,  14.6, 7%
    说明 双指针法，节约啥时间，损失空间。
    """
    flag = 1
    if len(nums) == 0:
        return flag - 1
    for i in range(1, len(nums)):
        if nums[i] != nums[flag - 1]:
            nums[flag] = nums[i]
            flag += 1
    del nums[flag:]
    return flag


if __name__ == '__main__':
    a = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(a))
    print(a)
