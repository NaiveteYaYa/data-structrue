# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 18:56
# @Author  : WuxieYaYa

"""
你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。例如，
字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。
但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。

示例 1：

输入： pattern = "abba", value = "dogcatcatdog"
输出： true
示例 2：

输入： pattern = "abba", value = "dogcatcatfish"
输出： false
示例 3：

输入： pattern = "aaaa", value = "dogcatcatdog"
输出： false
示例 4：

输入： pattern = "abba", value = "dogdogdogdog"
输出： true
解释： "a"="dogdog",b=""，反之也符合规则
提示：

0 <= len(pattern) <= 1000
0 <= len(value) <= 1000
你可以假设pattern只包含字母"a"和"b"，value仅包含小写字母。

链接：https://leetcode-cn.com/problems/pattern-matching-lcci
"""

def patternMatching(pattern,value):
    # TODO:未完待续
    size = len(pattern)
    a_num, b_num = 0, 0
    for i in pattern:
        if i == 'a':
            a_num += 1
    b_num = size - a_num

    for i in range(size//a_num):
        pass


    



if __name__ == '__main__':
    pattern = "abba"
    value = "dogcatcatdog"
    print(patternMatching(pattern, value))