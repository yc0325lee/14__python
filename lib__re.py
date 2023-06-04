#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# File : lib__re.py
# Author : yc0325lee
# Created : 2022-03-05 20:34:39 by lee2103
# Modified : 2022-03-05 20:34:39 by lee2103
# Description : 
#
# - raw string r"pattern" or r'pattern'
# ; every backslash ('\') in a regular expression doesn't need to be prefixed
#   with another one to escape it.
# ; re.match("\\W(.)\\1\\W", " ff ")
# ; re.match(r"\W(.)\1\W", " ff ")
#
# - flags
# ; re.A       re.ASCII
# ; re.DEBUG
# ; re.I       re.IGNORECASE
# ; re.L       re.LOCALE
# ; re.M       re.MULTILINE
# ; re.S       re.DOTALL
# ; re.X       re.VERBOSE
# ; example
#   flag = re.I|re.M|re.X
#
# ----------------------------------------------------------------------------
from utilities import printv
import re

lines = """
park 800905-1049118
kim 700905-1059119
shin 680419-2051218
lee 911207-1078074
xxx xxxxxx-xxxxxxx
"""

if False:
    # ------------------------------------------------------------------------
    # - regex = re.compile(pattern, flags=0)
    # ; compile a regular expression pattern into a regular expression object,
    #   which can be used for matching using its match(), search() and other
    #   methods
    #
    # - re.match(pattern, string, flags=0)
    # - regex.match(string, flags=0)
    # ; if zero or more characters at the beginning of string match the
    #   regular expression pattern return a corresponding match object.
    # ; return none if the string does not match the pattern
    #
    # - re.search(pattern, string, flags=0)
    # - regex.search(string[, pos[, endpos]])
    # ; scan through string looking for the first location where this regular
    #   expression produces a match, and return a corresponding match object.
    # ; never match unless match from the start
    # ; return none if no position in the string matches the pattern
    #
    # - re.match() vs. re.search()
    # ; match() find match from the start of string
    # ; 시작부터 match가 되지 않으면 더이상 search하지 않음
    # ------------------------------------------------------------------------

    regex = re.compile("(\d{6})[-]\d{7}")
    print(type(regex))
    print(regex)

    print('\n# testing re.search()')
    for line in lines.split("\n"):
        if line.isspace(): continue
        if not line: continue

        matched = regex.search(line)
        if matched:
            print("line= {}, matched, group= {}, start= {}, end= {}, span= {}"
                .format(line, match.group(), match.start(), match.end(), match.span()))
            #                 -------------  -------------  -----------  ------------
        else:
            print("line=", line, "not matched")
    # testing re.search()
    # park 800905-1049118, matched, group= 800905-1049118, start= 5, end= 19, span= (5, 19)
    # kim 700905-1059119, matched, group= 700905-1059119, start= 4, end= 18, span= (4, 18)
    # shin 680419-2051218, matched, group= 680419-2051218, start= 5, end= 19, span= (5, 19)
    # lee 911207-1078074, matched, group= 911207-1078074, start= 4, end= 18, span= (4, 18)
    # xxx xxxxxx-xxxxxxx not matched

    print('\n# testing re.match()')
    for line in lines.split("\n"):
        if line.isspace(): continue
        if not line: continue

        matched = regex.match(line)
        if matched:
            print("line= {}, matched, group= {}, start= {}, end= {}, span= {}"
                .format(line, match.group(), match.start(), match.end(), match.span()))
            #                 -------------  -------------  -----------  ------------
        else:
            print("line=", line, "not matched")
    # testing re.match()
    # line= park 800905-1049118 not matched
    # line= kim 700905-1059119 not matched
    # line= shin 680419-2051218 not matched
    # line= lee 911207-1078074 not matched
    # line= xxx xxxxxx-xxxxxxx not matched

if False:
    # re.sub(pattern, repl, string, count=0, flags=0)
    # pattern.sub(repl, string, count=0)
    # ; return the string obtained by replacing the leftmost non-overlapping
    #   occurrences of pattern in string by the replacement repl.
    # ; count is the maximum number of pattern occurrences to be replaced;
    #   count must be a non-negative integer. If omitted or zero, all
    #   occurrences will be replaced.

    regex = re.compile("(\d{6})[-](\d{7})")
    #                    -----     -----
    #                    captured -> referenced by \g<1>
    for lineno, line in enumerate(lines.split("\n"), 1):
        if line.isspace(): continue
        if not line: continue
        print(lineno, line)
        print(lineno, regex.sub("\g<1>-\g<2> and \g<0>", line))

    print()

    regex = re.compile("(?P<first>\d{6})[-](?P<second>\d{7})")
    #                    --------------     ---------------
    #                      \g<first>           \g<second>
    for lineno, line in enumerate(lines.split("\n"), 1):
        if line.isspace(): continue
        if not line: continue
        print(lineno, line)
        print(lineno, regex.sub("\g<first>-\g<second> and \g<0>", line))


