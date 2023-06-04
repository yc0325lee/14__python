#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__argparse.py
# - author : yc0325lee
# - created : 2023-05-27 21:30:36 by yc032
# - modified : 2023-05-27 21:30:36 by yc032
# - description : 
# ----------------------------------------------------------------------------
import os, os.path, sys
import pprint
import random
import argparse

if False:
    # -------------------------------------
    # - class argparse.ArgumentParser(
    #       prog=None, usage=None, description=None, epilog=None, parents=[],
    #       formatter_class=argparse.HelpFormatter, prefix_chars='-',
    #       fromfile_prefix_chars=None, argument_default=None,
    #       conflict_handler='error', add_help=True, allow_abbrev=True,
    #       exit_on_error=True
    #   )
    # ; create a new argumentparser object. all parameters should be passed as
    #   keyword arguments
    # ; prefix_chars='-' ---> default
    # ; prefix_chars='-+' ---> can handle +define or +libdir ...
    pass

if False:
    # -------------------------------------
    # - ArgumentParser.add_argument(
    #       name or flags...[, action][, nargs][, const][, default][, type]
    #       [, choices][, required][, help][, metavar][, dest]
    #   )
    # ; define how a single command-line argument should be parsed.
    #
    # ; name or flags - either a name or a list of option strings,
    #                   e.g. foo or -f, --foo.
    # ; action - the basic type of action to be taken when this argument is
    #            encountered at the command line.
    #            default=store
    # ; nargs - the number of command-line arguments that should be consumed.
    # ; const - a constant value required by some action and nargs selections.
    # ; default - the value produced if the argument is absent from the
    #             command line and if it is absent from the namespace object.
    # ; type - the type to which the command-line argument should be converted.
    # ; choices - a sequence of the allowable values for the argument.
    # ; required - whether or not the command-line option(-f or --foo) may be
    #              omitted (affects optionals only).
    # ; help - a brief description of what the argument does.
    # ; metavar - a name for the argument in usage messages.
    # ; dest - the name of the attribute to be added to the object returned by
    #          parse_args().
    # +----------+--------------------------------------------+------------------------------------+
    # | name     | description                                | values                             |
    # +----------+--------------------------------------------+------------------------------------+
    # | action   | specify how an argument should be handled  | 'store' 'store_const' 'store_true' |
    # |          |                                            | 'append' 'append_const'            |
    # |          |                                            | 'count' 'help' 'version'           |
    # | choices  | limit values to a specific set of choices  | ['foo','bar'], range(1, 10)        |
    # |          |                                            | or container instance              |
    # | const    | store a constant value                     |                                    |
    # | default  | default value used when an argument is     | defaults to none                   |
    # |          | not provided                               |                                    |
    # | dest     | specify the attribute name used            |                                    |
    # |          | in the result namespace                    |                                    |
    # | help     | help message for an argument               |                                    |
    # | metavar  | alternate display name for the argument    |                                    |
    # |          | as shown in help                           |                                    |
    # | nargs    | number of times the argument can be used   | int '?' '*' or '+'                 |
    # | required | indicate whether an argument is required   | true or false                      |
    # |          | or optional                                |                                    |
    # | type     | automatically convert an argument          | int float argparse.filetype('w')   |
    # |          | to the given type                          | or callable function               |
    # +----------+--------------------------------------------+------------------------------------+
    pass

if False:
    # -------------------------------------
    # - ArgumentParser.parse_args(args=None, namespace=None)
    # ; convert argument strings to objects and assign them as attributes of
    #   the namespace.
    # ; return the populated namespace.
    # ; args=None -> from sys.argv list
    #   args=list -> from list of string
    #
    # - ArgumentParser.add_argument_group(title=None, description=None)
    # ; conceptual groups can be created
    #
    # - ArgumentParser.add_mutually_exclusive_group(required=False)
    # ; create a mutually exclusive group.
    #
    # - ArgumentParser.set_defaults(**kwargs)
    # ; set_defaults() allows some additional attributes that are determined
    #   without any inspection of the command line to be added
    #
    # - ArgumentParser.get_default(dest)
    # ; get the default value for a namespace attribute, as set by either
    #   add_argument() or by set_defaults()
    #
    # - ArgumentParser.print_usage(file=None)
    # - ArgumentParser.print_help(file=None)
    # - ArgumentParser.format_usage()
    # - ArgumentParser.format_help()
    pass

