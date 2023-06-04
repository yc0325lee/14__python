#!/usr/bin/env python
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : 01_20_combining_multiple_mappings_into_a_single_mapping.py
# - author : yc0325lee
# - created : 2022-11-16 00:06:50 by yc032
# - modified : 2022-11-16 00:06:50 by yc032
# - description : 
# ----------------------------------------------------------------------------

if False:
    # - class collections.ChainMap(*maps)
    # ; a ChainMap groups multiple dicts or other mappings together to create
    #   a single, updateable view.
    # ; if there are duplicate keys, the values from the first mapping get used
    # ; operations that mutate the mapping always affect the first mapping listed
    import collections

    a = {'x':1, 'z':3}
    b = {'y':2, 'z':4}
    combined = collections.ChainMap(a, b)
    print("combined['x'] =", combined['x']) # 1
    print("combined['y'] =", combined['y']) # 2
    print("combined['z'] =", combined['z']) # 3

    b['w'] = 5 # 'combined' will be updated also!
    print("combined['w'] =", combined['w'])

    #del combined['y']
    # KeyError: "Key not found in the first mapping: 'y'"


if False:
    # - using built-in dict.update() method
    # ; same as above, but this is not an updateable view
    # ; if any of the original dictionaries mutate, the changes don’t get
    #   reflected in the merged dictionary.
    a = {'x':1, 'z':3}
    b = {'y':2, 'z':4}

    merged = dict(b)
    merged.update(a) # a has higher priority

    print('merged =', merged)


if True:
    # - using ChainMap.new_child() and ChainMap.parents
    # - new_child(m=None, **kwargs)
    # ; returns a new chainmap containing a new map followed by all of the
    #   maps in the current instance.
    # - parents
    # ; property returning a new chainmap containing all of the maps in the
    #   current instance except the first one.
    import collections
    values = collections.ChainMap()

    values['a'] = 0
    values['b'] = 1
    values['c'] = 2
    print('values =', values)
    # values = ChainMap({'a': 0, 'b': 1, 'c': 2})

    values = values.new_child()
    print('values =', values)
    values['a'] = 3
    print('values =', values)
    # values = ChainMap({}, {'a': 0, 'b': 1, 'c': 2})
    # values = ChainMap({'a': 3}, {'a': 0, 'b': 1, 'c': 2})

    values = values.new_child()
    print('values =', values)
    values['a'] = 4
    print('values =', values)
    # values = ChainMap({}, {'a': 3}, {'a': 0, 'b': 1, 'c': 2})
    # values = ChainMap({'a': 4}, {'a': 3}, {'a': 0, 'b': 1, 'c': 2})

    values = values.parents
    print('values =', values)
    # values = ChainMap({'a': 3}, {'a': 0, 'b': 1, 'c': 2})

    values = values.parents
    print('values =', values)
    # values = ChainMap({'a': 0, 'b': 1, 'c': 2})

    values = values.parents
    print('values =', values)
    # values = ChainMap({})
