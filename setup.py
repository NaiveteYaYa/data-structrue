# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 18:02
# @Author  : WuxieYaYa


from collections.abc import Iterable, Iterator

a = [1,2,3]
b = iter(a)
print(b)
print(next(b))
print(next(b))
print(isinstance(b, Iterator))
print(isinstance(a, Iterable))
print(isinstance(b, Iterable))
for i in b:
      print(i)
def a():
      yield 1
      name = 'asdf'
      yield 2
      age = '33'
      return 'aaa'

