# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 21:46
# @Author  : WuxieYaYa

def reverse(x):
    ans = ''
    x, res = abs(x), 0
    boundary = (1 << 31) - 1 if x > 0 else 1 << 31

    if x == 0:
        return 0

    """
    while 1:
    if x == 0:
        break
    ans += str(x % 10)
    x //= 10
    result = int(ans) if x > 0 else -int(ans)
    return result if x <= boundary else res
    """
    while x != 0:
        res = res * 10 + x % 10
        if res > boundary:
            return 0
        x //= 10
    return res if x > 0 else -res
"""
        y, res = abs(x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1<<31) -1 if x>0 else 1<<31
        while y != 0:
            res = res*10 +y%10
            if res > boundry :
                return 0
            y //=10
        return res if x >0 else -res

作者：boywithacoin_cn
链接：https://leetcode-cn.com/problems/reverse-integer/solution/pythondan-chu-he-tui-ru-shu-zi-yi-chu-qian-jin-xin/
"""


if __name__ == '__main__':
    a = -2147483412
    reult = reverse(a)
    print(reult)
