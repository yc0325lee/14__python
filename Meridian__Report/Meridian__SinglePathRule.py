# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Meridian__SinglePathRule.py
# - title : 
# - created : 20221025_000726
# - description
# ----------------------------------------------------------------------------
from Meridian__RuleBase import Meridian__RuleBase

class Meridian__SinglePathRule(Meridian__RuleBase):
    'Meridian__SinglePathRule class implementation'
    debug = False
    count = 0

    attributes = None
    maxlen = dict()

    @classmethod
    def init_class_data(cls):
        for attr in __class__.attributes:
            __class__.maxlen[attr] = len(attr)
        
    def __init__(self, chunk):
        super().__init__(chunk)
        for attr in __class__.attributes:
            self._data[attr] = chunk[attr]
            for i in enumerate(self._data[attr]):
                if len(self._data[attr][i]) > __class__.maxlen[attr]:
                    self.maxlen[attr] = len(self._data[attr][i])
        __class__.count += 1
        pass

    def write(self):
        # under construction
        pass

    pass
