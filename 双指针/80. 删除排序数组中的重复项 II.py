# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 14:07
# @Author  : WuxieYaYa

"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定 nums = [1,1,1,2,2,3],
函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
你不需要考虑数组中超出新长度后面的元素。
示例 2:
给定 nums = [0,0,1,1,1,1,2,3,3],
函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
你不需要考虑数组中超出新长度后面的元素。

链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
"""

def removeDuplicates(nums):
    """
    法：双指针法，32ms，99.2%,     13.3mb, 8%
        覆盖多余重复项，
        因为 for 循环中range（len(nums))一旦开始循环就不变，如果贸然删除nums内元素，则out of index
    :param nums:
    :return:
    """
    # length = 1
    # flag = 1
    # for i in range(1,len(nums)):
    #     if nums[i] != nums[length-1]:
    #         nums[length] = nums[i]
    #         length += 1
    #         flag = 1
    #     else:
    #         if flag == 1:
    #             nums[length] = nums[i]
    #             length += 1
    #             flag += 1
    #
    # del nums[length:]
    #
    # return length

    """
    法2：删除多余重复项：
    利用独立于len（nums)的count，来进行循环，从而即删除nums元素，又不用担心out of index
    time： 36   97.5%
    space：13.6  7%
    """
    count = 1
    flag = 0
    while count < len(nums):   # while循环在每次循环前都会判定，所以len（nums）会随之改变。
        if nums[count] == nums[count -1]:
            flag += 1
            if flag == 1:
                count += 1
            else:
                del nums[count]
        else:
            flag = 0
            count += 1
    return count
    #
    # # 去flag法：
    # i = 2
    # while i < len(nums):
    #     if nums[i] == nums[i - 2]:
    #         nums.pop(i)
    #     else:
    #         i += 1
    # return len(nums)





if __name__ == '__main__':
    nums = [0,0,1,1,1,1,2,3,3]
    print(removeDuplicates(nums))
    print(nums)