if False:
    # re.findall(pattern, string, flags=0)
    # ; return all non-overlapping matches of pattern in string, as a list of
    #   strings or tuples. the string is scanned left-to-right, and matches are
    #   returned in the order found. empty matches are included in the result.
    line = "life is too short"
    regex = re.compile("[a-z_]+")

    print("regex.findall=", regex.findall(line)) # list
    # regex.findall= ['life', 'is', 'too', 'short']

    for token in regex.findall(line):
        print("token=", token)

if False:
    # re.finditer(pattern, string, flags=0)
    # ; return an iterator yielding match objects over all non-overlapping
    #   matches for the re pattern in string. the string is scanned left-to-right,
    #   and matches are returned in the order found.
    # ; empty matches are included in the result.
    line = "life is too short"
    regex = re.compile("[a-z_]+")
    print("regex.finditer=", regex.finditer(line)) # iterator
    # regex.finditer= <callable_iterator object at 0x00000221004F0400>

    for found in regex.finditer(line):
        print("found=", found)
        print("found.group()=", found.group())


if False:
    # re.X or re.VERBOSE
    # re.compile("regex_str", re.VERBOSE)
    # ; This flag allows you to write regular expressions that look nicer and
    #   are more readable by allowing you to visually separate logical sections of
    #   the pattern and add comments. Whitespace within the pattern is ignored,
    regex = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
    regex = re.compile(r"""
                           &[#]                # Start of a numeric entity reference
                           (                   #
                               0[0-7]+         # Octal form
                             | [0-9]+          # Decimal form
                             | x[0-9a-fA-F]+   # Hexadecimal form
                           )                   #
                           ;                   # Trailing semicolon""", re.VERBOSE)

if False:
    # - capturing & extracting sub-match
    regex = re.compile(r"(\w+)\s+(\d+)[-](\d+)")
    #                     ---     ---     ---
    #                    \g<1>   \g<2>   \g<3>
    #                 group(1)  group(2)  group(3)
    #                 ----------------------------
    #                     group() or group(0)

    for lineno, line in enumerate(lines.split("\n"), 1):
        if line.isspace(): continue
        if not line: continue
        print('# line=', lineno, line)

        matched = regex.search(line)
        if matched:
            print("# matched, group= {}, start= {}, end= {}, span= {}"
                .format(matched.group(), matched.start(), matched.end(), matched.span()))
            print("# group()=", matched.group())
            print("# group(0)=", matched.group(0))
            print("# group(1)=", matched.group(1))
            print("# group(2)=", matched.group(2))
            print("# group(3)=", matched.group(3))
        else:
            print("# not matched")
        print()
    # ---------------------------------------------------------------------
    # 2 park 800905-1049118
    # matched, group= park 800905-1049118, start= 0, end= 19, span= (0, 19)
    # group(0)= park 800905-1049118
    # group(1)= park
    # group(2)= 800905
    # group(3)= 1049118
    #
    # 3 kim 700905-1059119
    # matched, group= kim 700905-1059119, start= 0, end= 18, span= (0, 18)
    # group(0)= kim 700905-1059119
    # group(1)= kim
    # group(2)= 700905
    # group(3)= 1059119
    #
    # 4 shin 680419-2051218
    # matched, group= shin 680419-2051218, start= 0, end= 19, span= (0, 19)
    # group(0)= shin 680419-2051218
    # group(1)= shin
    # group(2)= 680419
    # group(3)= 2051218
    #
    # 5 lee 911207-1078074
    # matched, group= lee 911207-1078074, start= 0, end= 18, span= (0, 18)
    # group(0)= lee 911207-1078074
    # group(1)= lee
    # group(2)= 911207
    # group(3)= 1078074
    #
    # 6 xxx xxxxxx-xxxxxxx
    # not matched
    # ---------------------------------------------------------------------


