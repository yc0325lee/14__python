#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# File : test_numpy.py
# Description : 
# Author : yc0325lee
# Created : 2021-06-19 20:33:06 by lee2103
# Modified : 2021-06-19 20:33:06 by lee2103
#
# o object of numpy.ndarray
#  - ndarray.ndim : the number of axes (dimensions)
#  - ndarray.shape :  the size of the array in each dimension, tuple of integers
#  - ndarray.size : the total number of elements
#  - ndarray.dtype : an object that describes the type of elements
#    -> print(x.dtype.name)
#  - ndarray.itemsize : the size in bytes of each element of the array
#  - ndarray.data : the size in bytes of each element of the array
# ----------------------------------------------------------------------------
import numpy as np
np.random.seed(20221209) # seed-ing

def ndarray_info(a, name="unknown", verbose=False):
    if isinstance(a, np.ndarray):
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

'''
# ndarray
x = np.array( [1.0, 2.0, 3.0])
y = np.array( [2.0, 4.0, 6.0])
print("x=", x.shape); print(x)
print("y=", y.shape); print(y)
print("")
print(x + y)
print(x - y)
print(x * y)
print(x / y)
'''

if False:
    # - numpy.set_printoptions(
    #       precision=None, threshold=None, edgeitems=None, linewidth=None,
    #       suppress=None, nanstr=None, infstr=None, formatter=None,
    #       sign=None, floatmode=None, *, legacy=None
    #   )
    # ; set printing options.
    # ; numpy.set_printoptions(precision=6, threshold=10, suppress=True)
    pass

if False:
    # array creation 
    print("\n1. conversion from other python structures (i.e. lists and tuples)")
    a1 = np.array([1, 2, 3, 4]); ndarray_info(a1, "a1")
    a2 = np.array([[1, 2], [3, 4]], dtype=np.int16); ndarray_info(a2, "a2")
    a3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=np.int8); ndarray_info(a3, "a3")

    print("\n2. intrinsic numpy array creation functions (e.g. arange, ones, zeros, etc.)")
    ndarray_info(np.arange(5), "np.arange(5)")
    ndarray_info(np.arange(10, dtype=np.float), "np.arange(10, dtype=np.float)")
    ndarray_info(np.arange(2, 3, 0.1, dtype=np.float32), "np.arange(2, 3, 0.1)")
    ndarray_info(np.linspace(1.0, 4.0, 6, dtype=np.float16), "np.linspace(1.0, 4.0, 6, dtype=np.float8)")
    ndarray_info(np.eye(5), "np.eye(5)") # identity matrix
    ndarray_info(np.eye(3, 5), "np.eye(3, 5)")
    ndarray_info(np.zeros((2, 3)), "np.zeros((2, 3))")
    ndarray_info(np.ones((2, 3, 4), dtype=np.float16), "np.ones((2, 3, 4))")

    rng = np.random.default_rng(seed=42) # generator(pcg64)
    ndarray_info(rng.random((2, 3)), "rng.random((2, 3))")
    ndarray_info(rng.random((2, 3, 4)), "rng.random((2, 3, 4))")
    
    print("\n3. replicating, joining, or mutating existing arrays")
    a = np.arange(5*5).reshape(5, 5)
    print("a=", a, sep='\n')
    b = a[:3, :3]
    print("b=", b, sep='\n')
    b *= 2 # modifies original array 'a'
    print("b=", b, sep='\n')
    print("a=", a, sep='\n')

    print()
    a = np.arange(5*5).reshape(5, 5)
    print("a=", a, sep='\n')
    b = a[:3, :3].copy() # copy()
    print("b=", b, sep='\n')
    b *= 2 # does not modify original array 'a'
    print("b=", b, sep='\n')
    print("a=", a, sep='\n')


if False:
    a = np.arange(10*10).reshape(10, 10)
    ndarray_info(a, "a")
    print("\n# slicing & striding")
    ndarray_info(a[2:8, 2:8], "a[2:8, 2:8]")
    ndarray_info(a[0:10:2, 0:10:2], "a[0:10:2, 0:10:2]")
    ndarray_info(a[1:10:2, 1:10:2], "a[1:10:2, 1:10:2]")

    print("\n# indexing with ndarray")
    b = a[np.array([0, 2, 4, 6, 8]), np.array([0, 2, 4, 6, 8])]
    ndarray_info(b, "a[np.array([0, 2, 4, 6, 8]), np.array([0, 2, 4, 6, 8])]")

