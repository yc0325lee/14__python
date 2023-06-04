#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__scipy_sparse.py
# - author : yc0325lee
# - created : 2022-12-24 21:14:06 by yc032
# - modified : 2022-12-24 21:14:06 by yc032
# - description : 
# ----------------------------------------------------------------------------
import os, os.path, sys
import random
import numpy as np
import sklearn
import scipy
#from scipy.sparse import csr_matrix
np.random.seed(42)
import pandas as pd

def dump_scr_matrix(m, name='unknown', verbose=False):
    if isinstance(m, scipy.sparse.csr_matrix):
        print("# csr_matrix({})".format(name))
        print("  dtype.name=", m.dtype.name)
        print("  shape=", m.shape)
        print("  ndim=", m.ndim)
        print("  nnz=", m.nnz)
        if verbose:
            print("  data=", m.data)
            print("  indices=", m.indices)
            print("  {} =".format(name))
            print(m, end='\n\n')
    else:
        print("[err ] type({}) is not csr_matrix!".format(name))


if True:
    # - class scipy.sparse.csr_matrix(
    #       arg1, shape=None, dtype=None, copy=False
    #   )
    # ; compressed sparse row matrix
    # ; attributes
    #   dtype shape ndim nnz data indices indptr has_sorted_indices
    row = np.array([0, 0, 1, 2, 2, 2])
    col = np.array([0, 2, 2, 0, 1, 2])
    data = np.array([1, 2, 3, 4, 5, 6])
    matrix = scipy.sparse.csr_matrix((data, (row, col)), shape=(3, 3))
    print('type(matrix)=', type(matrix))
    print('matrix=', matrix)
    # type(matrix)= <class 'scipy.sparse._csr.csr_matrix'>
    # matrix=   (0, 0)        1
    #   (0, 2)        2
    #   (1, 2)        3
    #   (2, 0)        4
    #   (2, 1)        5
    #   (2, 2)        6

    dump_scr_matrix(matrix, 'matrix', True)
    # csr_matrix(matrix)
    # dtype.name= int32
    # shape= (3, 3)
    # ndim= 2
    # nnz= 6
    # data= [1 2 3 4 5 6]
    # indices= [0 2 2 0 1 2]
    # matrix =
    # (0, 0)        1
    # (0, 2)        2
    # (1, 2)        3
    # (2, 0)        4
    # (2, 1)        5
    # (2, 2)        6

    print('matrix.toarray()=')
    print(matrix.toarray())
    # matrix.toarray()=
    # [[1 0 2]
    #  [0 0 3]
    #  [4 5 6]]

    print('\nmatrix.todense()=')
    print(matrix.todense())
    # matrix.todense()=
    # [[1 0 2]
    #  [0 0 3]
    #  [4 5 6]]