if False:
    # - named capturig group
    regex = re.compile(r"(?P<name>\w+)\s+(?P<first>\d+)[-](?P<last>\d+)")
    #                    -------------   --------------   -------------
    #                    group("name")   group("first")   group("last")
    #                         |               |                |
    #                         +---------------+----------------+
    #                                         |
    #                                 group() or group(0)

    for lineno, line in enumerate(lines.split("\n"), 1):
        if line.isspace(): continue
        if not line: continue
        print('# line=', lineno, line)

        matched = regex.search(line)
        if matched:
            print("# matched, group= {}, start= {}, end= {}, span= {}"
                .format(matched.group(), matched.start(), matched.end(), matched.span()))
            print("# group()=", matched.group())
            print("# group(0)=", matched.group(0))
            print('# group("name")=', matched.group("name")) # reference by name(str)
            print('# group("first")=', matched.group("first"))
            print('# group("last")=', matched.group("last"))
        else:
            print("# not matched")
        print()
    # ---------------------------------------------------------------------
    # line= 2 park 800905-1049118
    # matched, group= park 800905-1049118, start= 0, end= 19, span= (0, 19)
    # group()= park 800905-1049118
    # group(0)= park 800905-1049118
    # group("name")= park
    # group("first")= 800905
    # group("last")= 1049118
    #
    # line= 3 kim 700905-1059119
    # matched, group= kim 700905-1059119, start= 0, end= 18, span= (0, 18)
    # group()= kim 700905-1059119
    # group(0)= kim 700905-1059119
    # group("name")= kim
    # group("first")= 700905
    # group("last")= 1059119
    #
    # line= 4 shin 680419-2051218
    # matched, group= shin 680419-2051218, start= 0, end= 19, span= (0, 19)
    # group()= shin 680419-2051218
    # group(0)= shin 680419-2051218
    # group("name")= shin
    # group("first")= 680419
    # group("last")= 2051218
    #
    # line= 5 lee 911207-1078074
    # matched, group= lee 911207-1078074, start= 0, end= 18, span= (0, 18)
    # group()= lee 911207-1078074
    # group(0)= lee 911207-1078074
    # group("name")= lee
    # group("first")= 911207
    # group("last")= 1078074
    #
    # line= 6 xxx xxxxxx-xxxxxxx
    # not matched
    # ---------------------------------------------------------------------


if False:
    # - re.split(pattern, string, maxsplit=0, flags=0)
    # ; split string by the occurrences of pattern.
    # ; if capturing parentheses are used in pattern, then the text of all
    #   groups in the pattern are also returned as part of the resulting list.
    # ; if maxsplit is nonzero, at most maxsplit splits occur, and the remainder
    #   of the string is returned as the final element of the list.
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    fields = re.split(r'[;,\s]\s*', line)
    print(type(fields))
    print(fields) # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']


if False:
    # meta(special) characters in string
    lines = r'''     
park [[\abc  xyz]] 800905-1049118 [[abcd 3421 ]]
kim  [[\abc  xyz]] 700905-1059119 [[abcd 3421 ]]
shin [[\abc  xyz]] 680419-2051218 [[xyzw 3421 ]]
lee  [[\abc  xyz]] 911207-1078074 [[abcd 3421 ]]
xxx xxxxxx-xxxxxxx [[abcd 3421 ]]
  '''
    for lineno, line in enumerate(lines.split("\n"), 1):
        if not line: continue
        if line.isspace(): continue
        print(lineno, ':', line)

        regex = re.compile('\[\[[^\[\]]+\]\]') # compiled in advance for performance
        for source in regex.findall(line):
            target = re.sub('\s+', '', source) # remove white-spaces
            target = re.sub(r'\\', '', target) # remove back-slashes
            line = line.replace(source, target)
            print('   ', line)

        print(lineno, ':', line, end='\n\n')


if False:
    # --------------------------------------------------
    #  '*',  '+',  '?', {m,n}  ---> greedy qualifier
    # '*?', '+?', '??', {m,n}? ---> non-greedy qualifier
    # --------------------------------------------------
    lines = r'''     
<park> <800905-1049118> <abc>
<kiml> <700905-1059119> <abc>
<shin> <680419-2051218> <xyz>
<leex> <911207-1078074> <abc>
  '''
    print("# greedy")
    regex = re.compile('<.+>')
    for lineno, line in enumerate(lines.split("\n"), 1):
        if not line: continue
        if line.isspace(): continue
        print(lineno, ':', line)
        for item in regex.findall(line): # re.findall('<.+>', line)
            print("# found=", item)
        print()
        # <park> <800905-1049118> <abc>
        # found= <park> <800905-1049118> <abc>

    print("\n# non-greedy")
    regex = re.compile('<.+?>')
    for lineno, line in enumerate(lines.split("\n"), 1):
        if not line: continue
        if line.isspace(): continue
        print(lineno, ':', line)
        for item in regex.findall(line): # re.findall('<.+?>', line)
            print("# found=", item)
        print()
        # <park> <800905-1049118> <abc>
        # found= <park>
        # found= <800905-1049118>
        # found= <abc>