if False:
    # 2x2 matrix
    A = np.array(
    [[1, 2],
     [3, 4]]
    )
    B = np.array(
    [[3, 0],
     [0, 6]]
    )
    
    print("A=", A.shape); print(A)
    print("B=", B.shape); print(B)
    
    print("\nA + B =")
    print( A + B )
    print("\nA * B =")
    print( A * B )
    print("\nA * 10 =")
    print( A * 10 ) # broadcasting happens
    
    C = np.array([10, 20])
    print("\nC=", C.shape); print(C)
    print("\nA * C =", A * C, sep="\n")
    
    X = np.array(
    [[99, 98, 97],
     [96, 95, 94],
     [93, 92, 91]]
    )
    print("\nX =")
    print(X)
    
    print("X[0] =", X[0])
    print("X[0][1] =", X[0][1])
    
    for row in X:
        for item in row:
            print(item)
    
    X = X.flatten()
    print("X.flatten() = ", X)
    print( X[np.array([0, 3, 6])] )
    
    print("X[X<97] = ", X[X<97])
    print("X[X%2==0] = ", X[X%2==0])



if False:
    # numpy.dot()
    # - if either a or b is 0-d (scalar), it is equivalent to multiply and using
    #   numpy.multiply(a, b) or a * b is preferred.
    # - if both a and b are 1-d arrays, it is inner product of vectors
    # - if both a and b are 2-d arrays, it is matrix multiplication
    # - if a is an n-d array and b is a 1-d array, it is a sum of product over the
    #   last axis of a and b.
    # - if a is an n-d array and b is an m-d array (where m>=2), it is a sum
    #   product over the last axis of a and the second-to-last axis of b

    print("# inner product for 1-d array")
    a = np.arange(0, 3) # [0, 1, 2]
    b = np.arange(3, 6) # [3, 4, 5]
    print("a=", a)
    print("b=", b)
    print("dot(a,b)=", np.dot(a, b), end='\n\n')
    # ------------
    # a= [0 1 2]
    # b= [3 4 5]
    # dot(a,b)= 14
    # ------------
    
    print("# matrix multiplication for 2-d array")
    a = np.arange(0, 4).reshape(2, 2)
    b = np.arange(4, 8).reshape(2, 2)
    print("a=", a, sep='\n')
    print("b=", b, sep='\n')
    print("dot(a,b)=", np.dot(a, b), sep='\n', end='\n\n')
    # -------------------
    # a= [[0 1]
    #     [2 3]]
    # b= [[4 5]
    #     [6 7]]
    # dot(a,b)= [[ 6  7]
    #            [26 31]]
    # -------------------
    
    print("# matrix multiplication for 2-d array")
    a = np.arange(0, 6).reshape(2, 3)
    b = np.arange(6, 12).reshape(3, 2)
    print("a=", a, sep='\n')
    print("b=", b, sep='\n')
    print("dot(a,b)=", np.dot(a, b), sep='\n', end='\n\n')
    # -----------------------------
    # [0 1 2] * [ 6  7] = [ 28  31]
    # [3 4 5]   [ 8  9]   [100 112]
    #           [10 11] 
    # -----------------------------
    
    print("# (2,) dot (2,3) -> (3,)")
    x = np.arange(1, 3) # (2,)
    w = np.arange(1, 7).reshape(2, 3) # (2, 3)
    print("x=", x, sep='\n')
    print("w=", w, sep='\n')
    print("dot(x, w)=", np.dot(x, w), end='\n\n') # (3,)
    # ---------------------
    # x= [1 2]
    # w= [[1 2 3]
    #     [4 5 6]]
    # dot(x, w)= [ 9 12 15]
    # ---------------------

    print("# (1,2) dot (2,3) -> (1,3)")
    x = np.arange(1, 3).reshape(1, 2) # (1, 2)
    w = np.arange(1, 7).reshape(2, 3) # (2, 3)
    print("x=", x, sep='\n')
    print("w=", w, sep='\n')
    print("dot(x, w)=", np.dot(x, w).shape); print(np.dot(x, w)) # ok!
    # -----------------------------------
    # x= [[1 2]] shape=(1,2)
    # w= [[1 2 3]
    #     [4 5 6]]
    # dot(x, w)= [[ 9 12 15]] shape=(1,3)
    # -----------------------------------

    print("# (2,3,4) dot (2,4,5) -> ?")
    a = np.arange(2*3*4).reshape(2, 3, 4)
    b = np.arange(2*4*5).reshape(2, 4, 5)
    print("a=", a, sep='\n')
    print("b=", b, sep='\n')
    print("dot(a, b)=", np.dot(a, b).shape); print(np.dot(a, b))
    # ------------------------------------------------------------------
    # if a is an n-d array and b is an m-d array (where m>=2), it is a sum
    # product over the last axis of a and the second-to-last axis of b.
    #
    # a= [[[ 0  1  2  3]
    #      [ 4  5  6  7]
    #      [ 8  9 10 11]]
    #    
    #     [[12 13 14 15]
    #      [16 17 18 19]
    #      [20 21 22 23]]] -> shape= (2, 3, 4)
    # 
    # b= [[[ 0  1  2  3  4]
    #      [ 5  6  7  8  9]
    #      [10 11 12 13 14]
    #      [15 16 17 18 19]]
    #    
    #     [[20 21 22 23 24]
    #      [25 26 27 28 29]
    #      [30 31 32 33 34]
    #      [35 36 37 38 39]]] -> shape= (2, 4, 5)
    #
    # dot(a, b)= [[[[  70   76   82   88   94]
    #               [ 190  196  202  208  214]]
    #            
    #              [[ 190  212  234  256  278]
    #               [ 630  652  674  696  718]]
    #            
    #              [[ 310  348  386  424  462]
    #               [1070 1108 1146 1184 1222]]]
    #            
    #            
    #             [[[ 430  484  538  592  646]
    #               [1510 1564 1618 1672 1726]]
    #            
    #              [[ 550  620  690  760  830]
    #               [1950 2020 2090 2160 2230]]
    #            
    #              [[ 670  756  842  928 1014]
    #               [2390 2476 2562 2648 2734]]]] -> shape= (2, 3, 2, 5)
    # ------------------------------------------------------------------

    # same as below!
    W = a.shape[0] # 2
    Z = a.shape[1] # 3
    Y = b.shape[0] # 2
    X = b.shape[2] # 5
    out = np.zeros((W, Z, Y, X), dtype=np.int) # shape=(2,3,2,5)
    for w in range(W):
        for z in range(Z):
            for y in range(Y):
                for x in range(X):
                    out[w][z][y][x] = np.dot(a[w,z,:], b[y,:,x])
                    # out[w][z][y][x] = sum(a[w,z,:] * b[y,:,x])

    print("dot(a, b)=", out); print(out.shape)
    # ------------------------------------------------------------------
    # dot(a, b)= [[[[  70   76   82   88   94]
    #               [ 190  196  202  208  214]]
    #            
    #              [[ 190  212  234  256  278]
    #               [ 630  652  674  696  718]]
    #            
    #              [[ 310  348  386  424  462]
    #               [1070 1108 1146 1184 1222]]]
    #            
    #            
    #             [[[ 430  484  538  592  646]
    #               [1510 1564 1618 1672 1726]]
    #            
    #              [[ 550  620  690  760  830]
    #               [1950 2020 2090 2160 2230]]
    #            
    #              [[ 670  756  842  928 1014]
    #               [2390 2476 2562 2648 2734]]]] -> shape= (2, 3, 2, 5)
    # ------------------------------------------------------------------


