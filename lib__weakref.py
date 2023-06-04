# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : lib__weakref.py
# - author : yc0325lee
# - created : 2022-10-10 16:39:29 by lee2103
# - modified : 2022-10-10 16:39:29 by lee2103
# - description : 
#  ; referent means the object which is referred to by a weak reference.
#  ; weak references to an object do not increase its reference count.
#  ; weakkeydictionary, weakvaluedictionary and weakset use 'weakref'
# ----------------------------------------------------------------------------
import weakref


if False:
    def bye():
        print("[info] object is being destroyed ...")

    s1 = {1, 2, 3}
    s2 = s1

    ender = weakref.finalize(s1, bye)
    if ender.alive:
        print("[info] object is still alive ...")

    del s1
    if ender.alive:
        print("[info] object is still alive ...")

    s2 = [1, 2, 3] # 's2' refers to another object,
                   # so '{1, 2, 3}' should be garbage collected.
    print("[info] end of program ...")


if True:
    # class weakref.ref(object[, callback])
    # ; return a weak reference to object.
    # ; the original object can be retrieved by calling the reference object
    #   if the referent is still alive
    # ; if the referent is no longer alive, calling the reference object
    #   will cause 'None' to be returned.
    def bye(ref):
        print("[info] object referred by {} is being destroyed ...".format(ref))

    a = {0, 1}
    weak = weakref.ref(a, bye)
    print("weak=", weak)
    print("weak()=", weak())
    for attr in dir(weak):
        print(attr)
    print()

    a = {2, 3, 4} # '{0, 1}' is destroyed and bye() is invoked
    print("weak=", weak)
    print("weak()=", weak()) # None


