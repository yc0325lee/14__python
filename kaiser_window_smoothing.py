# vim: ft=python ts=4 sw=4 tw=999 expandtab
# ----------------------------------------------------------------------------
# File : kaiser_window_smoothing.py
# Description : 
# Author : yc0325lee
# Created : 2021-08-17 18:02:52 by lee2103
# Modified : 2021-08-17 18:02:52 by lee2103
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

def smooth(x,beta):
    """ kaiser window smoothing """
    window_len=11
    # extending the data at beginning and at the end
    # to apply the window at the borders
    s = np.r_[x[window_len-1:0:-1],x,x[-1:-window_len:-1]]
    w = np.kaiser(window_len,beta)
    y = np.convolve(w/w.sum(),s,mode='valid')
    return y[5:len(y)-5]


# random data generation
y = np.random.random(100) * 100 
for i in range(100):
    y[i] = y[i] + i**((150-i)/80.0) # modifies the trend

# smoothing the data
plt.figure(1, figsize=(12.8, 4.8))
plt.plot(y, '-k', label="original signal", alpha=.3)

beta = [2, 4, 16, 32]
for b in beta:
    yy = smooth(y, b)
    plt.plot(yy, label="filtered (beta = "+str(b)+")")

plt.legend()
plt.grid()
plt.savefig("kaiser_window_smoothing.png")
plt.show()