if False:
    # numpy.meshgrid()
    # ; return coordinate matrices from coordinate vectors.
    x = np.array([-2, -1, 0, 1, 2]); print(x)
    y = np.array([-2, -1, 0, 1, 2]); print(y)
    x, y = np.meshgrid(x, y)
    print("x=", x.shape); print(x)
    print("y=", y.shape); print(y)
    # ------------------
    # x= (5, 5)
    # [[-2 -1  0  1  2]
    #  [-2 -1  0  1  2]
    #  [-2 -1  0  1  2]
    #  [-2 -1  0  1  2]
    #  [-2 -1  0  1  2]]
    # y= (5, 5)
    # [[-2 -2 -2 -2 -2]
    #  [-1 -1 -1 -1 -1]
    #  [ 0  0  0  0  0]
    #  [ 1  1  1  1  1]
    #  [ 2  2  2  2  2]]
    # ------------------
    print("x=", x.flatten())
    print("y=", y.flatten())
    # x= [-2 -1  0  1  2 -2 -1  0  1  2 -2 -1  0  1  2 -2 -1  0  1  2 -2 -1  0  1  2]
    # y= [-2 -2 -2 -2 -2 -1 -1 -1 -1 -1  0  0  0  0  0  1  1  1  1  1  2  2  2  2  2]


