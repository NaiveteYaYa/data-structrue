# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 22:39
# @Author  : WuxieYaYa

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
例子：
    输入: "([)]"
    输出: false
"""

def isValid(s):

    # 2 此法完美,但是耗时68ms,13.5M内存
    # while '{}' in s or '()' in s or '[]' in s:
    #     s = s.replace('{}', '')
    #     s = s.replace('[]', '')
    #     s = s.replace('()', '')
    # return s == ''

    # 3，此法 32ms, 13.5M
    d = {")": "(", "]": "[", "}": "{"}
    l = []
    for i in s:
        if d.get(i) is None:
            l.append(i)
        elif len(l) == 0 or d.get(i) != l[-1]:
            return False
        elif d.get(i) == l[-1]:  # 此处利用栈的先进后出出
            l.pop()
    if len(l) == 0:
        print('1')
        return True
    else:
        return False

    """
    4. 官方答案
    """

    dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
    stack = ['?']
    for c in s:
        if c in dic:
            stack.append(c)
        elif dic[stack.pop()] != c:
            return False
    return len(stack) == 1



if __name__ == '__main__':
    aaa = "[][{()}()]()"
    isValid(aaa)
