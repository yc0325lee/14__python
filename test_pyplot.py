# vim: ft=python ts=4 sw=4 tw=999 expandtab
# ----------------------------------------------------------------------------
# File : test_matplotlib.py
# Description : 
# Author : yc0325lee
# Created : 2021-06-19 21:04:26 by lee2103
# Modified : 2021-06-19 21:04:26 by lee2103
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


# data
x = np.arange(0, 6, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()