if False:
    # random.choice(a, size=None, replace=True, p=None)
    sample = np.random.choice(100, 10)
    ndarray_info(sample, "sample")

    a = np.arange(100)
    sample = np.random.choice(a, 10)
    ndarray_info(sample, "sample")

    sample = np.random.choice(5, 10, p=[0.1, 0, 0.3, 0.6, 0]) # p : probability
    ndarray_info(sample, "sample")
    
    # random
    rng = np.random.default_rng(seed=42) # Generator(PCG64)
    a = rng.random((10, ))
    ndarray_info(a, "a")

    a = 0.1 * np.random.randn(3, 4)
    ndarray_info(a, "a")

    mean = 1.0
    sigma = 0.01
    a = mean + sigma * np.random.randn(2, 3, 4) # mean & sigma
    ndarray_info(a, "a")


if False:
    # iterating over arrays using numpy.nditer()
    a = np.arange(6).reshape(2, 3)
    print("a=", a, sep="\n")
    for item in np.nditer(a):
        print("item=", item)
    print()

    print("a.transpose()=", a.transpose(), sep="\n") # a.T == a.transpose()
    for item in np.nditer(a.transpose()):
        print("item=", item)
    print()
    
    print("a.transpose().copy()=", a.transpose().copy(), sep="\n") # a.T == a.transpose()
    for item in np.nditer(a.transpose().copy()):
        print("item=", item)
    print()
    
    # modifying array values - x
    a = np.arange(6).reshape(2, 3)
    print("a(before)=", a, sep="\n")
    print()
    for item in np.nditer(a):
        item = item + 1
    print("a(after)=", a, sep="\n") # not modified
    print()
    
    # to modify values in array
    with np.nditer(a, op_flags=['readwrite']) as it:
        for item in it:
            item += 1
    # write-back will happen here!
    print("a(modified)=", a, sep="\n") # modified!
    
    with np.nditer(a, flags=['multi_index'], op_flags=['readwrite']) as it:
        while not it.finished:
            print("it.multi_index=", it.multi_index) # tuple
            print("it=", it) # nditer object
            print("it[0]=", it[0]) # value of this element
            it.iternext()


if False:
    a = np.random.randn(3, 4)
    print("a=", a, sep="\n")
    mask = a <= 0;
    print("mask=", mask, sep="\n")
    out = a.copy()
    print("out=", out, sep="\n")
    out[mask] = 0
    print("out=", out, sep="\n")

if False:
    # padding numpy.ndarray
    # numpy.pad(array, pad_width, mode='constant', **kwargs)
    a = np.arange(7*7).reshape(7, 7) # shape= (2, 2)
    print("a(before)=", a.shape, a, sep="\n")
    #padded = np.pad(a, (2, 2), mode='constant', constant_values=((-1, -1), (-2, -2)))
    #padded = np.pad(a, (2, 2), mode='constant') # default=0
    padded = np.pad(a, (2, 2), mode='reflect')
    print("padded(before)=", padded.shape, padded, sep="\n")