if False:
    # -------------------------------------
    # - ArgumentParser.parse_known_args(args=None, namespace=None)
    # ; may only parse a few of the command-line arguments, passing the
    #   remaining arguments on to another script or program
    # ; does not produce an error when extra arguments are present. instead,
    #   it returns a two item tuple containing the populated namespace and the
    #   list of remaining argument strings.
    pass

if False:
    # -------------------------------------
    # - example
    parser = argparse.ArgumentParser(
        prog="python " + os.path.basename(__file__),
        description='this is an example of argparse',
        epilog='--------------- epilog ------------------',
    )
    parser.add_argument('filename')
    parser.add_argument('-c', '--count', type=int)
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.print_help()
    # usage: example [-h] [-c COUNT] [-v] filename
    # this is an example of argparse
    # positional arguments:
    #   filename
    # options:
    #   -h, --help            show this help message and exit
    #   -c COUNT, --count COUNT
    #   -v, --verbose

    options = [ # all string
        'somefile.txt', '--count', '4', '--verbose'
    ]
    args = parser.parse_args(options)
    print("args=", args)
    print("args.filename=", args.filename, type(args.filename))
    print("args.count=", args.count, type(args.count))
    print("args.verbose=", args.verbose, type(args.verbose))
    # args= Namespace(filename='somefile.txt', count=4, verbose=True)
    # args.filename= somefile.txt <class 'str'>
    # args.count= 4 <class 'int'>
    # args.verbose= True <class 'bool'>


if False:
    # -------------------------------------
    # - joined short options
    parser = argparse.ArgumentParser(
        prog="python " + os.path.basename(__file__),
        description='this is an example of argparse',
        epilog='--------------- epilog ------------------',
    )
    parser.add_argument('-w', action='store_true')
    parser.add_argument('-x', action='store_true')
    parser.add_argument('-y', action='store_true')
    parser.add_argument('-z', action='store_true')
    parser.print_help()
    # usage: example [-h] [-w] [-x] [-y] [-z]
    # this is an example of argparse
    # options:
    #   -h, --help  show this help message and exit
    #   -w
    #   -x
    #   -y
    #   -z

    options = [ # all string
        '-wxy'
    ]
    args = parser.parse_args(options)
    print("args=", args)
    # args= Namespace(w=True, x=True, y=True, z=False)

    print("vars(args)=", vars(args)) # returns __dict__ attribute of object
    # vars(args)= {'w': True, 'x': True, 'y': True, 'z': False}
    

