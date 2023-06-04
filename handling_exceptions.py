# vim: ft=python ts=4 sw=4 tw=999 expandtab
# ----------------------------------------------------------------------------
# File : handling_exceptions.py
# Author : yc0325lee
# Created : 2022-03-05 18:26:05 by lee2103
# Modified : 2022-03-05 18:26:05 by lee2103
# Description : 
# References
# - https://docs.python.org/2/library/exceptions.html#exception-hierarchy
# - https://wikidocs.net/30
# ----------------------------------------------------------------------------

# -------------------------------------
# exception handling
# - use 'try: ~ except: ~ else: ~' block!
# - Exception class hierarchy in python
#   ; https://docs.python.org/2/library/exceptions.html#exception-hierarchy
#
#     BaseException
#      +-- SystemExit
#      +-- KeyboardInterrupt
#      +-- GeneratorExit
#      +-- Exception
#           +-- StopIteration
#           +-- StandardError
#           |    +-- BufferError
#           |    +-- ArithmeticError
#           |    |    +-- FloatingPointError
#           |    |    +-- OverflowError
#           |    |    +-- ZeroDivisionError
#           |    +-- AssertionError
#           |    +-- AttributeError
#           |    +-- EnvironmentError
#           |    |    +-- IOError
#           |    |    +-- OSError
#           |    |         +-- WindowsError (Windows)
#           |    |         +-- VMSError (VMS)
#           |    +-- EOFError
#           |    +-- ImportError
#           |    +-- LookupError
#           |    |    +-- IndexError
#           |    |    +-- KeyError
#           |    +-- MemoryError
#           |    +-- NameError
#           |    |    +-- UnboundLocalError
#           |    +-- ReferenceError
#           |    +-- RuntimeError
#           |    |    +-- NotImplementedError
#           |    +-- SyntaxError
#           |    |    +-- IndentationError
#           |    |         +-- TabError
#           |    +-- SystemError
#           |    +-- TypeError
#           |    +-- ValueError
#           |         +-- UnicodeError
#           |              +-- UnicodeDecodeError
#           |              +-- UnicodeEncodeError
#           |              +-- UnicodeTranslateError
#           +-- Warning
#                +-- DeprecationWarning
#                +-- PendingDeprecationWarning
#                +-- RuntimeWarning
#                +-- SyntaxWarning
#                +-- UserWarning
#                +-- FutureWarning
#                +-- ImportWarning
#                +-- UnicodeWarning
#                +-- BytesWarning

# usages
# try:
#     ...
# except errtype:
#     ...
# 
# try:
#     ...
# except errtype as msg:
#     ...
# 
# try:
#     ...
# except errtype as msg: # -> upon error
#     ...
# else: # -> upon no error
#     ...
# 
# try:
#     ...
# except errtype as msg:
#     ...
# finally:
#     ...
# 
# try:
#     ...
# except err1 as msg:
#     ...
# except err2 as msg:
#     ...
# except err3 as msg:
#     ...
# 
# try:
#     ...
# except (err1, err2, err3) as msg:
#     ...



if False:
    # raising error - user-defined exception
    class UserDefinedErr(Exception):
        def __init__(self, msg):
            self.msg = msg
        def __str__(self):
            return self.msg

    try:
        num1 = 64
        num2 = 9
        if num1 >= 10 or num2 >= 10:
            raise UserDefinedErr("input num1= {0}, num2= {1}".format(num1,num2))
        print("{0} / {1] = {2}".format(num1, num2, int(num1/num2)))
    except UserDefinedErr as err:
        print("[err ] wrong input value!")
        print("       message=", err)
    finally:
        print("[info] end of execution...")

if False:
    # IndexError
    items = [ 0, 1, 2 ]
    try:
        print("item[%d] = %d" % (0, items[0]))
        print("item[%d] = %d" % (1, items[1]))
        print("item[%d] = %d" % (2, items[2]))
        print("item[%d] = %d" % (3, items[3]))
    except Exception as err:
        print("[err ] something's wrong!")
        print("       message= ", err)
    else:
        print("[info] there was no exception here!")

if False:
    # ZeroDivisionError
    dividend = 8;
    divisor = 0;
    try:
        result = dividend / divisor;
    except Exception as err:
        print("[err ] something's wrong!")
        print("       message= ", err)
    else:
        print("[info] result= ", result)

# FileNotFoundError
if False:
    try:
        inFile = open("somefile.txt", "r") # somefile.txt not exist
    except FileNotFoundError as err:
        print(err) # [Errno 2] No such file or directory: 'somefile.txt'
    finally:
        print("[info] end of execution...")

if False:
    # NotImplementedError
    # ; forcing exception -> 'raise'
    def do_something():
        raise NotImplementedError("function not implemented")
    do_something()

