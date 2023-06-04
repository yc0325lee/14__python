# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Meridian__Report.py
# - author : yc0325lee
# - created : 2022-10-23 23:02:40 by lee2103
# - modified : 2022-10-23 23:02:40 by lee2103
# - description :
# ----------------------------------------------------------------------------
import re

from Meridian__CNTL           import Meridian__CNTL
from Meridian__DATA           import Meridian__DATA
from Meridian__INTERFACE      import Meridian__INTERFACE
from Meridian__U_INTERFACE    import Meridian__U_INTERFACE
from Meridian__W_CNTL         import Meridian__W_CNTL
from Meridian__W_DATA         import Meridian__W_DATA
from Meridian__W_GLITCH       import Meridian__W_GLITCH
from Meridian__W_INTERFACE    import Meridian__W_INTERFACE
from Meridian__W_RECON_GROUPS import Meridian__W_RECON_GROUPS

class Meridian__Report:
    'Meridian__Report class implementation'
    Debug = False
    Count = 0
    regex__rule = None

    def __init__(self):
        super().__init__()
        self.fields = ['RuleName', 'TxFlop', 'RxFlop', 'ClockDomains', 'Info']
        for field in fields:
            self.attr[field] = None # attr[key] = val(str)
            self.maxlen[field] = 0 # maxlen[key] = len(attr[key])
        __class__.Count += 1
        pass

    @classmethod
    def initialize_class_data():
        pass

    attrName = list()
    def __swallow_line(chunk, attrName, attrValue):
        pass

    def read_report(self, inFileName):
        print("[info] reading {} ...".format(inFileName), file=sys.stderr)
        with open(inFileName, "r", encoding="utf8") as inFile:
            for lineno, line in enumerate(inFile, 1):
                if line.startswith('RuleName'):
                    nonlocal attrName
                    attrName = re.split('\s+', line)
                else if re.
                print(lineno + ": " + line, end="")
        pass


    def parse(self, chunk):
        pass

    def write(self):
        # under construction
        pass

    pass


