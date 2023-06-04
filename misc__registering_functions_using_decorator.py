#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : misc__registering_functions_using_decorator.py
# - author : yc0325lee
# - created : 2022-12-04 19:02:07 by yc032
# - modified : 2022-12-04 19:02:07 by yc032
# - description : 
# ----------------------------------------------------------------------------

# - example 7-23. to accept parameters, the new register decorator must be
#   called as a function
# - set.discard(elem)
# ; remove element elem from the set if it is present.
registry = set()

# register() -> decorator factory, returns decorator function
# decorate() is a real decorator.
def register(active=True):
    # 'active' is free variable in this closure!
    def decorate(func):
        if active:
            print('[dbg ] adding function %s on registry ...' % (func.__name__))
            registry.add(func)
        else:
            if func in registry:
                print('[dbg ] discarding function %s from registry ...' % (func.__name__))
                registry.discard(func)
        return func
    return decorate

@register(active=False) # register(active=False) -> returns decorator!
def f1():
    print('running f1()')

@register() 
def f2():
    print('running f2()')

@register() 
def f3():
    print('running f3()')

@register() 
def f4():
    print('running f3()')

print('running main()')
print("functions registered = {", ', '.join(func.__name__ for func in registry), "}")
for func in registry:
    func()

# add_func and remove_func are decorators
add_func = register(active=True)
remove_func = register(active=False)

add_func(f1)
print("functions registered = {", ', '.join(func.__name__ for func in registry), "}")

remove_func(f1)
remove_func(f2)
remove_func(f3)
remove_func(f4)
print("functions registered = {", ', '.join(func.__name__ for func in registry), "}")

remove_func(f1)
remove_func(f2)
remove_func(f3)
remove_func(f4)
