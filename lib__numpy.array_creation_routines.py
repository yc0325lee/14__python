#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__numpy.array_creation_routines.py
# - author : yc0325lee
# - created : 2022-12-19 18:39:53 by yc032
# - modified : 2022-12-19 18:39:53 by yc032
# - description : 
# ----------------------------------------------------------------------------
import numpy as np

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

if False:
    # - numpy.zeros(shape, dtype=float64, order='C', *, like=None)
    # ; return a new array of given shape and type, filled with zeros.
    ndarray_info( np.zeros((2, 3), dtype=np.int64), "np.zeros((2, 3), dtype=np.int64)", True )
    ndarray_info( np.zeros((2, 3), dtype=np.float64), "np.zeros((2, 3), dtype=np.float16)", True )
    # ------------------------------------------------
    # ndarray_info(np.zeros((2, 3), dtype=np.int64))
    # ndim= 2
    # shape= (2, 3)
    # size= 6
    # dtype.name= int64
    # itemsize= 8
    # data= <memory at 0x000001EDB4B2C790>
    # np.zeros((2, 3), dtype=np.int64) =
    # [[0 0 0]
    #  [0 0 0]]
    #
    # ndarray_info(np.zeros((2, 3), dtype=np.float16))
    # ndim= 2
    # shape= (2, 3)
    # size= 6
    # dtype.name= float64
    # itemsize= 8
    # data= <memory at 0x000001EDB4B2C790>
    # np.zeros((2, 3), dtype=np.float16) =
    # [[0. 0. 0.]
    #  [0. 0. 0.]]
    # ------------------------------------------------

if False:
    # - numpy.zeros_like(
    #       a, dtype=None, order='K', subok=True, shape=None
    #   )
    # ; return an array of zeros with the same shape and type as a given array.
    a = np.random.rand(3, 4)
    a = np.arange(12, dtype=np.int64).reshape(3, 4)
    ndarray_info(a, "a", True)

    zeros = np.zeros_like(a, dtype=np.float64)
    ndarray_info(zeros, "zeros", True)
    # ------------------------------------------
    # ndarray_info(a)      # ndarray_info(zeros)
    # ndim= 2              # ndim= 2            
    # shape= (3, 4)        # shape= (3, 4)      
    # size= 12             # size= 12           
    # dtype.name= int64    # dtype.name= float64
    # itemsize= 8          # itemsize= 8        
    # a =                  # zeros =            
    # [[ 0  1  2  3]       # [[0. 0. 0. 0.]     
    #  [ 4  5  6  7]       #  [0. 0. 0. 0.]     
    #  [ 8  9 10 11]]      #  [0. 0. 0. 0.]]    
    # ------------------------------------------