if False:
    # numpy's ellipsis
    # ; expands to the number of : objects needed for the selection tuple to index all dimensions.
    a = np.arange(3*3).reshape(3, 3)
    ndarray_info(a, "np.arange(3*3).reshape(3, 3)")

    print("a[0]=", a[0], sep="\n")
    print("a[1:]=", a[1:], sep="\n")

    print("a[...]=", a[...], sep="\n")
    print("a[1:,...]=", a[1:,...], sep="\n")

if False:
    "numpy.array_equal(a1, a2, equal_nan=False)"
    a1 = np.arange(2*3).reshape(2, 3)
    a2 = np.arange(2*3).reshape(2, 3)
    print("a1=", a1.shape, a1, sep="\n")
    print("a2=", a2.shape, a2, sep="\n")
    print("result=", np.array_equal(a1, a2))
    a2[1,1] = 9
    print("a2=", a2.shape, a2, sep="\n")
    print("result=", np.array_equal(a1, a2))
    a2[1][1] = 8
    print("a2=", a2.shape, a2, sep="\n")

if False:
    # -----------------------------------
    # label-to-onehot
    # 3 -> [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    # -----------------------------------
    labels = np.arange(10);
    ndarray_info(labels, "labels", verbose=True)

    onehots = np.zeros((labels.size, 10), dtype=np.int32)
    ndarray_info(onehots, "onehots", verbose=True)
    for i, row in enumerate(onehots):
        row[labels[i]] = 1

    ndarray_info(onehots, "onehots", verbose=True)
    # ---------------------------------
    #  labels = [0 1 2 3 4 5 6 7 8 9]
    #  onehots =
    #           [[1 0 0 0 0 0 0 0 0 0]
    #            [0 1 0 0 0 0 0 0 0 0]
    #            [0 0 1 0 0 0 0 0 0 0]
    #            [0 0 0 1 0 0 0 0 0 0]
    #            [0 0 0 0 1 0 0 0 0 0]
    #            [0 0 0 0 0 1 0 0 0 0]
    #            [0 0 0 0 0 0 1 0 0 0]
    #            [0 0 0 0 0 0 0 1 0 0]
    #            [0 0 0 0 0 0 0 0 1 0]
    #            [0 0 0 0 0 0 0 0 0 1]]
    # ---------------------------------

if False:
    a = np.arange(3*4).reshape(3, 4)
    mask = a < 5
    a[mask] = 0

    ndarray_info(a, "a", True)
    ndarray_info(mask, "mask", True)
    ndarray_info(a, "a", True)

    # -----------------------------
    # a =
    #   [[ 0  1  2  3]
    #    [ 4  5  6  7]
    #    [ 8  9 10 11]]
    # 
    # mask = a < 5
    #   [[ True  True  True  True]
    #    [ True False False False]
    #    [False False False False]]
    # a =
    #   [[ 0  0  0  0]
    #    [ 0  5  6  7]
    #    [ 8  9 10 11]]
    # -----------------------------

if False:
    X_W = np.arange(4*3).reshape(4, 3)
    ndarray_info(X_W, "X_W", True)
    B = np.arange(3).reshape(3)
    ndarray_info(B, "B", True)
    B = np.array([
        [0, 1, 2],
        [0, 1, 2],
        [0, 1, 2],
        [0, 1, 2],
    ])
    ndarray_info(B, "B", True)

    Y = X_W + B
    ndarray_info(Y, "Y", True)

if False:
    # numpy.sum()
    a = np.arange(4*3).reshape(4, 3)
    ndarray_info(a, "a", True)
    ndarray_info(np.sum(a, axis=0), "numpy.sum(a, axis=0)", True)
    ndarray_info(np.sum(a, axis=1), "numpy.sum(a, axis=1)", True)
    # a =
    #   [[ 0  1  2]
    #    [ 3  4  5]
    #    [ 6  7  8]
    #    [ 9 10 11]]
    #
    # numpy.sum(a, axis=0) = [18 22 26], shape=(3,)
    #
    # a =
    #   [[ 0  1  2]
    #    [ 3  4  5]
    #    [ 6  7  8]
    #    [ 9 10 11]]
    #
    # numpy.sum(a, axis=1) = [ 3 12 21 30], shape=(4,)

