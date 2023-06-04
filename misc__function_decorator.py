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
    def trace(func):                      # ȣ���� �Լ��� �Ű������� ����
        def wrapper():                    # ȣ���� �Լ��� ���δ� �Լ�
            print(func.__name__, 'start') # __name__���� �Լ� �̸� ���
            func()                        # �Ű������� ���� �Լ��� ȣ��
            print(func.__name__, 'end')
        return wrapper                    # wrapper �Լ� ��ȯ
     
    def hello():
        print('hello is running ...')
     
    def world():
        print('world is running ...')
    
     
    trace_hello = trace(hello)    # ���ڷ����Ϳ� ȣ���� �Լ��� ����
    trace_hello()                 # ��ȯ�� �Լ��� ȣ��
    
    trace_world = trace(world)    # ���ڷ����Ϳ� ȣ���� �Լ��� ����
    trace_world()                 # ��ȯ�� �Լ��� ȣ��


# (2)
if False:
    def trace(func):                      # ȣ���� �Լ��� �Ű������� ����
        def wrapper():                    # ȣ���� �Լ��� ���δ� �Լ�
            print(func.__name__, 'start') # __name__���� �Լ� �̸� ���
            func()                        # �Ű������� ���� �Լ��� ȣ��
            print(func.__name__, 'end')
        return wrapper                    # wrapper �Լ� ��ȯ
     
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
        def trace_inner(func):                           # ȣ���� �Լ��� �Ű������� ����
            def wrapper():                               # ȣ���� �Լ��� ���δ� �Լ�
                if active: print(func.__name__, 'start') # __name__���� �Լ� �̸� ���
                func()                                   # �Ű������� ���� �Լ��� ȣ��
                if active: print(func.__name__, 'end')
            return wrapper                               # wrapper �Լ� ��ȯ
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
    def trace(func):          # ȣ���� �Լ��� �Ű������� ����
        def wrapper(a, b):    # ȣ���� �Լ� add(a, b)�� �Ű������� �Ȱ��� ����
            r = func(a, b)    # func�� �Ű����� a, b�� �־ ȣ���ϰ� ��ȯ���� ������ ����
            print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r)) # �Ű������� ��ȯ�� ���
            return r          # func�� ��ȯ���� ��ȯ
        return wrapper        # wrapper �Լ� ��ȯ

    @trace
    def add(a, b):
        return a + b

    print("result=", add(10,20))


# (4) decorator with arguments
if False:
    def is_multiple(x):           # ���ڷ����Ͱ� ����� �Ű������� ����
        def real_decorator(func): # ȣ���� �Լ��� �Ű������� ����
            def wrapper(a, b):    # ȣ���� �Լ��� �Ű������� �Ȱ��� ����
                r = func(a, b)    # func�� ȣ���ϰ� ��ȯ���� ������ ����
                if r % x == 0:    # func�� ��ȯ���� x�� ������� Ȯ��
                    print("{0}'s return value is multiple of {1}.".format(func.__name__, x))
                else:
                    print("{0}'s return value is not multiple of {1}.".format(func.__name__, x))
                return r             # func�� ��ȯ���� ��ȯ
            return wrapper           # wrapper �Լ� ��ȯ
        return real_decorator        # real_decorator �Լ� ��ȯ

    @is_multiple(3)
    def add(a, b):
        return a + b

    print("result=", add(10,20))
    print("result=", add(3,4))


