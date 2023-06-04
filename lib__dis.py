# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : lib__dis.py
# - author : yc0325lee
# - created : 2022-10-15 20:00:14 by lee2103
# - modified : 2022-10-15 20:00:14 by lee2103
# - description : 
# ; disassembler for python bytecode
# ; the dis module supports the analysis of cpython bytecode by disassembling it.
# ----------------------------------------------------------------------------
import dis

if True:
    # -------------------------------------
    # - dis.dis(code_string)
    # ; return a formatted view of the bytecode operations (the same as printed
    #   by dis.dis(), but returned as a multi-line string).
    cont = (1, 2, [30, 40])
    print('cont=', cont)

    dis.dis('cont[2] += [50, 60]') # for debugging

    # dis.dis('t[2] += [50, 60]') # for debugging
    #  1           0 LOAD_NAME        0 (t)
    #              2 LOAD_CONST       0 (2)
    #              4 DUP_TOP_TWO
    #              6 BINARY_SUBSCR
    #              8 LOAD_CONST       1 (50)
    #             10 LOAD_CONST       2 (60)
    #             12 BUILD_LIST       2
    #             14 INPLACE_ADD
    #             16 ROT_THREE
    #             18 STORE_SUBSCR     *** trying to modify an element of tuple!!! ***
    #             20 LOAD_CONST       3 (None)
    #             22 RETURN_VALUE

    # let's catch the exception while trying to do this.
    try:
        cont[2] += [50, 60] # [question] is it possible to modify this?
    except Exception as err:
        print('[error]', err)

    print('cont=', cont)
    # cont= (1, 2, [30, 40, 50, 60])
    # -> anyway modified!
