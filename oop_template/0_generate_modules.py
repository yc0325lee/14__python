# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# File : 0_generate_modules.py
# Author : yc0325lee
# Created : 2022-10-09 15:23:49 by lee2103
# Modified : 2022-10-09 15:23:49 by lee2103
# Description : 
# ----------------------------------------------------------------------------
import sys
import os
import time


prefix = 'Employ__'
category = 'Company'
rule_hierarchy = {
    'Common' : {
        'CompanyBase' : {
            'Apple' : {},
            'Hwawei' : {},
            'Intel' : {},
            'Samsung' : {},
            'Qualcom' : {},
        },
    },
}

rule_attribute = {
    'Common' : '',
    'CompanyBase' : 'name age salary',
    'Apple' : 'rsvd0',
    'Hwawei' : 'rsvd1',
    'Intel' : 'rsvd2',
    'Samsung' : 'rsvd3',
    'Qualcom' : 'rsvd4',
};



nodeStack = list()
leaves = list()

def __is_root_node(node):
    return len(nodeStack) == 1
def __is_leaf_node(node):
    return len(node) == 0 # if there's no child!
def __depth():
    return len(nodeStack)-1

def traverse(hier):
    for thisName in hier.keys():
        print("[debug] visiting {} ...".format(thisName), file=sys.stderr)
        nodeStack.append(thisName)

        # write parent-first & child-later!
        if __is_root_node(hier[thisName]):
            write_root_class(None, thisName)
        else:
            if __is_leaf_node(hier[thisName]):
                print("[debug] {} is leaf-node!".format(thisName), file=sys.stderr)
                leaves.append(thisName)

            parentName = nodeStack[-2]
            write_derived_class(parentName, thisName)

        traverse(hier[thisName]) # recursive visit

        # end-of-traversing stuffs
        if __is_root_node(hier[thisName]):
            write_main(leaves)
            leaves.clear()

        nodeStack.pop()
    pass


def __now():
    return time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))

def __write_header(baseName, thisName):
    args = {
        'filename' : thisName + '.py',
        'title' : '',
        'created' : __now(),
    }
    print(
"""# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : {filename:s}
# - title : {title:s}
# - created : {created:s}
# - description
# ----------------------------------------------------------------------------"""
        .format(**args)
    )

def __write_body(baseName, thisName):

    if baseName is not None:
        baseName = '(' + baseName + ')'
    else:
        baseName = ''

    attributes = rule_attribute[thisName].split(' ')
    #attr = '{' + ', '.join(map(lambda attr: attr + ':None', attributes)) + '}'
    fields = '[' + ', '.join(map(lambda s: "'" + s + "'", attributes)) + ']'

    args = {
        'basename' : baseName,
        'thisname' : thisName,
        'fields' : fields,
    }

    print(
"""class {thisname:s}{basename:s}:
    '{thisname:s} class implementation'
    Debug = False
    Count = 0

    def __init__(self):
        super().__init__()
        self.fields = {fields:s}
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
"""
        .format(**args)
    )


def write_root_class(parentName, thisName):
    print("[info] write_root_class() invoked ...", file=sys.stderr)
    __write_header(parentName, thisName)
    __write_body(parentName, thisName)
    pass

def write_derived_class(parentName, thisName):
    print("[info] write_derived_class() invoked ...", file=sys.stderr)
    __write_header(parentName, thisName)
    __write_body(parentName, thisName)
    pass

def write_main(leaves):
    print("[info] write_main() invoked ...", file=sys.stderr)
    pass



# -------------------------------------
# main
if __name__ == "__main__":
    traverse(rule_hierarchy)
