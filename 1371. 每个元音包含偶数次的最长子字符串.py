# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 11:20
# @Author  : WuxieYaYa

"""
给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，
即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。

示例 1：

输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
示例 2：

输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
示例 3：

输入：s = "bcbcbc"
输出：6
解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。
 
提示：
1 <= s.length <= 5 x 10^5
s 只包含小写英文字母。

链接：https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts
"""


def findTheLongestSubstring(s):
    dp = [-float('inf')] * 32
    dp[0] = -1
    pattern = 0
    res = 0
    for i in range(len(s)):
        if s[i] == 'a':
            pattern ^= (1 << 0)
        elif s[i] == 'e':
            pattern ^= (1 << 1)
        elif s[i] == 'i':
            pattern ^= (1 << 2)
        elif s[i] == 'o':
            pattern ^= (1 << 3)
        elif s[i] == 'u':
            pattern ^= (1 << 4)
        if dp[pattern] != -float('inf'):
            cur_len = i - dp[pattern]
            res = max(res, cur_len)
        else:
            dp[pattern] = i
    return res

    """
    链接：https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/solution/xiang-xi-jie-shi-by-will_never_die/
    """

    """
    t, l, r, v = 0, {0: -1}, {0: -1}, {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
    for i, c in enumerate(s):
        t ^= v.get(c, 0)
        r[t] = i
        l.setdefault(t, i)
    return max(map(int.__sub__, r.values(), l.values()))

    链接：https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/solution/1371-mei-ge-yuan-yin-bao-han-ou-shu-ci-de-zui-chan/
    """


if __name__ == '__main__':
    s = "bcbcbc"
    print(findTheLongestSubstring(s))
    map
