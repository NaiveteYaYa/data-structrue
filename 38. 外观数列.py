# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 20:19
# @Author  : WuxieYaYa

"""
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
6.     312211
7.     13112221
8.     1113213211
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
注意：整数序列中的每一项将表示为一个字符串。

示例 1:

输入: 1
输出: "1"
解释：这是一个基本样例。
示例 2:

输入: 4
输出: "1211"
解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似 "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。

链接：https://leetcode-cn.com/problems/count-and-say
"""


def countAndSay(n):
    if n==1:
        return '1'

    ans = countAndSay(n-1)
    ans = ans + '0'
    i = 0
    m = 1
    result = ''
    while i < len(ans)-1:
        if ans[i] == ans[i+1]:
            m += 1

        else:
            result += str(m) + ans[i]
            m = 1
        i += 1
    return result

if __name__ == '__main__':
    print(countAndSay(6))


