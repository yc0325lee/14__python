# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# File : lib__argparse.py
# Author : yc0325lee
# Created : 2022-03-08 00:01:28 by lee2103
# Modified : 2022-03-08 00:01:28 by lee2103
# Description : 
# ----------------------------------------------------------------------------
import os, os.path, sys
import pprint
import random
import argparse


if False:
    # -------------------------------------
    # - square() function
    # ; action='count' and action='store_true'
    # ; default (int) value
    parser = argparse.ArgumentParser(
        prog='square',
        description='this is an example of calculating square value',
        epilog='-' * 39,
    )
    parser.add_argument(
        "value", type=int, action='store', help="integer value"
    ) # action="store" (default)
    parser.add_argument(
        "-v", "--verbosity", type=int, choices=[0, 1, 2],
        help="output verbosity {0, 1, 2}"
    )
    parser.add_argument(
        "-c", "--count", action='count', default=0,
        help="number of times for print"
    )
    parser.add_argument(
        "-d", "--debug", action='store_true',
        help="debugging mode enable"
    )
    parser.print_help()
    # usage: example [-h] [-v {0,1,2}] [-c] [-d] value
    # example: error: unrecognized arguments: 5
    # 
    # C:\WORK\14__python>python lib__argparse_tutorial.py
    # usage: square [-h] [-v {0,1,2}] [-c] [-d] value
    # 
    # this is an example of calculating square value
    # 
    # positional arguments:
    #   value                 integer value
    # 
    # options:
    #   -h, --help            show this help message and exit
    #   -v {0,1,2}, --verbosity {0,1,2}
    #                         output verbosity {0, 1, 2}
    #   -c, --count           number of times for print
    #   -d, --debug           debugging mode enable
    # 
    # ---------------------------------------

    #arguements = [
    #    '-d', '--verbosity', '2', '-c', '--count', '-c', '4',
    #]
    arguements = [
        '-d', '--verbosity', '2', '-c', '5'
    ]
    args = parser.parse_args(arguements)
    print('args=', args)
    # args= Namespace(value=4, verbosity=2)

    if args.debug:
        print('[dbg ] debugg mode enabled!')
    # [dbg ] debugg mode enabled!

    answer = args.value ** 2
    if args.verbosity == 2:
        print(f"the square of {args.value} equals {answer}")
    elif args.verbosity == 1:
        print(f"{args.value}^2 == {answer}")
    else:
        print(answer)
    # the square of 4 equals 16

    for i in range(args.count):
        print(f'count= {i}, answer= {answer}')


if False:
    # -------------------------------------
    # - base**exponent function
    # ; action='count' and action='store_true'
    # ; default (int) value
    parser = argparse.ArgumentParser(
        prog='base ** exponent',
        description='this is an example of base**exponent',
        epilog='-' * 39,
    )
    parser.add_argument(
        "base", type=int, action='store', help="integer base value"
    ) # action="store" (default)
    parser.add_argument(
        "exponent", type=int, action='store', help="integer exponent value"
    ) # action="store" (default)
    parser.add_argument(
        "-v", "--verbosity", action='count', default=0,
        help="output verbosity {1, 2, ...}"
    )
    parser.add_argument(
        "-c", "--count", action='count', default=0,
        help="number of times for print"
    )
    parser.add_argument(
        "-d", "--debug", action='store_true',
        help="debugging mode enable"
    )
    parser.print_help()

    arguements = [
        '-d', '-vvv', '--count', '-c', '4', '5',
    ]
    args = parser.parse_args(arguements)
    print('args=', args)
    # args= Namespace(base=4, exponent=5, verbosity=3, count=1, debug=True)

    if args.debug:
        print('[dbg ] debugg mode enabled!')
    # [dbg ] debugg mode enabled!

    answer = args.base ** args.exponent
    if args.verbosity >= 2:
        filename = os.path.basename(__file__)
        print(f"[info] running '{filename}'...")
        print(f"{args.base} to the power {args.exponent} equals to {answer}!")
    elif args.verbosity >= 1:
        print(f"{args.base} ** {args.exponent} == {answer}")
    else:
        print(f"answer= {answer}")

    for i in range(args.count):
        print(f'count= {i}, answer= {answer}')
    # 4 to the power 5 equals to 1024!
    # count= 0, answer= 1024


if True:
    # -------------------------------------
    # - base**exponent function
    # ; using add_mutually_exclusive_group()
    parser = argparse.ArgumentParser(
        prog='base ** exponent',
        description='this is an example of base**exponent',
        epilog='-' * 39,
    )
    parser.add_argument(
        "base", type=int, action='store', help="integer base value"
    ) # action="store" (default)
    parser.add_argument(
        "exponent", type=int, action='store', help="integer exponent value"
    ) # action="store" (default)
    parser.add_argument(
        "-d", "--debug", action='store_true', help="debugging mode enable"
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-q", "--quiet", action='store_true', help="quiet output"
    )
    group.add_argument(
        "-v", "--verbose", action='store_true', help="verbose output"
    )
    parser.print_help()
    # usage: base ** exponent [-h] [-d] [-q | -v] base exponent
    # 
    # this is an example of base**exponent
    # 
    # positional arguments:
    #   base           integer base value
    #   exponent       integer exponent value
    # 
    # options:
    #   -h, --help     show this help message and exit
    #   -d, --debug    debugging mode enable
    #   -q, --quiet    quiet output
    #   -v, --verbose  verbose output
    # ---------------------------------------

    arguements = [
        '--debug', '--verbose', '2', '5',
    ]
    args = parser.parse_args(arguements)
    print('args=', args)

    if args.debug:
        print('[dbg ] debugg mode enabled!')
    # [dbg ] debugg mode enabled!

    answer = args.base ** args.exponent
    if args.quiet:
        print(f"answer= {answer}")
    elif args.verbose:
        filename = os.path.basename(__file__)
        print(f"[info] running '{filename}'...")
        print(f"{args.base} to the power {args.exponent} equals to {answer}!")
    else:
        print(f"{args.base} ** {args.exponent} == {answer}")
