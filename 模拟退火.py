# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 21:49
# @Author  : WuxieYaYa

from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
import math

def aimf(x):
    return x**3 - 60*x**2 - 4*x + 6

# x = [i/10 for i in range(1000)]
# y = [0 for _ in range(1000)]
#
# for i in range(1000):
#     y[i] = aimf(x[i])
#
# plt.plot(x, y)
# plt.show()

T = 1000
Tmin = 10
x = np.random.uniform(0,100)
k = 50
y = 0
t = 0
while T >= Tmin:
    for i in range(k):
        y = aimf(x)
        xnew = x + np.random.uniform(-0.055，0.055)




if __name__ == '__main__':