if False:
    # -------------------------------------
    # - inheriting base-parser
    # - using parse_known_args()
    base = argparse.ArgumentParser(add_help=False) # base-parser
    base.add_argument(
        '-i', '--input', help="input filename", default='input.txt',
        metavar='input.txt'
    )
    base.add_argument(
        '-o', '--output', help="input filename", default='output.txt',
        metavar='output.txt'
    )

    # derived_0
    derived_0 = argparse.ArgumentParser(
        prog="python " + os.path.basename(__file__),
        parents=[base],
        description='derived_0 argparser from base',
        epilog='---- end of derived_0 ----',
    )
    derived_0.add_argument(
        '--language', help="language type (verilog/systemverilog/vhdl)",
        default='verilog', required=True,
        choices=['verilog', 'systemverilog', 'vhdl', 'systemc'],
    )
    derived_0.add_argument(
        '--log', help="log-file name",
        default='message.log', metavar='message.log'
    )
    derived_0.print_help()
    # usage: python lib__argparse.py [-h] [-i input.txt] [-o output.txt] --language
    #                                {verilog,systemverilog,vhdl,systemc} [--log message.log]
    # 
    # derived_0 argparser from base
    # 
    # options:
    #   -h, --help            show this help message and exit
    #   -i input.txt, --input input.txt
    #                         input filename
    #   -o output.txt, --output output.txt
    #                         input filename
    #   --language {verilog,systemverilog,vhdl,systemc}
    #                         language type (verilog/systemverilog/vhdl)
    #   --log message.log     log-file name
    # 
    # ---- end of derived_0 ----

    # derived_1
    derived_1 = argparse.ArgumentParser(
        prog="python " + os.path.basename(__file__),
        parents=[base],
        description='derived_1 argparser from base',
        epilog='---- end of derived_1 ----',
    )
    derived_1.add_argument(
        '--tech', help="technology node (20nm, 14nm, 10nm, 7nm, 5nm, 3nm)",
        default='7nm', required=True,
        choices="20nm 14nm 10nm 7nm 5nm 3nm".split(),
    )
    derived_1.add_argument(
        '--ratio', type=float, action='store', default=1.0,
        required=False,
        help="dropout_ratio, float (0.0, 1.0], default=1.0"
    )
    derived_1.print_help()
    # usage: python lib__argparse.py [-h] [-i input.txt] [-o output.txt] --tech {20nm,14nm,10nm,7nm,5nm,3nm}
    #                                [--ratio RATIO]
    # 
    # derived_1 argparser from base
    # 
    # options:
    #   -h, --help            show this help message and exit
    #   -i input.txt, --input input.txt
    #                         input filename
    #   -o output.txt, --output output.txt
    #                         input filename
    #   --tech {20nm,14nm,10nm,7nm,5nm,3nm}
    #                         technology node (20nm, 14nm, 10nm, 7nm, 5nm, 3nm)
    #   --ratio RATIO         dropout_ratio, float (0.0, 1.0], default=1.0
    # 
    # ---- end of derived_1 ----

    arguements = "--input input.txt --output output.txt --log message.log --language vhdl --tech 14nm --ratio 0.7".split()
    print("arguements=", arguements)

    args = derived_0.parse_known_args(arguements)
    print('args=', args)

    args = derived_1.parse_known_args(arguements)
    print('args=', args)
    # args= (
    #   Namespace(input='input.txt', output='output.txt', language='vhdl', log='message.log'), -> swallowed
    #   ['--tech', '14nm', '--ratio', '0.7'] -> remaining
    # )
    #
    # args= (
    #   Namespace(input='input.txt', output='output.txt', tech='14nm', ratio=0.7), -> swallowed
    #   ['--log', 'message.log', '--language', 'vhdl'] -> remaining
    # )


if False:
    # -------------------------------------
    # - allowing multiple arguments with single option
    parser = argparse.ArgumentParser(
        prog="python " + os.path.basename(__file__),
        description="testing append and extend actions",
        epilog='---- end of parser help ----',
    )
    parser.add_argument(
        '--files', action='extend', nargs='+', required=False,
        help="single filename", metavar='FILE',
    )
    parser.add_argument(
        '--file', action='append', required=False,
        help="single filename", metavar='FILE'
    )
    parser.print_help()

    arguements = "--file aaa --file bbb --files ccc ddd eee".split()
    args = parser.parse_args(arguements)
    print('args=', args)

    import itertools
    for i, filename in enumerate(itertools.chain(args.file, args.files)):
        print(f"file[{i}]= {filename}")


