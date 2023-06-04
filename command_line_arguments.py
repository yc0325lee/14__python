# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : command_line_arguments.py
# - author : yc0325lee
# - created : 2022-10-15 11:43:36 by lee2103
# - modified : 2022-10-15 11:43:36 by lee2103
# - description : 
# ----------------------------------------------------------------------------


# -------------------------------------
# - (1) using sys.argv
# ; the list of command line arguments passed to a python script
if False:
    import sys
    args = sys.argv[1:]
    for i, arg in enumerate(args):
        print("arg[%d]= %s" % (i, arg))
    # ---------------------------------------------------------
    # python    main.py    aaa        bbb        ccc        ...
    #           -------    -------    -------    -------
    #           argv[0]    argv[1]    argv[2]    argv[3]    ...
    # ---------------------------------------------------------


# -------------------------------------
# - (2) using argparse library
if False:
    import argparse
    parser = argparse.ArgumentParser(
        prog="python command_line_arguments.py",
        description="explanation: calculate the sum of all input integer values",
        epilog="----------- end of usage -------------"
    )
    parser.add_argument("value", type=int, nargs="+", help="value (integer)")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true", help="turn on verbose-mode")
    group.add_argument("-q", "--quiet", action="store_true", help="turn on quiet-mode")
    group.add_argument("--version", action="version", version="%(prog)s v1.00", help="show program version")
    args = parser.parse_args()

    answer = 0
    for val in args.value:
        answer += val

    if args.quiet:
        print(answer)
    elif args.verbose:
        for i, val in enumerate(args.value):
            if i == len(args.value)-1:
                print(f"{val} = ", end="")
            else:
                print(f"{val} + ", end="")
        print(answer)
    else:
        print(f"sum = {answer}")
