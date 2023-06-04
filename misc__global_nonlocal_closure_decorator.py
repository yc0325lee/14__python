#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : misc__global_nonlocal_closure.py
# - author : yc0325lee
# - created : 2022-10-16 23:56:15 by lee2103
# - modified : 2022-10-16 23:56:15 by lee2103
# - references
# ; https://shoark7.github.io/programming/python/closure-in-python
# ; https://en.wikipedia.org/wiki/First-class_citizen
# - description : 
# ; netsted function definition is allowed like nested if structure
# ; function is 'first class object(citizen)' in python
# ; scopes -> global, nonlocal, local
#   global & nonlocal -> read-only access, write not allowed
# ----------------------------------------------------------------------------


# -------------------------------------
# - global scope vs nonlocal scope
#
# outer(), inner() 함수 입장에서 전역(global) 범위
# def outer():
#     # outer() 함수 입장에서 지역(local) 범위
#     # inner() 함수 입장에서 비지역(nonlocal) 범위
#     def inner():
#         # inner 함수 입장에서 지역(local) 범위
#         pass


# -------------------------------------
# - global statement
# ; global id0, id1, ...
# ; the global statement is a declaration which holds for the entire current
#   code block. it means that the listed identifiers are to be interpreted as
#   globals.
if False:
    b = 6 # global scope
    def f3(a):
        global b # 'b' can be modified inside function f3()
        print("a=", a)
        print("b=", b) # 6 -> ok, just reading...
        print("f3() is modifying global::b ...")

        b += 3
        # trying to modify variable in global scope
        # ; error without global statement
        #   -> UnboundLocalError: local variable 'b' referenced
        #      before assignment

    f3(3)
    print("global::b=", b)
    # global::b= 9


# -------------------------------------
# - nonlocal statement
# ; nonlocal id0, id1, ...
# ; the nonlocal statement causes the listed identifiers to refer to previously
#   bound variables in the nearest enclosing scope excluding globals.
# ; it is possible nonlocal variables be modified in local scope
if False:
    z = 3 # global scope of 'inner'
    def outer(x):
        y = 10 # nonlocal scope of 'inner'
        def inner():
            x = 1000
            return x # local scope
        return inner()

    print(outer(10)) # print local 'x' -> 1000

if False:
    def count(x):
        def increment():
            nonlocal x  # x가 로컬이 아닌 nonlocal의 변수임을 확인한다.
            x += 1 # ok!
            print(x)

        increment()

    count(5) # prints '6'

# -------------------------------------
# - closure
# ; a closure is a function object that remembers values in enclosing scopes
#   even if they are not present in memory.
# - 자신을 둘러싼 스코프(네임스페이스)의 상태값을 기억하는 함수
#  ; 해당 함수는 어떤 함수 내의 중첩된 함수여야 한다.
#  ; 해당 함수는 자신을 둘러싼(enclose) 함수 내의 상태값을 반드시 참조해야 한다.
#  ; 해당 함수를 둘러싼 함수는 이 함수를 반환해야 한다.
if False:
    def in_cache(func):
        cache = {} # dict
        def wrapper(n):
            print("[debug] {}.cache=".format(func.__name__), cache) ## !!!!
            if n in cache:
                return cache[n]
            else:
                cache[n] = func(n) # register new-value
                return cache[n]
        return wrapper

    # wrapper function meets all conditions to be a closure!

    def factorialN(n):
        ret = 1
        for i in range(1, n+1): # 1, 2, 3, ..., n
            ret *= i
        return ret

    def sumN(n):
        sum = 0
        for i in range(n+1):
            sum += i
        return sum

    factorialN = in_cache(factorialN)
    # now factorialN(with nonlocal cached) stores previous result.
    # -> closure!

    for n in range(11):
        print("factorialN({}) = ".format(n), factorialN(n))
    # [debug] factorialN.cache= {}
    # [debug] factorialN.cache= {0: 1}
    # [debug] factorialN.cache= {0: 1, 1: 1}
    # [debug] factorialN.cache= {0: 1, 1: 1, 2: 2}
    # [debug] factorialN.cache= {0: 1, 1: 1, 2: 2, 3: 6}
    # [debug] factorialN.cache= {0: 1, 1: 1, 2: 2, 3: 6, 4: 24}
    # [debug] factorialN.cache= {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120}
    # [debug] factorialN.cache= {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720}
    # [debug] factorialN.cache= {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040}
    # [debug] factorialN.cache= {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320}
    # [debug] factorialN.cache= {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}


    sumN = in_cache(sumN)
    # now sumN(cached) stores previous result.
    # -> closure!

                 # --------------------------------------
    del in_cache # in_cache function deleted!
                 # but closures still contain everything!
                 # --------------------------------------

    for n in range(11):
        print("sumN({}) = ".format(n), sumN(n))
    # [debug] sumN.cache= {0: 0}
    # [debug] sumN.cache= {0: 0, 1: 1}
    # [debug] sumN.cache= {0: 0, 1: 1, 2: 3}
    # [debug] sumN.cache= {0: 0, 1: 1, 2: 3, 3: 6}
    # [debug] sumN.cache= {0: 0, 1: 1, 2: 3, 3: 6, 4: 10}
    # [debug] sumN.cache= {0: 0, 1: 1, 2: 3, 3: 6, 4: 10, 5: 15}
    # [debug] sumN.cache= {0: 0, 1: 1, 2: 3, 3: 6, 4: 10, 5: 15, 6: 21}
    # [debug] sumN.cache= {0: 0, 1: 1, 2: 3, 3: 6, 4: 10, 5: 15, 6: 21, 7: 28}
    # [debug] sumN.cache= {0: 0, 1: 1, 2: 3, 3: 6, 4: 10, 5: 15, 6: 21, 7: 28, 8: 36}
    # [debug] sumN.cache= {0: 0, 1: 1, 2: 3, 3: 6, 4: 10, 5: 15, 6: 21, 7: 28, 8: 36, 9: 45}

    # debugging information
    print(factorialN.__closure__) # tuple
    for item in factorialN.__closure__:
        print(item.cell_contents)
    # {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880, 10: 3628800}
    # <function factorialN at 0x0000028A6CD08F40>

if False:
    # - decorator does the same thing!
    # ; attach additional responsibilities to an object
    #   dynamically(import-time)
    def in_cache(func):
        cache = {} # dict
        def wrapper(n):
            print("[debug] {}.cache=".format(func.__name__), cache) ## !!!!
            if n in cache:
                return cache[n]
            else:
                cache[n] = func(n) # register new-value
                return cache[n]
        return wrapper

    @in_cache # decorator, factorialN = in_cache(factorialN)
    def factorialN(n):
        ret = 1
        for i in range(1, n+1):
            ret *= i
        return ret

    @in_cache # decorator, sumN = in_cache(sumN)
    def sumN(n):
        sum = 0
        for i in range(n+1):
            sum += i
        return sum

                 # --------------------------------------
    del in_cache # 'in_cache' function deleted!
                 # but closures are still alive!
                 # --------------------------------------

    # now factorialN() and sumN() are closures!
    for n in range(11):
        print("factorialN({}) = ".format(n), factorialN(n))

    for n in range(11):
        print("sumN({}) = ".format(n), sumN(n))

    # debugging information
    print(factorialN.__closure__) # tuple
    for item in factorialN.__closure__:
        print(item.cell_contents)
    # {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880, 10: 3628800}
    # <function factorialN at 0x0000028A6CD08F40>
