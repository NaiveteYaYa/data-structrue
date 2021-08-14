# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 21:28
# @Author  : WuxieYaYa

"""
无限迭代器

    迭代器         参数         结果                                                例子
    count()     start, [step]   start, start+step, start+2*step, ...                count(10) --> 10 11 12 13 14 ...
    cycle()     p               p0, p1, ... plast, p0, p1, ...                      cycle('ABCD') --> A B C D A B C D ...
    repeat()    elem [,n]       elem, elem, elem, ... endlessly or up to n times    repeat(10, 3) --> 10 10 10


处理输入序列迭代器

    迭代器          参数            结果                                        例子
    chain()     p, q, ...           p0, p1, ... plast, q0, q1, ...              chain('ABC', 'DEF') --> A B C D E F
    compress()  data, selectors     (d[0] if s[0]), (d[1] if s[1]), ...         compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
    dropwhile() pred, seq           seq[n], seq[n+1], starting when pred fails  dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
    groupby()   iterable[, keyfunc] sub-iterators grouped by value of keyfunc(v)
    ifilter()   pred, seq           elements of seq where pred(elem) is True    ifilter(lambda x: x%2, range(10)) --> 1 3 5 7 9
    ifilterfalse()  pred, seq       elements of seq where pred(elem) is False   ifilterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
    islice()    seq, [start,] stop [, step] elements from seq[start:stop:step]  islice('ABCDEFG', 2, None) --> C D E F G
    imap()      func, p, q, ...     func(p0, q0), func(p1, q1), ...             imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000
    starmap()   func, seq           func(*seq[0]), func(*seq[1]), ...           starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
    tee()       it, n               it1, it2 , ... itn splits one iterator into n
    takewhile() pred, seq           seq[0], seq[1], until pred fails            takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
    izip()      p, q, ...           (p[0], q[0]), (p[1], q[1]), ...             izip('ABCD', 'xy') --> Ax By
    izip_longest()  p, q, ...       (p[0], q[0]), (p[1], q[1]), ...             izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-


组合生成器

    迭代器          参数                        结果
    product()       p, q, ... [repeat=1]        cartesian product, equivalent to a nested for-loop
    permutations()  p[, r]                      r-length tuples, all possible orderings, no repeated elements
    combinations()  p, r                        r-length tuples, in sorted order, no repeated elements
    combinations_with_replacement() p, r        r-length tuples, in sorted order, with repeated elements
    product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
    permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
    combinations('ABCD', 2)                     AB AC AD BC BD CD
    combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD
"""