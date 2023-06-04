# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# File : lib__numpy.random.py
# Author : yc0325lee
# Created : 2022-09-20 23:22:32 by lee2103
# Modified : 2022-09-20 23:22:32 by lee2103
# Description : 
# ----------------------------------------------------------------------------
import numpy as np

def ndarray_info(a, name="unknown", verbose=False):
    if type(a).__name__ == "ndarray":
        print("# ndarray_info({})".format(name))
        print("  ndim=", a.ndim)
        print("  shape=", a.shape)
        print("  size=", a.size)
        print("  dtype.name=", a.dtype.name)
        print("  itemsize=", a.itemsize)
        if verbose:
            print("  data=", a.data) # address
            print("  {} =".format(name))
            print(a, end='\n\n')
    else:
        print("[err ] type({}) is not ndarray!".format(name))

if False:
    # random.rand(d0, d1, ..., dn)
    # ; create an array of the given shape and populate it with random samples
    #   from a uniform distribution over [0, 1).
    a = np.random.rand(3, 4)
    ndarray_info(a, "a", True)

if False:
    # random.random_sample(size=None)
    # ; return random floats in the half-open interval [0.0, 1.0).
    # ; results are from the "continuous uniform" distribution over the stated
    #   interval. 
    # ; (b - a) * random_sample() + a
    a = np.random.random_sample(size=(3, 4))
    ndarray_info(a, "a", True)


if False:
    # - random.randn(d0, d1, ..., dn)
    # ; return a sample (or samples) from the "standard normal" distribution
    # ; if positive int_like arguments are provided, randn generates an array of shape (d0, d1, ..., dn),
    #   filled with random floats sampled from a univariate "normal" (gaussian) distribution of mean 0 and variance 1.
    # ; a single float randomly sampled from the distribution is returned if no argument is provided.
    val = np.random.randn()
    print("val=", val)

    mean = 0.0
    sigma = 0.2
    a = mean + sigma * np.random.randn(3, 4) # mean & sigma
    ndarray_info(a, "a", True)

if True:
    # - random.randint(low, high=None, size=None, dtype=int)
    # ; return random integers from the "discrete uniform" distribution of
    #   the specified dtype in the "half-open" interval [low, high).
    #   if high is none (the default), then results are from [0, low)
    a = np.random.randint(2, size=10)
    ndarray_info(a, "a", True)
    a = np.random.randint(0, 10, size=(2, 4))
    ndarray_info(a, "a", True)
    # a =
    # [[7 3 7 1]
    #  [4 2 0 5]]

if False:
    pass
