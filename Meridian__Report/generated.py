# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Meridian__Common.py
# - title : 
# - created : 20221023_222108
# - description
# ----------------------------------------------------------------------------
class Meridian__Common:
    'Meridian__Common class implementation'
    Debug = False
    Count = 0

    def __init__(self):
        super().__init__()
        self.fields = ['']
        for field in fields:
            self.attr[field] = None # attr[key] = val(str)
            self.maxlen[field] = 0 # maxlen[key] = len(attr[key])
        __class__.Count += 1
        pass

    def parse(self, chunk):
        pass

    def write(self):
        # under construction
        pass

    pass

# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Meridian__RuleBase.py
# - title : 
# - created : 20221023_222108
# - description
# ----------------------------------------------------------------------------
class Meridian__RuleBase(Meridian__Common):
    'Meridian__RuleBase class implementation'
    Debug = False
    Count = 0

    def __init__(self):
        super().__init__()
        self.fields = ['']
        for field in fields:
            self.attr[field] = None # attr[key] = val(str)
            self.maxlen[field] = 0 # maxlen[key] = len(attr[key])
        __class__.Count += 1
        pass

    def parse(self, chunk):
        pass

    def write(self):
        # under construction
        pass

    pass

# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Meridian__SinglePathRule.py
# - title : 
# - created : 20221023_222108
# - description
# ----------------------------------------------------------------------------
class Meridian__SinglePathRule(Meridian__RuleBase):
    'Meridian__SinglePathRule class implementation'
    Debug = False
    Count = 0

    def __init__(self):
        super().__init__()
        self.fields = ['']
        for field in fields:
            self.attr[field] = None # attr[key] = val(str)
            self.maxlen[field] = 0 # maxlen[key] = len(attr[key])
        __class__.Count += 1
        pass

    def parse(self, chunk):
        pass

    def write(self):
        # under construction
        pass

    pass

# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Meridian__CNTL.py
# - title : 
# - created : 20221023_222108
# - description
# ----------------------------------------------------------------------------
class Meridian__CNTL(Meridian__SinglePathRule):
    'Meridian__CNTL class implementation'
    Debug = False
    Count = 0

    def __init__(self):
        super().__init__()
        self.fields = ['RuleName', 'TxFlop', 'RxFlop', 'ClockDomains', 'Info']
        for field in fields:
            self.attr[field] = None # attr[key] = val(str)
            self.maxlen[field] = 0 # maxlen[key] = len(attr[key])
        __class__.Count += 1
        pass

    def parse(self, chunk):
        pass

    def write(self):
        # under construction
        pass

    pass

# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Meridian__DATA.py
# - title : 
# - created : 20221023_222108
# - description
# ----------------------------------------------------------------------------
class Meridian__DATA(Meridian__SinglePathRule):
    'Meridian__DATA class implementation'
    Debug = False
    Count = 0

    def __init__(self):
        super().__init__()
        self.fields = ['RuleName', 'TxFlop', 'RxFlop', 'ClockDomains', 'Info']
        for field in fields:
            self.attr[field] = None # attr[key] = val(str)
            self.maxlen[field] = 0 # maxlen[key] = len(attr[key])
        __class__.Count += 1
        pass

    def parse(self, chunk):
        pass

    def write(self):
        # under construction
        pass

    pass

# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Meridian__W_CNTL.py
# - title : 
# - created : 20221023_222108
# - description
# ----------------------------------------------------------------------------
class Meridian__W_CNTL(Meridian__SinglePathRule):
    'Meridian__W_CNTL class implementation'
    Debug = False
    Count = 0

    def __init__(self):
        super().__init__()
        self.fields = ['RuleName', 'TxFlop', 'RxFlop', 'ClockDomains', 'Info']
        for field in fields:
            self.attr[field] = None # attr[key] = val(str)
            self.maxlen[field] = 0 # maxlen[key] = len(attr[key])
        __class__.Count += 1
        pass

    def parse(self, chunk):
        pass

    def write(self):
        # under construction
        pass

    pass

# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Meridian__W_DATA.py
# - title : 
# - created : 20221023_222108
# - description
# ----------------------------------------------------------------------------
class Meridian__W_DATA(Meridian__SinglePathRule):
    'Meridian__W_DATA class implementation'
    Debug = False
    Count = 0

    def __init__(self):
        super().__init__()
        self.fields = ['RuleName', 'TxFlop', 'RxFlop', 'ClockDomains', 'Info']
        for field in fields:
            self.attr[field] = None # attr[key] = val(str)
            self.maxlen[field] = 0 # maxlen[key] = len(attr[key])
        __class__.Count += 1
        pass

    def parse(self, chunk):
        pass

    def write(self):
        # under construction
        pass

    pass

# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Meridian__MultiPathRule.py
# - title : 
# - created : 20221023_222108
# - description
# ----------------------------------------------------------------------------
class Meridian__MultiPathRule(Meridian__RuleBase):
    'Meridian__MultiPathRule class implementation'
    Debug = False
    Count = 0

    def __init__(self):
        super().__init__()
        self.fields = ['']
        for field in fields:
            self.attr[field] = None # attr[key] = val(str)
            self.maxlen[field] = 0 # maxlen[key] = len(attr[key])
        __class__.Count += 1
        pass

    def parse(self, chunk):
        pass

    def write(self):
        # under construction
        pass

    pass

# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Meridian__InterfaceBase.py
# - title : 
# - created : 20221023_222108
# - description
# ----------------------------------------------------------------------------
class Meridian__InterfaceBase(Meridian__MultiPathRule):
    'Meridian__InterfaceBase class implementation'
    Debug = False
    Count = 0

    def __init__(self):
        super().__init__()
        self.fields = ['']
        for field in fields:
            self.attr[field] = None # attr[key] = val(str)
            self.maxlen[field] = 0 # maxlen[key] = len(attr[key])
        __class__.Count += 1
        pass

    def parse(self, chunk):
        pass

    def write(self):
        # under construction
        pass

    pass

# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Meridian__INTERFACE.py
# - title : 
# - created : 20221023_222108
# - description
# ----------------------------------------------------------------------------
class Meridian__INTERFACE(Meridian__InterfaceBase):
    'Meridian__INTERFACE class implementation'
    Debug = False
    Count = 0

    def __init__(self):
        super().__init__()
        self.fields = ['RuleName', 'Signal', 'ClockDomains', 'Info']
        for field in fields:
            self.attr[field] = None # attr[key] = val(str)
            self.maxlen[field] = 0 # maxlen[key] = len(attr[key])
        __class__.Count += 1
        pass

    def parse(self, chunk):
        pass

    def write(self):
        # under construction
        pass

    pass

# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Meridian__U_INTERFACE.py
# - title : 
# - created : 20221023_222108
# - description
# ----------------------------------------------------------------------------
class Meridian__U_INTERFACE(Meridian__InterfaceBase):
    'Meridian__U_INTERFACE class implementation'
    Debug = False
    Count = 0

    def __init__(self):
        super().__init__()
        self.fields = ['RuleName', 'Signal', 'ClockDomains', 'Info']
        for field in fields:
            self.attr[field] = None # attr[key] = val(str)
            self.maxlen[field] = 0 # maxlen[key] = len(attr[key])
        __class__.Count += 1
        pass

    def parse(self, chunk):
        pass

    def write(self):
        # under construction
        pass

    pass

# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Meridian__W_INTERFACE.py
# - title : 
# - created : 20221023_222108
# - description
# ----------------------------------------------------------------------------
class Meridian__W_INTERFACE(Meridian__InterfaceBase):
    'Meridian__W_INTERFACE class implementation'
    Debug = False
    Count = 0

    def __init__(self):
        super().__init__()
        self.fields = ['RuleName', 'Signal', 'ClockDomains', 'Info']
        for field in fields:
            self.attr[field] = None # attr[key] = val(str)
            self.maxlen[field] = 0 # maxlen[key] = len(attr[key])
        __class__.Count += 1
        pass

    def parse(self, chunk):
        pass

    def write(self):
        # under construction
        pass

    pass

# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Meridian__W_GLITCH.py
# - title : 
# - created : 20221023_222108
# - description
# ----------------------------------------------------------------------------
class Meridian__W_GLITCH(Meridian__MultiPathRule):
    'Meridian__W_GLITCH class implementation'
    Debug = False
    Count = 0

    def __init__(self):
        super().__init__()
        self.fields = ['RuleName', 'DriverFlop', 'VictimFlop', 'ClockDomains', 'Info']
        for field in fields:
            self.attr[field] = None # attr[key] = val(str)
            self.maxlen[field] = 0 # maxlen[key] = len(attr[key])
        __class__.Count += 1
        pass

    def parse(self, chunk):
        pass

    def write(self):
        # under construction
        pass

    pass

# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Meridian__W_RECON_GROUPS.py
# - title : 
# - created : 20221023_222108
# - description
# ----------------------------------------------------------------------------
class Meridian__W_RECON_GROUPS(Meridian__MultiPathRule):
    'Meridian__W_RECON_GROUPS class implementation'
    Debug = False
    Count = 0

    def __init__(self):
        super().__init__()
        self.fields = ['RuleName', 'DriverFlop', 'ReconPoint', 'ReconDepth', 'ClockDomains', 'Info']
        for field in fields:
            self.attr[field] = None # attr[key] = val(str)
            self.maxlen[field] = 0 # maxlen[key] = len(attr[key])
        __class__.Count += 1
        pass

    def parse(self, chunk):
        pass

    def write(self):
        # under construction
        pass

    pass

