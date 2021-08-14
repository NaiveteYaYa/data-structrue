# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 13:37
# @Author  : WuxieYaYa

"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
"""


def subsets(nums):
    """
    法1；二进制
         bin                        reverse
        0b0
        ['0']                       ['0']
        0b1
        ['1']                       ['1']
        0b10
        ['1', '0']                  ['0','1']
        0b11
        ['1', '1']                  ['1','1']
        0b100
        ['1', '0', '0']             ['0','0','1']
        0b101
        ['1', '0', '1']
        0b110
        ['1', '1', '0']
        执行用时 :40 ms, 在所有 Python3 提交中击败了52.63%的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了27.56%的用户
    """
    # ans = []
    # n = 2 ** len(nums)
    # for i in range(n):
    #     temp = list(bin(i))[2:]
    #     ans.append(temp)
    #
    # for j in ans[:n]:
    #     tem = []
    #     # [1,2,3]
    #     # 0:[] 1:3  10:2  11:[2,3] 110:[1]  101:[1,3]
    #     j.reverse()
    #     for index, h in enumerate(j):
    #         if h == '1':
    #             tem.append(nums[index])
    #         else:
    #             continue
    #
    #     ans.append(tem)
    # return ans[n:]

    """
    二进制法2.通过位运算节省时间复杂度
            nth_bit = 1 << n
            for i in range(2**n):
                # generate bitmask, from 0..00 to 1..11
                bitmask = bin(i | nth_bit)[3:]
            此处等同于：
            for i in range(2**n, 2**(n+1)):
                bin(i)[3:]    
            品！！！！
            
    链接：https://leetcode-cn.com/problems/subsets/solution/zi-ji-by-leetcode/
        将其转换成统一标准
    0           000
    1           001
    10          010
    11          011 
    100         100
    101         101
    110         110
    111         111
    """
    # n_bit = 1 << len(nums)
    # for i in range(n):
    #     mask = bin(i | n_bit)[3:]
    #     ans.append([nums[j] for j in range(len(nums)) if mask[j] == '1'])
    #
    # return ans

    """
    二、迭代法
        开始假设输出子集为空，每一步都向子集添加新的整数，并生成新的子集。
    
    """
    # n = len(nums)
    # output = [[]]
    #
    # for num in nums:
    #     output += [curr + [num] for curr in output]
    #
    # return output

    """
    三、回溯法：
        幂集是所有长度从 0 到 n 所有子集的组合。根据定义，该问题可以看作是从序列中生成幂集。
        遍历子集长度，通过回溯生成所有给定长度的子集。
    """
    ans = []
    n = len(nums)
    
    def helper(k, temp):
        ans.append(temp)
        for i in range(k,n):
            helper(i+1, temp+[nums[i]])

    helper(0, [])
    return ans





if __name__ == '__main__':
    print(subsets([1, 2, 3]))