if False:
    # - numpy.histogram(
    #       a, bins=10, range=None, normed=None, weights=None, density=None
    #   )
    # ; compute the histogram of a dataset.
    a = 4 + np.random.normal(0, 1.5, 1000)
    hist, bin_edges = np.histogram(a, bins=10)
    print('hist=', hist, 'len=', len(hist))
    print('bin_edges=', bin_edges, 'len=', len(bin_edges))
    # hist= [  6  40  90 166 227 239 130  71  27   4] len= 10
    # bin_edges= [-0.40987463  0.50607884  1.42203232  2.3379858   3.25393927  4.16989275
    #   5.08584623  6.0017997   6.91775318  7.83370666  8.74966013] len= 11

if False:
    # - random.shuffle(x)
    # ; modify a sequence in-place by shuffling its contents.
    # ; returns None
    a = np.arange(12)
    np.random.shuffle(a)
    a = a.reshape(3, 4)
    ndarray_info(a, "a", True)

if False:
    # - numpy.argmax(a, axis=None, out=None, *, keepdims=<no value>)
    # ; returns the indices of the maximum values along an axis.

    # random.choice(a, size=None, replace=True, p=None)
    a = np.random.choice(100, 10)
    ndarray_info(a, "a", True)
    print('np.argmax(a)=', np.argmax(a))
    # a = [36 36 72 76  5 96 60 85 26 16]
    # np.argmax(a)= 5

    a = np.arange(12)
    np.random.shuffle(a)
    a = a.reshape(3, 4)
    ndarray_info(a, "a", True)
    # [[11  2  5 10]
    #  [ 3  0  6  9]
    #  [ 7  8  1  4]]

    print('np.argmax(a)=', np.argmax(a))
    print('np.argmax(a, axis=0)=', np.argmax(a, axis=0))
    print('np.argmax(a, axis=1)=', np.argmax(a, axis=1))
    # np.argmax(a)= 0
    # np.argmax(a, axis=0)= [0 2 1 0]
    # np.argmax(a, axis=1)= [0 3 1]

if False:
    # - numpy.amin(
    #       a, axis=None, out=None, keepdims=<no value>, initial=<no value>,
    #       where=<no value>
    #   )
    # ; return the minimum of an array or minimum along an axis.
    #
    # - numpy.amax(
    #       a, axis=None, out=None, keepdims=<no value>, initial=<no value>,
    #       where=<no value>
    #   )
    # ; return the maximum of an array or maximum along an axis.
    a = np.random.randint(0, 100, size=(4, 5))
    ndarray_info(a, "a", True)
    # a =
    # [[36 36 72 76  5]
    #  [96 60 85 26 16]
    #  [33  8  7 31 62]
    #  [88 13 88  0 80]]
    print('np.amin(a)=', np.amin(a))
    print('np.amax(a)=', np.amax(a))

    ndarray_info(np.amin(a, axis=0), 'np.amin(a, axis=0)', True)
    ndarray_info(np.amin(a, axis=1), 'np.amin(a, axis=1)', True)
    # np.amin(a, axis=0) = [33  8  7  0  5]
    # np.amin(a, axis=1) = [ 5 16  7  0]

    ndarray_info(np.amax(a, axis=0), 'np.amax(a, axis=0)', True)
    ndarray_info(np.amax(a, axis=1), 'np.amax(a, axis=1)', True)
    # np.amax(a, axis=0) = [96 60 88 76 80]
    # np.amax(a, axis=1) = [76 96 62 88]

if False:
    # - numpy.c_ = <numpy.lib.index_tricks.CClass object>
    # ; translates slice objects to concatenation along the second axis.
    pass

if False:
    # - numpy.concatenate(
    #       (a1, a2, ...), axis=0, out=None, dtype=None, casting="same_kind"
    #   )
    # ; join a sequence of arrays along an existing axis.

    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6]])
    np.concatenate((a, b), axis=0)
    # array([[1, 2],
    #        [3, 4],
    #        [5, 6]])
    np.concatenate((a, b.T), axis=1)
    # array([[1, 2, 5],
    #        [3, 4, 6]])
    np.concatenate((a, b), axis=None)
    # array([1, 2, 3, 4, 5, 6])

if False:
    pass
