# vim: ft=python ts=4 sw=4 tw=999 expandtab
# ----------------------------------------------------------------------------
# File : lib__array.py
# Author : yc0325lee
# Created : 2022-03-19 16:02:54 by lee2103
# Modified : 2022-03-19 16:02:54 by lee2103
# Description : 
# ; array - efficient arrays of numeric values
# ; an object type which can compactly represent an array of basic values
#   -> characters, integers, floating point numbers
# ; value types and size are constrained(limitted)
#   +-----------+--------------------+-------------------+-----------------------+
#   | type code | c type             | python type       | minimum size in bytes |
#   +-----------+--------------------+-------------------+-----------------------+
#   | 'b'       | signed char        | int               | 1                     |
#   | 'B'       | unsigned char      | int               | 1                     |
#   | 'u'       | wchar_t            | Unicode character | 2                     |
#   | 'h'       | signed short       | int               | 2                     |
#   | 'H'       | unsigned short     | int               | 2                     |
#   | 'i'       | signed int         | int               | 2                     |
#   | 'I'       | unsigned int       | int               | 2                     |
#   | 'l'       | signed long        | int               | 4                     |
#   | 'L'       | unsigned long      | int               | 4                     |
#   | 'q'       | signed long long   | int               | 8                     |
#   | 'Q'       | unsigned long long | int               | 8                     |
#   | 'f'       | float              | float             | 4                     |
#   | 'd'       | double             | float             | 8                     |
#   +-----------+--------------------+-------------------+-----------------------+
#
# ----------------------------------------------------------------------------
import array

if False:
    symbols = 'abcdefghijklmnopqrstuvwxyz'
    codes = array.array('I', (ord(symbol) for symbol in symbols))
    # 'I' for unsigned int with 2 bytes

    print("type=", type(codes))
    print("array.array=", codes)

    for symbol, code in zip(symbols, codes):
        #print(f'simbol= {symbol}, code= {code}')
        print('simbol= {}, code= {:3d}'.format(symbol, code))

if False:
    # - class array.array(typecode[, initializer])
    # ; efficient arrays of numeric values
    # ; an object type which can compactly represent an array of basic values
    #   -> characters, integers, floating point numbers
    import random
    SIZE = 16

    doubles_0 = array.array('d', (random.random() for i in range(SIZE)))
    #                            --------------------------------------
    #                                     generator expression

    print("\n# doubles_0")
    for i, value in enumerate(doubles_0):
        print("value[{}]= {:.16f}".format(i, value))
    
    # writing to a file
    fileName = "doubles.dat"
    with open(fileName, 'wb') as outFile:
        print("\n[info] writing {} ...".format(fileName))
        doubles_0.tofile(outFile)

    # reading from a file
    doubles_1 = array.array('d')
    with open(fileName, 'rb') as inFile:
        print("\n[info] reading {} ...".format(fileName))
        doubles_1.fromfile(inFile, SIZE) # fast!

    print("\n# doubles_1")
    for i, value in enumerate(doubles_1):
        print("value[{}]= {:.16f}".format(i, value))

    print("[info] doubles_0 == doubles_1 -->", doubles_0 == doubles_1)
    print("[info] doubles_0.typecode=", doubles_0.typecode) # d(double)
    print("[info] doubles_1.typecode=", doubles_1.typecode) # d(double)

    # sorting
    doubles_2 = array.array(doubles_1.typecode, sorted(doubles_1))
    print("\n# doubles_2")
    for i, value in enumerate(doubles_2):
        print("value[{}]= {:.16f}".format(i, value))
