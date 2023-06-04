#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : data__user_defined_dict.py
# - author : yc0325lee
# - created : 2023-05-11 22:50:39 by yc032
# - modified : 2023-05-11 22:50:39 by yc032
# - description : 
# ----------------------------------------------------------------------------
import os, os.path, sys
import collections
import collections.abc


def _upper(x):
    try:
        return x.upper()
    except AttributeError:
        return x

class DictSub(dict):
    def __missing__(self, key):
        return self[_upper(key)]


class UserDictSub(UserDict):
    def __missing__(self, key):
        return self[_upper(key)]


class SimpleMappingSub(abc.Mapping):
    def __init__(self, *args, **kwargs):
        self._data = dict(*args, **kwargs)

    # next three methods: abstract in ABC
    def __getitem__(self, key):
        return self._data[key]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    # never called by instances of this class
    def __missing__(self, key):
        return self[_upper(key)]


class MappingMissingSub(SimpleMappingSub):
    def __getitem__(self, key):
        try:
            return self._data[key]
        except KeyError:
            return self[_upper(key)]


class DictLikeMappingSub(SimpleMappingSub):
    def __getitem__(self, key):
        try:
            return self._data[key]
        except KeyError:
            return self[_upper(key)]

    def get(self, key, default=None):
        return self._data.get(key, default)

    def __contains__(self, key):
        return key in self._data


if __name__ == '__main__':

    if False:
        d = DictSub(A = 'letter A')
        d['a']
        d.get('a', '')
        'a' in d
        pass
