#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : NotImplemented_vs_NotImplementedError.py
# - author : yc0325lee
# - created : 2022-11-27 00:37:20 by yc032
# - modified : 2022-11-27 00:37:20 by yc032
# - description : 
# ----------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# - NotImplemented
# ; A special value which should be returned by the binary special methods
#   (e.g. __eq__(), __lt__(), __add__(), __rsub__(), etc.) to indicate that the
#   operation is not implemented with respect to the other type; may be returned
#   by the in-place binary special methods (e.g. __imul__(), __iand__(), etc.)
#   for the same purpose. It should not be evaluated in a boolean context.
#   NotImplemented is the sole instance of the types.NotImplementedType type.


# ------------------------------------------------------------------------------
# - NotImplementedError
# ; exception NotImplementedError
# ; This exception is derived from RuntimeError. In user defined base classes,
#   abstract methods should raise this exception when they require derived
#   classes to override the method, or while the class is being developed to
#   indicate that the real implementation still needs to be added.
