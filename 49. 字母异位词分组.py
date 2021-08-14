# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 11:33
# @Author  : WuxieYaYa

def groupAnagrams(strs):
    """
    法1.时间复杂度：860ms，空间复杂度高：16.6Mb。排名垫底
    :param strs:
    :return:
    """
    # ans_set = []
    # ans = []
    # n = len(strs)
    # for i in range(n):
    #     temp = list(strs[i])
    #     temp.sort()
    #     if temp not in ans_set:
    #         ans_set.append(temp)
    #         ans.append([strs[i]])
    #     else:
    #         for j in range(len(ans_set)):
    #             if temp == ans_set[j]:
    #                 ans[j].append(strs[i])
    #
    # return ans

    """
    法2：利用collections.defaultdict.
    时间复杂度降为52ms，空间：16.7
    """
    from collections import defaultdict
    n = len(strs)
    ans = defaultdict(list)
    for i in strs:
        ans[tuple(sorted(i))].append(i)
    return list(ans.values())

    """
    方法3：按计数分类思路
    当且仅当它们的字符计数（每个字符的出现次数）相同时，两个字符串是字母异位词。
    算法  
    """





if __name__ == '__main__':
    a = ["eat", "tea", "tan", "ate", "nat", "bat"]
    ans1 = groupAnagrams(a)
    print(ans1)
