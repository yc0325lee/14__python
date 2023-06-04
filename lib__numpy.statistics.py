#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__numpy.statistics.py
# - author : yc0325lee
# - created : 2023-01-09 22:14:49 by yc032
# - modified : 2023-01-09 22:14:49 by yc032
# - description : 
# ----------------------------------------------------------------------------

# -------------------------------------
# averages and variances
#
# - median(a[, axis, out, overwrite_input, keepdims])
#     Compute the median along the specified axis.
# - average(a[, axis, weights, returned, keepdims])
#     Compute the weighted average along the specified axis.
# - mean(a[, axis, dtype, out, keepdims, where])
#     Compute the arithmetic mean along the specified axis.
# - std(a[, axis, dtype, out, ddof, keepdims, where])
#     Compute the standard deviation along the specified axis.
# - var(a[, axis, dtype, out, ddof, keepdims, where])
#     Compute the variance along the specified axis.
# - nanmedian(a[, axis, out, overwrite_input, ...])
#     Compute the median along the specified axis, while ignoring NaNs.
# - nanmean(a[, axis, dtype, out, keepdims, where])
#     Compute the arithmetic mean along the specified axis, ignoring NaNs.
# - nanstd(a[, axis, dtype, out, ddof, ...])
#     Compute the standard deviation along the specified axis, while ignoring NaNs.
# - nanvar(a[, axis, dtype, out, ddof, ...])
#     Compute the variance along the specified axis, while ignoring NaNs.
