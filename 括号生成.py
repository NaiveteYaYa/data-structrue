# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 15:14
# @Author  : WuxieYaYa

"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

        [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]
"""


def generateParenthesis(n):
    """
    1. 暴力递归方法：
        先生成能组合的所有情况，有2**n种。然后将符合条件的添加到结果中。

    时间复杂度：n*2**n个，即对于2**n个序列中的每一个，我们用于建立和验证该序列的复杂度为 O(n)。
    空间复杂度：n*2**n个，每个序列都是有效的。
    """
    # ans = []
    #
    # def valid(A):
    #     flag = 0
    #     for i in A:
    #         flag = flag + 1 if i=='(' else flag-1
    #         if flag < 0:
    #             return False
    #     return flag == 0
    #
    # def generater(A=[]):
    #     if len(A) == 2*n:
    #         if valid(A):
    #             ans.append(''.join(A))
    #
    #     else:
    #         A.append('(')
    #         generater(A)
    #         A.pop()
    #         A.append(')')
    #         generater(A)
    #         A.pop()
    #
    # generater()
    # return ans

    """
    法2. 回溯法：只有在我们知道序列仍然保持有效时才添加 '(' or ')'，而不是像方法一那样每次添加。
                 我们可以通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点，
                 如果我们还剩一个位置，我们可以开始放一个左括号。 如果它不超过左括号的数量，我们可以放一个右括号。    
    """

    sns = []

    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            sns.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    backtrack()
    return sns


if __name__ == '__main__':
    a = generateParenthesis(4)
    print(a)
