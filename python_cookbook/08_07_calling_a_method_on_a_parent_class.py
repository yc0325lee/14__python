#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 08_07_calling_a_method_on_a_parent_class.py
# - author : yc0325lee
# - created : 2022-11-22 20:52:04 by yc032
# - modified : 2022-11-22 20:52:04 by yc032
# - description : 
# ; how to invoke overidden method explicitly
# ; class super([type[, object-or-type]])
#   return a proxy object that delegates method calls to a parent or sibling
#   class of type.
#   this is useful for accessing inherited methods that have been overridden
#   in a class.
# ----------------------------------------------------------------------------

if False:
    # - invoking a method in parent class
    class A:
        def spam(self):
            print('[dbg ] A.spam')


    class B(A):
        def spam(self):
            print('[dbg ] B.spam')
            super().spam()

    b = B()
    b.spam()


if False:
    # - taking care of initializing parent class when inheriting
    class A:
        def __init__(self):
            print('[dbg ] A.__init__() invoked ...')
            self.x = 0

    class B(A):
        def __init__(self):
            print('[dbg ] B.__init__() invoked ...')
            super().__init__()
            self.y = 1

    b = B()
    print('b.__dict__ =', b.__dict__)
    # [dbg ] B.__init__() invoked ...
    # [dbg ] A.__init__() invoked ...
    # b.__dict__ = {'x': 0, 'y': 1}


if False:
    # proxy class hold some other instance of a class
    class Proxy:
        def __init__(self, obj):
            self._obj = obj

        # Delegate attribute lookup to internal obj
        def __getattr__(self, name):
            return getattr(self._obj, name)
     
        # Delegate attribute assignment
        def __setattr__(self, name, value):
            if name.startswith('_'):
                super().__setattr__(name, value) # Call original __setattr__
            else:
                setattr(self._obj, name, value)


if False:
    class Base:
        def __init__(self):
            print('[dbg ] Base.__init__')

    class A(Base):
        def __init__(self):
            Base.__init__(self)
            print('[dbg ] A.__init__')

            
    class B(Base):
        def __init__(self):
            Base.__init__(self)
            print('[dbg ] B.__init__')

            
    class C(A, B):
        def __init__(self):
            A.__init__(self)
            B.__init__(self)
            print('[dbg ] C.__init__')

    c = C()
    # [dbg ] Base.__init__
    # [dbg ] A.__init__
    # [dbg ] Base.__init__ *** Base.__init__ invoked twice!!! ***
    # [dbg ] B.__init__
    # [dbg ] C.__init__


if False:
    # - properly initializing base classes using super()
    class Base:
        def __init__(self):
            print('[dbg ] Base.__init__')

    class A(Base):
        def __init__(self):
            super().__init__()
            print('[dbg ] A.__init__')

    class B(Base):
        def __init__(self):
            super().__init__()
            print('[dbg ] B.__init__')

    class C(A, B):
        def __init__(self):
            super().__init__() # only one call to super() here
            print('[dbg ] C.__init__')

    c = C()
    # [dbg ] Base.__init__
    # [dbg ] B.__init__
    # [dbg ] A.__init__
    # [dbg ] C.__init__

    print('C.__mro__ =', C.__mro__)
    # ------------------------------------------------------------
    # - MRO(Method Resolution Order)
    # C.__mro__ = ( <class '__main__.C'>, <class '__main__.A'>,
    #               <class '__main__.B'>, <class '__main__.Base'>,
    #               <class 'object'>
    #             )
    # ------------------------------------------------------------
    # - child classes get checked before parents
    # - multiple parents get checked in the order listed.
    # - if there are two valid choices for the next class, pick the one from
    #   the first parent.
    # ------------------------------------------------------------


if True:
    # - focus. here is a special case!
    class A:
        def spam(self):
            print('[dbg ] A.spam')
            super().spam() # what will be done?
                           # next sibling's will be checked and invoked!

    class B:
        def spam(self):
            print('[dbg ] B.spam')

    class C(A,B):
        pass

    c = C()
    c.spam()
    print('C.__mro__ =', C.__mro__)
    # <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>
    #                       --------------------  ----------+---------
    #                                                       |
    #                           super().spam() -------------+
