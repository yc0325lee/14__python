# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : double_underscore_object_readonly_attrs.py
# - author : yc0325lee
# - created : 2022-10-10 20:51:29 by lee2103
# - modified : 2022-10-10 20:51:29 by lee2103
# - description : 
# ----------------------------------------------------------------------------
if False:
    # - original version
    class Vector2d:
        typecode = 'd' # class attribute

        def __init__(self, x, y):
            self.x = float(x)
            self.y = float(y)

        def __iter__(self):
            return (i for i in (self.x, self.y)) # comprehension

        pass


if True:
    # - modified vesion
    # (1) double underscores -> private attributes
    # (2) @property decorators for getter method
    # (3) self.__x -> x() getter
    # - this will be ok as long as derived classes access 'x' and 'y'
    #   for read-only attributes.
    class Vector2d:
        typecode = 'd' # class attribute

        def __init__(self, x, y):
            self.__x = float(x)
            self.__y = float(y)

        @property
        def x(self):
            return self.__x

        @property
        def y(self):
            return self.__y

        def __iter__(self):
            return (i for i in (self.x, self.y)) # comprehension

        pass


    v = Vector2d(3, 4)
    print("v= ", v)

    print('v.x =', v.x) # -> this is ok!
    print('v.y =', v.y) #    (read-only)

    v.x = 5.0 # AttributeError: can't set attribute
    v.y = 6.0
