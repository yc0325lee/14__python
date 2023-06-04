# vim: ft=python ts=4 sw=4 tw=78 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : misc__function_decorator.py
# - author : yc0325lee
# - created : 2022-10-16 23:48:06 by lee2103
# - modified : 2022-10-16 23:48:06 by lee2103
# - description : 
# - decorator
# ; a function returning another function, usually applied as a function
#   transformation using the @wrapper syntax.
# ; attach additional responsibilities to an object dynamically
# ----------------------------------------------------------------------------

if False:
    import time
    import functools

    # - decorator for debugging
    def debug(func):
        @functools.wraps(func) # func's attributes preserved
        def wrapper(*args, **kwargs):
            arglist = []
            if args:
                arglist.append(', '.join(repr(arg) for arg in args))
            if kwargs:
                pairs = ['%s=%r' % (k, v) for k, v in sorted(kwargs.items())]
                arglist.append(', '.join(pairs))
            arg_str = ', '.join(arglist)
            print("[dgb ] {}({}) invoked ...".format(func.__name__, arg_str))
            start_ = time.perf_counter()
            result = func(*args, **kwargs)
            end_ = time.perf_counter()
            elapsed_ = end_ - start_
            if True:
                print("[dgb ] {}() ends ... elapsed= {:.8fs}"
                        .format(func.__name__, elapsed_))
            return result
        return wrapper # decorated-func

    # - with 'active' option
    # ; decorator factory should return a real decorator!
    def debug(active=True):
        '''this function returns a decorator - debug()'''
        def debug_inner(func):
            '''this is the real decorator'''
            @functools.wraps(func) # func's attributes preserved
            def wrapper(*args, **kwargs):
                arglist = []
                if args:
                    arglist.append(', '.join(repr(arg) for arg in args))
                if kwargs:
                    pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
                    arglist.append(', '.join(pairs))
                arg_str = ', '.join(arglist)

                if active:
                    print("[dgb ] {}({}) invoked ...".format(func.__name__, arg_str))
                    start_ = time.perf_counter()

                result = func(*args, **kwargs)

                if active:
                    end_ = time.perf_counter()
                    elapsed_ = end_ - start_
                    print("[dgb ] {}() ends ... elapsed= {:.8fs}"
                            .format(func.__name__, elapsed_))

                return result
            return wrapper # decorated-func
        return debug_inner

# (1)
if False:
    def trace(func):                      # 호출할 함수를 매개변수로 받음
        def wrapper():                    # 호출할 함수를 감싸는 함수
            print(func.__name__, 'start') # __name__으로 함수 이름 출력
            func()                        # 매개변수로 받은 함수를 호출
            print(func.__name__, 'end')
        return wrapper                    # wrapper 함수 반환
     
    def hello():
        print('hello is running ...')
     
    def world():
        print('world is running ...')
    
     
    trace_hello = trace(hello)    # 데코레이터에 호출할 함수를 넣음
    trace_hello()                 # 반환된 함수를 호출
    
    trace_world = trace(world)    # 데코레이터에 호출할 함수를 넣음
    trace_world()                 # 반환된 함수를 호출


# (2)
if False:
    def trace(func):                      # 호출할 함수를 매개변수로 받음
        def wrapper():                    # 호출할 함수를 감싸는 함수
            print(func.__name__, 'start') # __name__으로 함수 이름 출력
            func()                        # 매개변수로 받은 함수를 호출
            print(func.__name__, 'end')
        return wrapper                    # wrapper 함수 반환
     
    @trace
    def hello(): # hello = trace(hello)
        print('hello is running ...')
     
    @trace
    def world(): # world = trace(world)
        print('world is running ...')
    
    hello()
    world()

# (2-1) 'active' parameters
# ; requires 1 more level of nested structure
# ; trace() here is a decorator factory
if True:
    def trace(active=True):
        def trace_inner(func):                           # 호출할 함수를 매개변수로 받음
            def wrapper():                               # 호출할 함수를 감싸는 함수
                if active: print(func.__name__, 'start') # __name__으로 함수 이름 출력
                func()                                   # 매개변수로 받은 함수를 호출
                if active: print(func.__name__, 'end')
            return wrapper                               # wrapper 함수 반환
        return trace_inner
     
    @trace(True)
    def hello(): # hello = trace(hello)
        print('hello is running ...')
     
    @trace(False)
    def world(): # world = trace(world)
        print('world is running ...')
    
    hello()
    world()


# (3) multiple decorator
if False:
    def decorator1(func):
        def wrapper():
            print("[info] decorator1 ...")
            func()
        return wrapper
     
    def decorator2(func):
        def wrapper():
            print("[info] decorator2 ...")
            func()
        return wrapper
     
    @decorator1
    @decorator2
    def hello():
        print('[info] hello is running ...')

    hello()

    # same as the following
    def world():
        print('[info] world is running ...')

    world = decorator1(decorator2(world))

    world()


# (3)
if False:
    def trace(func):          # 호출할 함수를 매개변수로 받음
        def wrapper(a, b):    # 호출할 함수 add(a, b)의 매개변수와 똑같이 지정
            r = func(a, b)    # func에 매개변수 a, b를 넣어서 호출하고 반환값을 변수에 저장
            print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r)) # 매개변수와 반환값 출력
            return r          # func의 반환값을 반환
        return wrapper        # wrapper 함수 반환

    @trace
    def add(a, b):
        return a + b

    print("result=", add(10,20))


# (4) decorator with arguments
if False:
    def is_multiple(x):           # 데코레이터가 사용할 매개변수를 지정
        def real_decorator(func): # 호출할 함수를 매개변수로 받음
            def wrapper(a, b):    # 호출할 함수의 매개변수와 똑같이 지정
                r = func(a, b)    # func를 호출하고 반환값을 변수에 저장
                if r % x == 0:    # func의 반환값이 x의 배수인지 확인
                    print("{0}'s return value is multiple of {1}.".format(func.__name__, x))
                else:
                    print("{0}'s return value is not multiple of {1}.".format(func.__name__, x))
                return r             # func의 반환값을 반환
            return wrapper           # wrapper 함수 반환
        return real_decorator        # real_decorator 함수 반환

    @is_multiple(3)
    def add(a, b):
        return a + b

    print("result=", add(10,20))
    print("result=", add(3,4))


