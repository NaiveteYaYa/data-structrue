# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 16:54
# @Author  : WuxieYaYa

"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
"""

def lengthOfLongestSubstring(s):
    """
    法1：暴力求解，费时费空间
    :param s:
    :return:
    """
    # n = len(s)
    # top = 0
    # for i in range(n):
    #     temp = [i]
    #     ss = [s[i]]
    #     for j in range(i+1,n):
    #         if j-1 == temp[-1] and s[j] not in ss:
    #             ss.append(s[j])
    #             temp.append(j)
    #         else:
    #             break
    #     if len(temp)>top:
    #         top = len(temp)
    # return top

    """
    法2：利用滑动窗口
    
    作者：superychen
    链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-tu-wen-jiang-jie-by-superychen/
    """
    """# 如果字符串s为空，返回0
    if not s:
        return 0
    # 保存窗口内字符串
    lookup = list()
    n = len(s)
    # 最大子串长度
    max_len = 0
    # 当前窗口长度
    cur_len = 0
    # 遍历字符串s
    for i in range(n):
        val = s[i]
        # 如果该值不在窗口中
        if not val in lookup:
            # 添加到窗口内
            lookup.append(val)
            # 当前长度+1
            cur_len += 1
        # 如果该值在窗口中已存在
        else:
            # 获取其在窗口中的位置
            index = lookup.index(val)
            # 移除该位置及之前的字符，相当于上图中的图3到图4
            lookup = lookup[index + 1:]
            lookup.append(val)
            # 当前长度更新为窗口长度
            cur_len = len(lookup)
        # 如果当前长度大于最大长度，更新最大长度值
        if cur_len > max_len:
            max_len = cur_len
    # 返回最大子串长度
    return max_len"""
    #
    # n = len(s)
    # if n==0:
    #     return 0
    # window = []
    # max_len = 0
    # for i in range(n):
    #     if s[i] not in window:
    #         window.append(s[i])
    #     else:
    #         ind = window.index(s[i])
    #         window = window[ind+1:]
    #         window.append(s[i])
    #     if len(window) > max_len:
    #         max_len = len(window)
    #
    # return max_len

    """
    法3：利用动态规划
    
        一个简单的例子
    
    已知字符串S1='abcc'，其最长无重复子串是'abc'，问字符串S2='abccd'的最长无重复子串长度是什么？
    S1结尾加上'd'之后，最长无重复子串有两种可能的来源：
    最长无重复子串包含新增的'd'，即'cd'
    最长无重复子串不包含新增的'd'，即S1的最长无重复子串'abc'
    比较'cd'与'abc'，len('abc')>len('cd')，所以S2的最长无重复子串依然是'abc'
    
    推导状态转移方程
        lengthOfLongestSubString(Si+1)=max(Li,len(C结尾的无重复子串))
    根据例子的思路推广至一般的情况：
    给出一个字符串Si，已知它的最长子串长度为Li，如果在Si的末尾追加一个字符C，即Si+1=Si+C，那么Si+1的最长子串是多少？
    
    很容易想到：
    
    lengthOfLongestSubString(Si+1)=max(Li,len(C结尾的无重复子串))
    
    思路的具体实现
    
    根据状态转移方程，轻松得到代码，因为查找新增字符结尾的无重复子串长度是向左搜索，所以暂且把这个过程取名叫find_left
    
    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            for i in range(0, len(s)):
                length = max(length, find_left(s, i))
            return length
    接下来，求以s为结尾的无重复子串长度，这就非常容易了
    
    def find_left(s, i):
        tmp_str = s[i]
        j = i - 1
        while j >= 0 and s[j] not in tmp_str:
            tmp_str += s[j]
            j -= 1
        return len(tmp_str)
    最后考虑一些特殊情况
    
    if s == '':
        return 0
    if len(s) == 1:
        return 1
    完整的代码
    
    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            if s == '':
                return 0
            if len(s) == 1:
                return 1
    
            def find_left(s, i):
                tmp_str = s[i]
                j = i - 1
                while j >= 0 and s[j] not in tmp_str:
                    tmp_str += s[j]
                    j -= 1
                return len(tmp_str)
            length = 0
            for i in range(0, len(s)):
                length = max(length, find_left(s, i))
            return length
    
    作者：marcusxu
    链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/python3ti-jie-chao-jian-dan-de-dong-tai-gui-hua-ji/
    """

    n = len(s)
    if n == 0:
        return 0
    if n==1:
        return 1

    def find_left(s, i):
        temp = s[i]
        j = i-1
        while s[i] == s[j]:
            length = i-j
            max(length, )




    """
    利用 hash
    # 可抛弃字符串的索引尾值 - 字符串索引值，该索引值以及之前的字符都属于重复字符串中的一部分，不再在计算中涉及
        ignore_str_index_end = -1
        dic = {}        # 任意字符最后出现在索引的位置 - {字符: 字符索引值}
        max_length = 0  # 最长字符串长度

        for i, c in enumerate(s):
            # 如果字典中已经存在字符c，则字符c重复
            # 如果字符索引值大于ignore_str_index_end，则字符c在需处理的范围内（补充说明请参考备注一）
            if c in dic and dic[c] > ignore_str_index_end:
                # 先更新可抛弃字符串的索引尾值为字符c上一次的索引值
                ignore_str_index_end = dic[c]
                # 再更新字符c的索引值
                dic[c] = i
            # 否则，
            else:
                # 更新字符最近的索引位置
                dic[c] = i
                # 更新最大长度
                max_length = max(i - ignore_str_index_end, max_length)

        return max_length
    
    作者：imckl
    链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/python-hua-dong-chuang-kou-xun-xu-jian-jin-de-3ge-/
    """




if __name__ == '__main__':
    a = "pweae"
    result = lengthOfLongestSubstring(a)
    print(result)
