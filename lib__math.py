# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# File : lib__math.py
# Author : yc0325lee
# Created : 2022-03-20 14:44:55 by lee2103
# Modified : 2022-03-20 14:44:55 by lee2103
# Description : 
# References
# - https://docs.python.org/3/library/math.html
# ----------------------------------------------------------------------------
import math

if False:
    # - math.hypot(*coordinates)
    # ; return the euclidean norm, sqrt(sum(x**2 for x in coordinates))
    coords = [3.0, 4.0, 5.0]
    print("math.hypot(coords)=", math.hypot(*coords))
    print('sqrt(sum(x**2 for x in coords))=', math.sqrt(sum(x**2 for x in coords)))
    # math.hypot(coords)= 7.0710678118654755
    # sqrt(sum(x**2 for x in coords))= 7.0710678118654755


if True:
    print('math.pi  =', math.pi )
    print('math.e   =', math.e  )
    print('math.tau =', math.tau)
    print('math.inf =', math.inf)
    print('math.nan =', math.nan)
    # math.pi  = 3.141592653589793
    # math.e   = 2.718281828459045
    # math.tau = 6.283185307179586
    # math.inf = inf
    # math.nan = nan
