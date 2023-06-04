#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__dataclasses.py
# - author : yc0325lee
# - created : 2023-05-28 23:38:37 by yc032
# - modified : 2023-05-28 23:38:37 by yc032
# - description : 
# ----------------------------------------------------------------------------
import os, os.path, sys
import pprint
import argparse
import random
import re

import dataclasses

if False:
    # -------------------------------------
    # - dataclasses
    # ; this module provides a decorator and functions for automatically
    #   adding generated special methods such as __init__() and __repr__() to
    #   user-defined classes. it was originally described in pep 557.
    #
    # - @dataclasses.dataclass(
    #       *, init=True, repr=True, eq=True, order=False, unsafe_hash=False,
    #       frozen=False, match_args=True, kw_only=False, slots=False,
    #       weakref_slot=False
    #   )
    # ; this function is a decorator that is used to add generated special
    #   methods to classes
    # ; keyword-argument only! <--- '*'
    # ; eq=True & frozen=True -> __hash__, hashable
    pass
