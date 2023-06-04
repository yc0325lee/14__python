#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__types.py
# - author : yc0325lee
# - created : 2023-05-14 17:32:04 by yc032
# - modified : 2023-05-14 17:32:04 by yc032
# - description : 
# ----------------------------------------------------------------------------


if False:
    # -------------------------------------
    # - types — dynamic type creation and names for built-in types
    pass


if False:
    # -------------------------------------
    # - class types.MappingProxyType(mapping)
    # ; read-only proxy of a mapping. it provides a dynamic view on the
    #   mapping's entries, which means that when the mapping changes, the view
    #   reflects these changes.
    import types
    import pprint

    lookup = {
        'dwzca': 50, 'cwjxm': 91, 'iexon': 75, 'ymnae': 57, 'gisnx': 36,
        'bsyrc': 34, 'swqid': 57, 'uqubh': 78, 'pfsxn': 30, 'spiea': 98
    }
    print("lookup=")
    pprint.pprint(lookup)
    # lookup=
    # {'bsyrc': 34, 'cwjxm': 91, 'dwzca': 50, 'gisnx': 36, 'iexon': 75,
    #  'pfsxn': 30, 'spiea': 98, 'swqid': 57, 'uqubh': 78, 'ymnae': 57}

    proxy = types.MappingProxyType(lookup)
    print("proxy=")
    pprint.pprint(proxy)
    # proxy=
    # mappingproxy({'bsyrc': 34, 'cwjxm': 91, 'dwzca': 50, 'gisnx': 36, 'iexon': 75,
    #               'pfsxn': 30, 'spiea': 98, 'swqid': 57, 'uqubh': 78, 'ymnae': 57})

    lookup['xxxxx'] = 99
    pprint.pprint(proxy)
    # mappingproxy({'bsyrc': 34, 'cwjxm': 91, 'dwzca': 50, 'gisnx': 36, 'iexon': 75,
    #               'pfsxn': 30, 'spiea': 98, 'swqid': 57, 'uqubh': 78, 'xxxxx': 99,
    #               'ymnae': 57})

    proxy['yyyyy'] = 99
    # TypeError: 'mappingproxy' object does not support item assignment
