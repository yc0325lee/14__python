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

rule_hierarchy = {
    'Meridian__Common' : {
        'Meridian__RuleBase' : {
            'Meridian__SinglePathRule' : {
                'Meridian__CNTL' : {},
                'Meridian__DATA' : {},
                'Meridian__W_CNTL' : {},
                'Meridian__W_DATA' : {},
            },
            'Meridian__MultiPathRule' : {
                'Meridian__InterfaceBase' : {
                    'Meridian__INTERFACE' : {},
                    'Meridian__U_INTERFACE' : {},
                    'Meridian__W_INTERFACE' : {},
                },
                'Meridian__W_GLITCH' : {},
                'Meridian__W_RECON_GROUPS' : {},
            },
        },
    },
}

rule_attribute = {
    'Meridian__Common' : '',
    'Meridian__RuleBase' : '',
    'Meridian__SinglePathRule' : '',
    'Meridian__CNTL' : '',
    'Meridian__DATA' : '',
    'Meridian__W_CNTL' : '',
    'Meridian__W_DATA' : '',
    'Meridian__MultiPathRule' : '',
    'Meridian__InterfaceBase' : '',
    'Meridian__INTERFACE' : '',
    'Meridian__U_INTERFACE' : '',
    'Meridian__W_INTERFACE' : '',
    'Meridian__W_GLITCH' : '',
    'Meridian__W_RECON_GROUPS' : '',
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
        #print("[dbg ] visiting {} ...".format(thisName), file=sys.stderr)
        nodeStack.append(thisName)

        # write parent-first & child-later!
        if __is_root_node(hier[thisName]):
            if False: print("[dbg ] {} is root-node!".format(thisName), file=sys.stderr)
            write_root_class(None, thisName)
        else:
            if __is_leaf_node(hier[thisName]):
                if False: print("[dbg ] {} is leaf-node!".format(thisName), file=sys.stderr)
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

def __write_header(baseName, thisName, file=sys.stdout):
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
        .format(**args), file=file
    )

def __write_body(baseName, thisName, file=sys.stdout):

    if baseName is not None:
        baseName = '(' + baseName + ')'
    else:
        baseName = ''

    #attributes = rule_attribute[thisName].split(' ')
    #attr = '{' + ', '.join(map(lambda attr: attr + ':None', attributes)) + '}'
    #fields = '[' + ', '.join(map(lambda s: "'" + s + "'", attributes)) + ']'

    args = {
        'basename' : baseName,
        'thisname' : thisName,
    }

    if baseName:
        print("from {} import {}"
            .format(baseName.strip('()'), baseName.strip('()')),
            end='\n\n', file=file)
        args['memberdata'] = ''
    else:
        args['memberdata'] = '\n        self._data = dict()'

    print(
"""class {thisname:s}{basename:s}:
    '{thisname:s} class implementation'
    debug = False
    count = 0

    attributes = None
    maxlen = dict()

    @classmethod
    def init_class_data(cls):
        for attr in __class__.attributes:
            __class__.maxlen[attr] = len(attr)
        
    def __init__(self, chunk):
        super().__init__(chunk){memberdata:s}
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

    pass"""
        .format(**args), file=file
    )


def write_root_class(parentName, thisName):
    outFileName = thisName + '.py'
    print("[info] writing {} ...".format(outFileName), file=sys.stderr)
    with open(outFileName, "w", encoding="utf8") as outFile:
        __write_header(parentName, thisName, file=outFile)
        __write_body(parentName, thisName, file=outFile)
    pass

def write_derived_class(parentName, thisName):
    outFileName = thisName + '.py'
    print("[info] writing {} ...".format(outFileName), file=sys.stderr)
    with open(outFileName, "w", encoding="utf8") as outFile:
        __write_header(parentName, thisName, file=outFile)
        __write_body(parentName, thisName, file=outFile)
    pass

def write_main(leaves):
    print("[info] write_main() invoked ...", file=sys.stderr)
    pass



# -------------------------------------
# main
if __name__ == "__main__":
    traverse(rule_hierarchy)
