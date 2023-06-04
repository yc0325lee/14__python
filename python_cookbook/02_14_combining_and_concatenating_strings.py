#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 02_14_combining_and_concatenating_strings.py
# - author : yc0325lee
# - created : 2022-11-25 23:31:24 by yc032
# - modified : 2022-11-25 23:31:24 by yc032
# - description : 
# ----------------------------------------------------------------------------

if False:
    parts = ['Is', 'Chicago', 'Not', 'Chicago?']
    combined = ' '.join(parts)
    print('combined =', combined)
    combined = ','.join(parts)
    print('combined =', combined)
    combined = ','.join(parts)
    print('combined =', combined)

if False:
    a = 'Is Chicago'
    b = 'Not Chicagoo?'
    joined = a + ' ' + b
    print('joined =', joined)

if False:
    print('{} {}'.format(a, b))
    print(a + ' ' + b) # same as above

if False:
    joined = 'Hello' 'World'
    print('joined =', joined) # same as 'Hello' + 'World'

if False:
    parts = ['Is', 'Chicago', 'Not', 'Chicago?']
    concatenated = ''
    for part in parts:
        concatenated += part
    print('concatenated =', concatenated)

if False:
    # sometimes data conversion required!
    # (int -> str, float -> str)
    data = ['ACME', 50, 91.1]
    print(','.join(str(datum) for datum in data))
    #              ----------
    #              conversion

if False:
    # several ways
    print(a + ':' + b + ':' + c) # ugly
    print(':'.join([a, b, c])) # still ugly
    print(a, b, c, sep=':') # better


if False:
    # using generator function
    def get_string():
        yield 'Is'
        yield 'Chicago'
        yield 'Not'
        yield 'Chicago?'

    combined = ' '.join(sample())
    print('combined =', combined)

    for part in sample():
        print(part)

if False:
    # using both join and generator function
    def combine(source, maxsize):
        parts = []
        size = 0
        for part in source:
            parts.append(part)
            size += len(part)
            if size > maxsize:
                yield ''.join(parts)
                parts = []
                size = 0

        yield ''.join(parts) # yield remainings
    
    for part in combine(sample(), 32768):
        outfile.write(part)
