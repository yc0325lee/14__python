# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : oop__methods_for_operator_overloading.py
# - author : yc0325lee
# - created : 2022-11-04 23:20:04 by lee2103
# - modified : 2022-11-04 23:20:04 by lee2103
# - description : 
# ----------------------------------------------------------------------------

# infix(binary) operators
# ; reverse methods invoked when the initial method call returns 'NotImplemented'
# ; if a class does not implement the in-place operators listed,
#   the augmented assignment operators are just syntactic sugar:
#   a += b is evaluated exactly as a = a + b.
# ; that’s the expected behavior for immutable types, and if you have __add__
#   then += will work with no additional code.
# ; 
# +----------+--------------+---------------+---------------+---------------------------------+
# | operator | forward      | reverse       | in-place      | description                     |
# +----------+--------------+---------------+---------------+---------------------------------+
# | +        | __add__      | __radd__      | __iadd__      | Addition or concatenation       |
# | -        | __sub__      | __rsub__      | __isub__      | Subtraction                     |
# | *        | __mul__      | __rmul__      | __imul__      | Multiplication or repetition    |
# | /        | __truediv__  | __rtruediv__  | __itruediv__  | True division                   |
# | //       | __floordiv__ | __rfloordiv__ | __ifloordiv__ | Floor division                  |
# | %        | __mod__      | __rmod__      | __imod__      | Modulo                          |
# | divmod() | __divmod__   | __rdivmod__   | __idivmod__   | Returns tuple of floor division |
# |          |              |               |               | quotient and modulo             |
# | **-pow() | __pow__      | __rpow__      | __ipow__      | Exponentiation                  |
# | @        | __matmul__   | __rmatmul__   | __imatmul__   | Matrix multiplication           |
# | &        | __and__      | __rand__      | __iand__      | Bitwise and                     |
# | |        | __or__       | __ror__       | __ior__       | Bitwise or                      |
# | ^        | __xor__      | __rxor__      | __ixor__      | Bitwise xor                     |
# | <<       | __lshift__   | __rlshift__   | __ilshift__   | Bitwise shift left              |
# | >>       | __rshift__   | __rrshift__   | __irshift__   | Bitwise shift right             |
# +----------+--------------+---------------+---------------+---------------------------------+

if False:
    # '+' vs. '+='
    # ; __add__ vs __iadd__(in-place add)
    # ; __add__()
    #   the result is produced by calling the constructor to build a new
    #   instance.
    # ; __iadd__()
    #   the result is produced by returning self, after it has been modified.
    a = [1, 2, 3]
    b = [4, 5, 6]
    print('a =', a, id(a))
    print('b =', b, id(b))
    y = a + b # y = list.__add__(a, b)
    print('a + b =', y, id(y))
    a += b # list.__iadd__(a, b)
    print('a += b --->', a, id(a))
    # --------------------------------------------
    # a = [1, 2, 3]                  2339314240640
    # b = [4, 5, 6]                  2339315232896
    # a + b = [1, 2, 3, 4, 5, 6]     2339315804352
    # a += b ---> [1, 2, 3, 4, 5, 6] 2339314240640
    # --------------------------------------------



# comparison operators
# ; reverse methods invoked when the initial method call returns 'NotImplemented'
# +----------+----------------+---------------------+---------------------+-----------------------+
# | group    | infix operator | forward method call | reverse method call | fall back             |
# +----------+----------------+---------------------+---------------------+-----------------------+
# | equality | a == b         | a.__eq__(b)         | b.__eq__(a)         | return id(a) == id(b) |
# | equality | a != b         | a.__ne__(b)         | b.__ne__(a)         | return not (a == b)   |
# | ordering | a > b          | a.__gt__(b)         | b.__lt__(a)         | raise TypeError       |
# | ordering | a < b          | a.__lt__(b)         | b.__gt__(a)         | raise TypeError       |
# | ordering | a >= b         | a.__ge__(b)         | b.__le__(a)         | raise TypeError       |
# | ordering | a <= b         | a.__le__(b)         | b.__ge__(a)         | raise TypeError       |
# +----------+----------------+---------------------+---------------------+-----------------------+