if False:
    # -------------------------------------
    # - allowing multiple arguments with single option
    # ; using dest will eliminate the need of 'itertools.chain'
    parser = argparse.ArgumentParser(
        prog="python " + os.path.basename(__file__),
        description="testing append and extend actions",
        epilog='---- end of parser help ----',
    )
    parser.add_argument(
        '--files', action='extend', nargs='+', dest='files', required=False,
        help="single filename", metavar='FILE',
    )
    parser.add_argument(
        '--file', action='append', dest='files', required=False,
        help="single filename", metavar='FILE'
    )
    parser.print_help()

    arguements = "--file aaa --file=bbb --files ccc ddd eee --file fff --file=ggg --files hhh iii".split()
    args = parser.parse_args(arguements)
    print('args=', args)
    # args= Namespace(files=['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii'])

    #import itertools
    #for i, filename in enumerate(itertools.chain(args.file, args.files)):
    #    print(f"file[{i}]= {filename}")
    for i, filename in enumerate(args.files):
        print(f"file[{i}]= {filename}")


if False:
    # -------------------------------------
    # - arguments for deep_cnn trainig & testing
    parser = argparse.ArgumentParser(
        prog=os.path.basename(__file__),
        description="train or test 'deep_cnn' model",
        epilog="----------- end of usage -------------"
    )
    parser.add_argument(
        '--version', action='version', version='%(prog) v1.0.a',
        help="current version"
    )
    parser.add_argument(
        '--dtype', type=str, action='store', default='float64', required=False,
        help="data-type for cnn parameters and inputs - float64(default), float32, float16"
    )
    parser.add_argument(
        "--dropout", type=float, action='store', default=0.0, required=False,
        help="dropout_ratio, float [0.0, 1.0), default=0.0"
    )
    parser.add_argument(
        "--epoch", type=int, action='store', default=20, required=False,
        help="number of epochs for training, integer(>0), default=20"
    )
    parser.add_argument(
        "--batch_normalize", action='store_true', required=False,
        help="batch_normalization enable, default=False"
    )
    parser.add_argument(
        "--debug", action='store_true', required=False,
        help="debug mode enable, default=False"
    )
    parser.print_help()
    # usage: python lib__argparse.py [-h] [--dtype DTYPE] [--dropout DROPOUT]
    #                                [--epoch EPOCH] [--batch_normalize]
    #                                [--debug]
    # 
    # train or test 'deep_cnn' model
    # 
    # options:
    #   -h, --help         show this help message and exit
    #   --dtype DTYPE      data-type for cnn parameters and inputs - float64(default), float32, float16
    #   --dropout DROPOUT  dropout_ratio, float [0.0, 1.0), default=0.0
    #   --epoch EPOCH      number of epochs for training, integer(>0), default=20
    #   --batch_normalize  batch_normalization enable, default=False
    #   --debug            debug mode enable, default=False
    # 
    # ----------- end of usage -------------

    arguments = "--dtype float32 --dropout 0.0 --epoch 10 --batch_normalize --debug".split()
    args = parser.parse_args(arguments)
    print('args=', args)
    # args= Namespace(dtype='float32', dropout=0.0, epoch=10, batch_normalize=True, debug=True)

    print("args.dtype=", args.dtype, type(args.dtype))
    print("args.dropout=", args.dropout, type(args.dropout))
    print("args.epoch=", args.epoch, type(args.epoch))
    print("args.batch_normalize=", args.batch_normalize, type(args.batch_normalize))
    print("args.debug=", args.debug, type(args.debug))
    # args.dtype= float32 <class 'str'>
    # args.dropout= 0.0 <class 'float'>
    # args.epoch= 10 <class 'int'>
    # args.batch_normalize= True <class 'bool'>
    # args.debug= True <class 'bool'>

    name = "deep_cnn-arch={}-dropout={:.1f}-epoch={:02d}"
    print(
        "\nfilename= " +
        f"deep_cnn-arch={args.dtype}-dropout={args.dropout:.1f}-" +
        f"epoch={args.epoch:02d}-" +
        f"batch_normalize={args.batch_normalize:d}-" +
        f"debug={args.debug:d}"
    )
    # filename= deep_cnn-arch=float32-dropout=0.0-epoch=10-batch_normalize=1-debug=1
