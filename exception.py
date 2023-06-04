# vim: ft=python ts=4 sw=4 tw=999 expandtab
# ----------------------------------------------------------------------------
# File : exception.py
# Description : 
# Author : yc0325lee
# Created : 2021-06-27 20:59:46 by lee2103
# Modified : 2021-06-27 20:59:46 by lee2103
# ----------------------------------------------------------------------------

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
    print("[info] it's ok!")


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


# raising error - user-defined exception
class SpecialError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    num1 = 64
    num2 = 9

    if num1 >= 10 or num2 >= 10:
        raise SpecialError("input num1= {0}, num2= {1}".format(num1,num2))

    print("{0} / {1] = {2}".format(num1, num2, int(num1/num2)))

except SpecialError as err:
    print("[err ] wrong value on input!")
    print("       message=", err)
finally:
    print("[info] end of execution...")
