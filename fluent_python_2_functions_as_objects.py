#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : fluent_python_3_functions_as_objects.py
# - author : yc0325lee
# - created : 2022-11-29 23:54:30 by yc032
# - modified : 2022-11-29 23:54:30 by yc032
# - description : 
# 7. functions as first-class objects
# 8. type hints in functions
# 9. decorators and closures
# 10. design patterns with first-class functions
# ----------------------------------------------------------------------------


# -------------------------------------
# chapter 5: first-class functions

# first-class object
# - created at runtime
# - assigned to a variable or element in a data structure
# - passed as an argument to a function
# - returned as the result of a function
# - integers, strings, lists and dictionaries are first-class objects.

if False:
    # - a first-class object is an entity
    #   within a programming language that can:
    #   (1) appear in an expression
    #   (2) be assigned to a variable
    #   (3) be used as an argument
    #   (4) be returned by a function call
    def add(a, b):
        return a + b

    def execute(func, *args):
        return func(*args) # (3)

    op = add # (2)

    execute(op, 3, 5) # (1)


if False:
    # - factorial example
    # ; function is first-class object in python
    def factorial(n): 
        '''factorial(n) returns n!'''
        return 1 if n < 2 else n * factorial(n-1)

    print(factorial(10))
    print(factorial)
    print(factorial.__doc__) # docstring

    func = factorial # assigned to a variable
    print("func=", func)
    print("func(5)=", func(5))

    # passing function object to another function
    for result in map(func, range(10)):
        print("result=", result)

if False:
    # higher-order functions
    # ; a function that takes a function as argument or
    #   returns a function as the result
    # ; map, filter, reduce, ...
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits, key=len))

if False:
    # modern replacements for map, filter, and reduce
    def factorial(n): 
        return 1 if n < 2 else n * factorial(n-1)
    
    print( list(map(factorial, range(6))) ) # map

    print( [factorial(n) for n in range(6)] ) # list comprehension

    print( list(map(factorial, filter(lambda n: n % 2, range(6)))) ) # map

    print( [factorial(n) for n in range(6) if n % 2] ) # list comprehension
    # [1, 1, 2, 6, 24, 120]
    # [1, 6, 120]

    # adding up to 100
    from functools import reduce
    from operator import add
    print("sum=", reduce(add, range(1, 101, 1))) # sum= 5050

if False:
    # anonymous function - lambda
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

    def criteria(word):
        return ''.join(reversed(word))

    print(sorted(fruits, key=criteria))
    print()
    print(sorted(fruits, key=lambda word: word[::-1]))
    #                        -----------------------
    #                        anonymous function using lambda


if False:
    # ------------------------------------------------------------------------
    # - the seven flavors of callable objects
    # ; object + call-operator -> invokes some functionality
    # ; object() or object(*args)
    # (1) user-defined functions
    #     created with def statements or lambda expressions.
    # (2) built-in functions
    #     a function implemented in c (for cpython), like len or time.strftime.
    # (3) built-in methods
    #     methods implemented in c, like dict.get.
    # (4) methods
    #     functions defined in the body of a class.
    # (5) classes
    #     __new__ when creating an instance and __init__
    # (6) class instances
    #     when __call__ method is defined and invoked by instance() 
    # (7) generator functions
    #     functions with 'yield'
    # ------------------------------------------------------------------------

    # checking if an object is callable
    for obj in (abs, str, 13, 'aaa'):
        print("{} -> callable? {}".format(obj, callable(obj)))

    # <built-in function abs> -> callable? True
    # <class 'str'> -> callable? True
    # 13 -> callable? False
    # aaa -> callable? False

if False:
    # ---------------------------------------------------------------------
    # user-defined callable types
    # ; making an object to behave like function (callable)
    # ; __call__ should be implemented
    #
    # object.__call__(self[, args...])
    # ; called when the instance is "called" as a function
    # ; if this method is defined, x(arg1, arg2, ...) roughly translates to
    #   type(x).__call__(x, arg1, arg2, ...)
    #
    # callable(object)
    # ; return true if the object argument appears callable, false if not
    # ; classes are callable (calling a class returns a new instance)
    # ; instances are callable if their class has a __call__() method
    # ---------------------------------------------------------------------
    import random

    class BingoCage:
        def __init__(self, items):
            self._items = list(items) 
            random.shuffle(self._items) 

        def __repr__(self):
            return "%r" % self._items

        def pick(self):
            try:
                return self._items.pop()
            except LookupError:
                raise LookupError('pick from an empty BingoCage') 

        def __call__(self):
            "this makes self callable!"
            return self.pick()


    bingo = BingoCage(range(10))
    print("bingo=", bingo)

    for i in range(10):
        if i % 2:
            print("pick[{}]= {}".format(i, bingo.pick()))
        else:
            print("pick[{}]= {}".format(i, bingo()))
        # bingo() does the same thing aas bingo.pick()

    print("callable(bingo)=", callable(bingo))

if False:
    # function introspection
    # ; listing attributes of functions that don't exist in plain instances
    class Temp:
        pass
    obj = Temp()

    def func():
        pass

    print("# function-only attributes")
    for attr in sorted(set(dir(func)) - set(dir(obj))):
        print("attr=", attr)

if False:
    # extracting information about the function arguments (1)
    # ; from function attributes
    def some_func(name, /, age=17, sex="male", **kwargs):
        thisfunc = sys._getframe().f_code.co_name
        print("\n[info] {} invoked ...".format(thisfunc))
        print("name= %s, age= %d, sex= %s" % (name, age, sex))
        for key in kwargs:
            print("{}={}".format(key, kwargs[key]))

    print("some_func.__defaults__=", some_func.__defaults__)
    print("some_func.__code__.co_varnames=", some_func.__code__.co_varnames)
    print("some_func.__code__.co_argcount=", some_func.__code__.co_argcount, end='\n\n')
    # some_func.__defaults__= (17, 'male')
    # some_func.__code__.co_varnames= ('name', 'age', 'sex', 'kwargs', 'thisfunc', 'key')
    # some_func.__code__.co_argcount= 3
    # -> does not include any variable arguments prefixed with * or **

    # extracting information about the function arguments (2)
    # ; using 'inspect' module's signature function
    import inspect
    sig = inspect.signature(some_func)
    print("sig=", sig)
    print("type(sig)=", type(sig))
    print("str(sig)=", str(sig))
    # sig= (name, /, age=17, sex='male', **kwargs)
    # type(sig)= <class 'inspect.Signature'>
    # str(sig)= (name, /, age=17, sex='male', **kwargs)

    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)

    # POSITIONAL_ONLY : name = <class 'inspect._empty'>
    # POSITIONAL_OR_KEYWORD : age = 17
    # POSITIONAL_OR_KEYWORD : sex = male
    # VAR_KEYWORD : kwargs = <class 'inspect._empty'>

if False:
    import inspect
    # function annotations
    # ; just saved in function.__annotations__
    # ; nothing else is done, like no checks, enforcement, validation
    def add(a:'int > 0', b:'int > 0') -> int:
        return a + b

    print("add(3, 4) =", add(3, 4))
    print("add.__annotations__=", add.__annotations__)
    print("add(-3, 4) =", add(-3, 4)) # nothing is checked!

    print()

    sig = inspect.signature(add)
    print("sig=", sig)
    print("str(sig)=", str(sig))
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)

if False:
    # freezing arguments with functools.partial using functools.partial
    # ; produces a new callable with some of the arguments of the original
    #   function fixed.
    # ; returns a new callable with fewer arguments
    import functools
    def add(a, b):
        print('[dbg ] a= {}, b= {}'.format(a, b))
        return a + b

    func1 = functools.partial(add, 1)
    #                              |
    #                             'a' fixed
    print('\nfunc1.func =', func1.func)
    print('func1.args =', func1.args)
    print('func1.keywords =', func1.keywords)
    print([func1(i) for i in range(10)])

    func2 = functools.partial(add, 2)
    #                              |
    #                             'a' fixed
    print('\nfunc2.func =', func2.func)
    print('func2.args =', func2.args)
    print('func2.keywords =', func2.keywords)
    print([func2(i) for i in range(10)])

    func3 = functools.partial(add, 2, 3) # all arguments fixed!
    #                              |  |
    #                              | 'b' fixed
    #                             'a' fixed
    print('\nfunc3.func =', func3.func)
    print('func3.args =', func3.args)
    print('func3.keywords =', func3.keywords)
    print([func3() for i in range(10)])


# -------------------------------------
# chapter 6: design patterns with first-class functions


# case study: refactoring strategy
# - strategy design pattern
# ; define a family of algorithms, encapsulate each one, and make them
#   interchangeable.
# ; strategy lets the algorithm vary independently from clients that use it.
#
# - discount rules
# ; customers with 1,000 or more fidelity points get a global 5% discount per order - fidelity
# ; a 10% discount is applied to each line item with 20 or more units in the same order - bulkitem
# ; orders with at least 10 distinct items get a 7% global discount - largeorder
#   (fidelity : the quality of being faithful or loyal to a country, organization, etc)


if False:
    # - example 6-1. implementation order class with pluggable discount
    #   strategies
    # ; @abstractmethod decorator from 'abc' module
    from abc import ABC, abstractmethod
    from collections import namedtuple

    Customer = namedtuple('Customer', 'name fidelity')

    class LineItem:
        def __init__(self, product, quantity, price):
            self.product = product # str
            self.quantity = quantity # int
            self.price = price # float

        def total(self):
            return self.price * self.quantity

        def __repr__(self):
            fmt = "item: product={:s} quantity={:d} price={:.2f} total={:.2f}"
            return fmt.format(
                self.product, self.quantity, self.price, self.total()
            )

    class Order: # the Context
        def __init__(self, customer, cart, promotion=None):
            self.customer = customer
            self.cart = list(cart) # cart -> iterable
            self.promotion = promotion

        def total(self):
            if not hasattr(self, '__total'):
                self.__total = sum(item.total() for item in self.cart)
            return self.__total

        def due(self):
            if self.promotion is None:
                discount = 0
            else:
                discount = self.promotion.discount(self)
            return self.total() - discount #       -+--
            #                                       |
            #                                  order object
            #                                  ; Promotion.discount(promotion, order)

        def __repr__(self):
            fmt = "{:s}(fidelity={:d})'s order total: {:.2f} due: {:.2f}"
            return fmt.format(self.customer.name, self.customer.fidelity,
                              self.total(), self.due())

                          # ---------------------------------------------
    class Promotion(ABC): # the Strategy: an abstract base class
                          # ; ABC -> cannot be instantiated directly
                          # ; @abstractmethod must be overriden
                          #   in the derived class(pure virtual function)
        @abstractmethod   # ---------------------------------------------
        def discount(self, order):
            """Return discount as a positive dollar amount"""

    class Fidelity(Promotion): # 1st Concrete Strategy
        """5% discount for customers with 1000 or more fidelity points"""
        def discount(self, order):
            return order.total() * .05 if order.customer.fidelity >= 1000 else 0

    class BulkItem(Promotion): # 2nd Concrete Strategy
        """10% discount for each LineItem with 20 or more units"""
        def discount(self, order):
            discount = 0
            for item in order.cart:
                if item.quantity >= 20:
                    discount += item.total() * .1 # 10% discount
            return discount

    class LargeOrder(Promotion): # 3rd Concrete Strategy
        """7% discount for orders with 10 or more distinct items"""
        def discount(self, order):
            distinct_items = {item.product for item in order.cart} # set comprehension
            if len(distinct_items) >= 10:
                return order.total() * .07 # 7% discount
            return 0

    class Special(Promotion): # 4th Concrete Strategy
        """20% discount for every orders"""
        # didn't implement discount()
        # -> cannot instantiate this class -> error!
        pass

    # trying to instantiate Promotion ABC
    # promotion = Promotion()
    # -> TypeError: Can't instantiate abstract class Promotion with abstract method discount

    # customers
    joe = Customer('john doe', 0) # (name, fidelity)
    ann = Customer('ann smith', 1100)

    print("\n# 1. fidelity promotion")
    cart = [
        LineItem('banana', 4, .5), 
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)
    ]
    print(Order(joe, cart, Fidelity()))
    print(Order(ann, cart, Fidelity()))

    print("\n# 2. bulkitem promotion")
    cart = [
        LineItem('banana', 30, .5),
        LineItem('apple', 10, 1.5)
    ]
    print(Order(joe, cart, BulkItem()))
    print(Order(ann, cart, BulkItem()))

    print("\n# 3. large-order promotion")
    cart = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    #for i, item in enumerate(cart):
    #    print("{}. {}".format(i, item))
    print(Order(joe, cart, LargeOrder()))
    print(Order(ann, cart, LargeOrder()))
    # --------------------------------------------------------
    # 1. fidelity promotion
    # john doe(fidelity=0)'s order total: 42.00 due: 42.00
    # ann smith(fidelity=1100)'s order total: 42.00 due: 39.90
    # 2. bulkitem promotion
    # john doe(fidelity=0)'s order total: 30.00 due: 28.50
    # ann smith(fidelity=1100)'s order total: 30.00 due: 28.50
    # 3. large-order promotion
    # john doe(fidelity=0)'s order total: 10.00 due: 9.30
    # ann smith(fidelity=1100)'s order total: 10.00 due: 9.30
    # --------------------------------------------------------

if False:
    # - example 6-3. Order class with discount strategies
    #   implemented as functions
    # ; replacing the concrete strategies with simple functions and
    #   removing the Promo abstract class
    from collections import namedtuple

    Customer = namedtuple('Customer', 'name fidelity')

    class LineItem:
        def __init__(self, product, quantity, price):
            self.product = product
            self.quantity = quantity
            self.price = price

        def total(self):
            return self.price * self.quantity

        def __repr__(self):
            fmt = "item: product={:s} quantity={:d} price={:.2f} total={:.2f}"
            return fmt.format(
                self.product, self.quantity, self.price, self.total()
            )

    class Order: # the Context
        def __init__(self, customer, cart, promotion=None):
            self.customer = customer     # ---------
            self.cart = list(cart)       # function object(callable)
            self.promotion = promotion

        def total(self):
            if not hasattr(self, '__total'):
                self.__total = sum(item.total() for item in self.cart)
            return self.__total

        def due(self):
            if self.promotion is None:
                discount = 0.0
            else:
                discount = self.promotion(self)
                #          --------------------
                #          function call with order argument
            return self.total() - discount

        def __repr__(self):
            fmt = "total: {:.2f} due: {:.2f} with {:s}"
            return fmt.format(self.total(), self.due(), self.promotion.__name__)

    def fidelity_promotion(order:'Order') -> float:
        """5% discount for customers with 1000 or more fidelity points"""
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0

    def bulkitem_promotion(order:'Order') -> float:
        """10% discount for each LineItem with 20 or more units"""
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount

    def largeorder_promotion(order:'Order') -> float:
        """7% discount for orders with 10 or more distinct items"""
        distinct_items = {item.product for item in order.cart}
        #                -------------------------------------
        #                need to get list of unique items -> get comprehension
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0


    # customers
    joe = Customer('John Doe', 0) # (name, fidelity)
    ann = Customer('Ann Smith', 1100)

    print("\n# 1. fidelity promotion")
    cart1 = [
        LineItem('banana', 4, .5), 
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)
    ]
    print(joe.name, Order(joe, cart1, fidelity_promotion))
    print(ann.name, Order(ann, cart1, fidelity_promotion))

    print("\n# 2. bulkitem promotion")
    cart2 = [
        LineItem('banana', 30, .5),
        LineItem('apple', 10, 1.5)
    ]
    print(joe.name, Order(joe, cart2, bulkitem_promotion))
    print(ann.name, Order(ann, cart2, bulkitem_promotion))

    print("\n# 3. large-order promotion")
    cart3 = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    #for i, item in enumerate(cart3):
    #    print("{}. {}".format(i, item))
    print(joe.name, Order(joe, cart3, largeorder_promotion))
    print(ann.name, Order(ann, cart3, largeorder_promotion))


    customers = [joe, ann]
    carts = [cart1, cart2, cart3]
    promotions = [fidelity_promotion, bulkitem_promotion, largeorder_promotion]
    # -> hard-coded! hmm... is this the best?

    # listing all cases
    for customer in customers:
        print("\n# {}'s shopping cases".format(customer.name))
        for i, cart in enumerate(carts, 1):
            print("- cart{}".format(i))
            for promotion in promotions:
                print(Order(customer, cart, promotion))

    # choosing the best strategy: simple approach
    def best_promotion(order):
        """select best discount available"""
        return max(promotion(order) for promotion in promotions)
        #          --------------------------------------------
        #                      generator expression

    for customer in customers:
        print("\n# {}'s best shopping".format(customer.name))
        for i, cart in enumerate(carts, 1):
            print("cart{}".format(i), Order(customer, cart, best_promotion))

    # acquiring enrolled promotions automatically
    # ; this approach is not good if somebody doesn't follow
    #   the naming rule for promotion policy.
    table = dict(globals())
    promotions = [table[name] for name in table
                              if name.endswith('_promotion')
                              and not name.startswith('best_')]
    print("promotions=", promotions)
    #for key, val in dict(globals()).items():
    #    if key.endswith('_promotion') and not key.startswith('best'):
    #        promotions.append(val)


# -------------------------------------
# chapter 7: function decorators and closures

# - closure
# ; a closure is a function object that remembers values in enclosing scopes
#   even if they are not present in memory.
#
# - closure : 자신을 둘러싼 스코프(네임스페이스)의 상태값을 기억하는 함수
#  ; 해당 함수는 어떤 함수 내의 중첩된 함수여야 한다.
#  ; 해당 함수는 자신을 둘러싼(enclose) 함수 내의 상태값을 반드시 참조해야 한다.
#  ; 해당 함수를 둘러싼 함수는 이 함수를 반환해야 한다.
#
# - decorator
# ; a callable that takes another function as argument(the decorated function)
#
# - decorator syntax
# ; replace the decorated function with a similar or different one
# ; functions are decorated during their import-time, not run-time
# ; syntactic sugar for metaprogramming(changing behavior at run-time)
# ; registered at 'import time', not run-time
if False:
    def decorate(func):
        def wrapper():
            print('[info]', func.__name__, 'starts ...')
            func()
            print('[info]', func.__name__, 'ends ...')
        return wrapper

    @decorate
    def target():
        print("[info] target() running ...")

    target() # decorated version
             # ; same as target = decorate(target)
    # [info] target starts ...
    # [info] target() running ...
    # [info] target ends ...

    print("target=", target)
    # target= <function decorate.<locals>.wrapper at 0x000001F5415A8F40>


if False:
    # - example 7-2 when python executes decorators
    registry = [] 
    
    def register(func): 
        print('[info] running register(%s)' % func) 
        registry.append(func) 
        return func 
    
    @register 
    def f1():
        print('[info] running f1()')
    
    @register
    def f2():
        print('[info] running f2()')
    
    def f3(): 
        print('[info] running f3()')
    
    def main(): 
        print('[info] running main()')
        print('       registry ->', registry)
        f1()
        f2()
        f3()
    
    
    main() 
    # [info] running register(<function f1 at 0x00000198CC9A8FE0>)
    # [info] running register(<function f2 at 0x00000198CC9A8F40>)
    # [info] running main()
    #        registry -> [
    #                <function f1 at 0x00000198CC9A8FE0>,
    #                <function f2 at 0x00000198CC9A8F40>
    #            ]
    # [info] running f1()
    # [info] running f2()
    # [info] running f3()


if False:
    # - example 7-3. the functions for promotions are gathered by
    #   the promotion decorator
    # ; better implementation for flexible policy management
    #   using registration decorator
    from collections import namedtuple

    Customer = namedtuple('Customer', 'name fidelity')

    class LineItem:
        def __init__(self, product, quantity, price):
            self.product = product
            self.quantity = quantity
            self.price = price

        def total(self):
            return self.price * self.quantity

        def __repr__(self):
            fmt = "item: product={:s} quantity={:d} price={:.2f} total={:.2f}"
            return fmt.format(
                self.product, self.quantity, self.price, self.total()
            )

    class Order: # the Context
        def __init__(self, customer, cart, promotion=None):
            self.customer = customer     # ---------
            self.cart = list(cart)       # function object!
            self.promotion = promotion

        def total(self):
            if not hasattr(self, '__total'):
                self.__total = sum(item.total() for item in self.cart)
            return self.__total

        def due(self):
            if self.promotion is None:
                discount = 0
            else:
                discount = self.promotion(self)
            return self.total() - discount

        def __repr__(self):
            fmt = "total: {:.2f} due: {:.2f} with {:s}"
            return fmt.format(self.total(), self.due(), self.promotion.__name__)

                    # --------------------------------------------------
    promotions = [] # decorator will fill this list!
                    # (1) no need to maintain the function naming
                    # (2) the purpose for function is clear
                    # (3) strategies can be maintained in another module
                    #     (separation -> easy to handle)
                    # --------------------------------------------------

    def promotion(func): # decorator
        print("[info] registering {} promotion at import-time ...".format(func.__name__))
        promotions.append(func)
        return func

    @promotion
    def fidelity(order): 
        """5% discount for customers with 1000 or more fidelity points"""
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0

    @promotion
    def bulk_item(order):
        """10% discount for each LineItem with 20 or more units"""
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount

    @promotion
    def large_order(order):
        """7% discount for orders with 10 or more distinct items"""
        distinct_items = {item.product for item in order.cart} # set comprehension
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0

    def best_promotion(order):
        """select best discount available"""
        return max(promotion(order) for promotion in promotions)
        #          --------------------------------------------
        #                      generator expression

    joe = Customer('John Doe', 0) # (name, fidelity)
    ann = Customer('Ann Smith', 1100)
    customers = [joe, ann]

    cart1 = [
        LineItem('banana', 4, .5), 
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)
    ]
    cart2 = [
        LineItem('banana', 30, .5),
        LineItem('apple', 10, 1.5)
    ]
    cart3 = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    carts = [cart1, cart2, cart3]

    for customer in customers:
        print("\n# {}'s best shopping".format(customer.name))
        for i, cart in enumerate(carts, 1):
            print("cart{}".format(i), Order(customer, cart, best_promotion))


if False:
    # - example 7-8. average_oo.py
    # ; a class-based implementation that calculates a running average
    class Averager():
        def __init__(self):
            self.series = [] # list

        # for callable object
        def __call__(self, value):
            self.series.append(value)
            if True:
                print('[dbg ] series=', self.series)
            return sum(self.series)/len(self.series)
            #      ---------------------------------
            #                  average

    average = Averager() # callable object
    for i in range(10):
        print("average({})=".format(i), average(i))

    # [dbg ] series= [0]
    # average(0)= 0.0
    # [dbg ] series= [0, 1]
    # average(1)= 0.5
    # [dbg ] series= [0, 1, 2]
    # average(2)= 1.0
    # [dbg ] series= [0, 1, 2, 3]
    # average(3)= 1.5
    # [dbg ] series= [0, 1, 2, 3, 4]
    # average(4)= 2.0
    # [dbg ] series= [0, 1, 2, 3, 4, 5]
    # average(5)= 2.5
    # [dbg ] series= [0, 1, 2, 3, 4, 5, 6]
    # average(6)= 3.0
    # [dbg ] series= [0, 1, 2, 3, 4, 5, 6, 7]
    # average(7)= 3.5
    # [dbg ] series= [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # average(8)= 4.0
    # [dbg ] series= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # average(9)= 4.5

if False:
    # - example 7-9. average.py
    # ; a higher-order function to calculate a running average
    def make_averager():
        series = [] # list, nonlocal scope of averager
                    # free variable

        def averager(value): # closure
            series.append(value)
            if True:
                print('[dbg ] series=', series)
            return sum(series)/len(series) # not efficient!

        return averager # returns inner function

    average = make_averager() # returns callable object

    del(make_averager) # it's ok now

    for i in range(10):
        print("average({})=".format(i), average(i))
    # [dbg ] series= [0]
    # average(0)= 0.0
    # [dbg ] series= [0, 1]
    # average(1)= 0.5
    # [dbg ] series= [0, 1, 2]
    # average(2)= 1.0
    # [dbg ] series= [0, 1, 2, 3]
    # average(3)= 1.5
    # [dbg ] series= [0, 1, 2, 3, 4]
    # average(4)= 2.0
    # [dbg ] series= [0, 1, 2, 3, 4, 5]
    # average(5)= 2.5
    # [dbg ] series= [0, 1, 2, 3, 4, 5, 6]
    # average(6)= 3.0
    # [dbg ] series= [0, 1, 2, 3, 4, 5, 6, 7]
    # average(7)= 3.5
    # [dbg ] series= [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # average(8)= 4.0
    # [dbg ] series= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # average(9)= 4.5

    # free variables of closure
    # ; a closure is a function that retains the bindings of the free
    #   variables that exist when the function is defined
    # ; python keeps the names of local and free variables in the __code__ attribute
    print("average.__code__.co_varnames=", average.__code__.co_varnames)
    print("average.__code__.co_freevars=", average.__code__.co_freevars) # 1 free variable 'series'
    print("average.__closure__=", average.__closure__)
    print("average.__closure__[0].cell_contents=", average.__closure__[0].cell_contents)
    # average.__code__.co_varnames= ('value',)
    # average.__code__.co_freevars= ('series',)
    # average.__closure__= (<cell at 0x0000013ADB548070: list object at 0x0000013ADB54F040>,)
    # average.__closure__[0].cell_contents= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if False:
    # example 7-14. calculate a running average without keeping all history
    # (fixed with the use of nonlocal)
    def make_averager():
        count = 0
        total = 0

        def averager(value): # closure
            nonlocal count, total
            count += 1
            total += value
            if True:
                print('[dbg ] count= {}, total= {}'.format(count, total))
            return total/count # changed!

        return averager

    average = make_averager() # callable object
    del(make_averager) # it's ok now
    for i in range(10):
        print("average({})=".format(i), average(i))
    # [dbg ] count= 1, total= 0
    # average(0)= 0.0
    # [dbg ] count= 2, total= 1
    # average(1)= 0.5
    # [dbg ] count= 3, total= 3
    # average(2)= 1.0
    # [dbg ] count= 4, total= 6
    # average(3)= 1.5
    # [dbg ] count= 5, total= 10
    # average(4)= 2.0
    # [dbg ] count= 6, total= 15
    # average(5)= 2.5
    # [dbg ] count= 7, total= 21
    # average(6)= 3.0
    # [dbg ] count= 8, total= 28
    # average(7)= 3.5
    # [dbg ] count= 9, total= 36
    # average(8)= 4.0
    # [dbg ] count= 10, total= 45
    # average(9)= 4.5

    # free variables of closure
    print("average.__code__.co_varnames=", average.__code__.co_varnames)
    print("average.__code__.co_freevars=", average.__code__.co_freevars)
    print("average.__closure__=", average.__closure__)
    print("average.__closure__[0].cell_contents=", average.__closure__[0].cell_contents)
    print("average.__closure__[1].cell_contents=", average.__closure__[1].cell_contents)
    # average.__code__.co_varnames= ('value',)
    # average.__code__.co_freevars= ('count', 'total')
    # average.__closure__= (
    #     <cell at 0x000001DF6EF58B80: int object at 0x00007FFBD248D448>,
    #     <cell at 0x000001DF6EF590F0: int object at 0x00007FFBD248D8A8>
    # )
    # average.__closure__[0].cell_contents= 10 ---> count
    # average.__closure__[1].cell_contents= 45 ---> total


if False:
    # decorator
    # ; example 7-15. a simple decorator to output the running time of functions
    # ; shortcomings
    #   keyword arguments not supported
    #   loses some attributes of the decorated function
    import time

    def clock(func):
        def clocked(*args): # inner
            t0 = time.perf_counter() # or perf_counter_ns()
            result = func(*args) # [note] 'func' is a free variable within closure 
            elapsed = time.perf_counter() - t0 # or perf_counter_ns()
            name = func.__name__
            arg_str = ', '.join(repr(arg) for arg in args)
            print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
            return result
        return clocked # clocked function
                       # this replaces the decorated function

    @clock
    def snooze(seconds):
        time.sleep(seconds)
    # same as 'snooze = clock(snooze)'

    @clock
    def factorial(n):
        '''factorial(n) returns n!'''
        return 1 if n < 2 else n * factorial(n-1)
    # same as 'factorial = clock(factorial)


    print('[info] calling snooze(.123) ...')
    snooze(.123)
    # [0.12303880s] snooze(0.123) -> None

    print('[info] calling factorial(6) ...')
    print('6! =', factorial(6))
    # [0.00000050s] factorial(1) -> 1
    # [0.00002910s] factorial(2) -> 2
    # [0.00005210s] factorial(3) -> 6
    # [0.00007450s] factorial(4) -> 24
    # [0.00009630s] factorial(5) -> 120
    # [0.00011970s] factorial(6) -> 720
    # 6! = 720

    print("[debug] factorial.__name__=", factorial.__name__)
    print("[debug] factorial.__doc__=", factorial.__doc__)
    # [debug] factorial.__name__= clocked
    # [debug] factorial.__doc__= None
    # -> decorator masks __name__ and __doc__ of decorated function, hmm...


if False:
    # - example 7-17. an improved clock decorator using functools.wraps()
    # ; 'functools.wraps()' copies attributes like __name__ and __doc__
    #   from the decorated function, and
    #   helps building well-behaved decorators
    # ; enhanced using 'functools.wraps()'
    #   (1) keyword arguments supported now
    #   (2) doesn't lose attributes of the decorated function
    import time
    import functools

    def clock(func):
        @functools.wraps(func) # (2) func's attributes preserved
        def clocked(*args, **kwargs): # (1) kwargs can be handled
            t0 = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - t0
            funcname = func.__name__
            arglist = []
            if args:
                arglist.append(', '.join(repr(arg) for arg in args))
            if kwargs:
                pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
                arglist.append(', '.join(pairs))
            arg_str = ', '.join(arglist)
            print('[%0.8fs] %s(%s) -> %r ' % (elapsed, funcname, arg_str, result))
            return result
        return clocked # (2) func.__name__ is passed


    @clock
    def snooze(seconds):
        time.sleep(seconds)
    # same as 'snooze = clock(snooze)'

    @clock
    def factorial(n):
        '''factorial(n) returns n!'''
        return 1 if n < 2 else n * factorial(n-1)
    # same as 'factorial = clock(factorial)

    print('[info] calling snooze(.123) ...')
    snooze(.123)
    # [0.12303880s] snooze(0.123) -> None

    print('[info] calling factorial(6) ...')
    print('6! =', factorial(6))
    # [0.00000050s] factorial(1) -> 1
    # [0.00002910s] factorial(2) -> 2
    # [0.00005210s] factorial(3) -> 6
    # [0.00007450s] factorial(4) -> 24
    # [0.00009630s] factorial(5) -> 120
    # [0.00011970s] factorial(6) -> 720
    # 6! = 720

    print("[debug] factorial.__name__=", factorial.__name__)
    print("[debug] factorial.__doc__=", factorial.__doc__)
    print("        functools.wraps() copied the original attribute of factorial")
    print("        to the clocked wrapper")
    # [debug] factorial.__name__= factorial
    # [debug] factorial.__doc__= factorial(n) returns n!
    #         functools.wraps() copied the original attribute of factorial
    #         to the clocked wrapper


if False:
    # 3 decorators in the standard library
    # ; property, classmethod, staticmethod
    # ; lru_cache and singledispatch decorators in functools module
    pass

if False:
    # - example 7-18 memoization with functools.lru_cache
    # ; recursive way to compute the nth number in the fibonacci series
    #   without memoization would be very costly!
    # ; improved with functools.lru_cache decorator
    # ; LRU(Least Recently Used)
    import time
    import functools

    def clock(func):
        @functools.wraps(func)
        def clocked(*args, **kwargs):
            t0 = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - t0
            funcname = func.__name__
            arg_lst = []
            if args:
                arg_lst.append(', '.join(repr(arg) for arg in args))
            if kwargs:
                pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
                arg_lst.append(', '.join(pairs))
            arg_str = ', '.join(arg_lst)
            print('[%0.8fs] %s(%s) -> %r ' % (elapsed, funcname, arg_str, result))
            return result
        return clocked

    @clock
    def fibonacci(n):
        '''fibonacci(n)'''
        if n < 2:
            return n
        return fibonacci(n-2) + fibonacci(n-1) # recursive version

    print('fibonacci(6)=', fibonacci(6))

    # ---------------------------------------
    # [0.00000000s] fibonacci(0) -> 0
    # [0.00000000s] fibonacci(1) -> 1 ***
    # [0.00000000s] fibonacci(2) -> 1
    # [0.00000000s] fibonacci(1) -> 1 ***
    # [0.00000000s] fibonacci(0) -> 0
    # [0.00000000s] fibonacci(1) -> 1 ***
    # [0.00100088s] fibonacci(2) -> 1
    # [0.00100088s] fibonacci(3) -> 2
    # [0.00100088s] fibonacci(4) -> 3
    # [0.00000000s] fibonacci(1) -> 1 ***
    # [0.00000000s] fibonacci(0) -> 0
    # [0.00000000s] fibonacci(1) -> 1 ***
    # [0.00100017s] fibonacci(2) -> 1
    # [0.00100017s] fibonacci(3) -> 2
    # [0.00000000s] fibonacci(0) -> 0
    # [0.00000000s] fibonacci(1) -> 1 ***
    # [0.00000000s] fibonacci(2) -> 1
    # [0.00000000s] fibonacci(1) -> 1 ***
    # [0.00000000s] fibonacci(0) -> 0
    # [0.00000000s] fibonacci(1) -> 1 ***
    # [0.00000000s] fibonacci(2) -> 1
    # [0.00099969s] fibonacci(3) -> 2
    # [0.00199914s] fibonacci(4) -> 3
    # [0.00399995s] fibonacci(5) -> 5
    # [0.00600100s] fibonacci(6) -> 8
    #
    # fibonacci(0) -> 5 times
    # fibonacci(1) -> 8 times -> very costly!
    # fibonacci(2) -> 5 times
    # fibonacci(3) -> 3 times
    # fibonacci(4) -> 2 times
    # fibonacci(5) -> 1 times
    # fibonacci(6) -> 1 times
    # ---------------------------------------

if False:
    # - example 7-19. faster implementation using caching
    # ; with memoization with functools.lru_cache decorator
    #   (lru: least recently used)
    # ; discarding least recently used one in the cache
    # - @functools.lru_cache(user_function) ---> maxsize=128(default)
    # - @functools.lru_cache(maxsize=128, typed=False)
    # ; decorator to wrap a function with a memoizing callable that saves up
    #   to the maxsize most recent calls.
    # ; since a dictionary is used to cache results, the positional and
    #   keyword arguments to the function must be hashable.
    # ; if maxsize is set to none, the lru feature is disabled and the cache
    #   can grow without bound.
    # ; if typed is set to true, function arguments of different types will be
    #   cached separately.
    import time
    import functools

    def clock(func):
        @functools.wraps(func)
        def clocked(*args, **kwargs):
            t0 = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - t0
            funcname = func.__name__
            arg_lst = []
            if args:
                arg_lst.append(', '.join(repr(arg) for arg in args))
            if kwargs:
                pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
                arg_lst.append(', '.join(pairs))
            arg_str = ', '.join(arg_lst)
            print('[%0.8fs] %s(%s) -> %r ' % (elapsed, funcname, arg_str, result))
            return result
        return clocked

    @functools.lru_cache() # stacked decorators with no config paramter
    @clock
    def fibonacci(n):
        '''fibonacci(n)'''
        if n < 2:
            return n
        return fibonacci(n-2) + fibonacci(n-1)

    print('fibonacci(6)=', fibonacci(6))
    # ------------------------------------------------------------------
    # [0.00000000s] fibonacci(0) -> 0
    # [0.00000000s] fibonacci(1) -> 1
    # [0.00000000s] fibonacci(2) -> 1
    # [0.00000000s] fibonacci(3) -> 2
    # [0.00178313s] fibonacci(4) -> 3
    # [0.00000000s] fibonacci(5) -> 5
    # [0.00178313s] fibonacci(6) -> 8 *** performance improved a lot ***
    # fibonacci(6)= 8
    # ------------------------------------------------------------------


if False:
    # - example 7-21. singledispatch creates a custom htmlize.register
    #   to bundle several functions into a generic function
    # - @functions.singledispatch generic functions
    # ; transform a function into a single-dispatch generic function.
    #   (similar to function overloading in c++)
    # ; to define a generic function, decorate it with the @singledispatch
    #   decorator.
    # ; when defining a function using @singledispatch, note that the dispatch
    #   happens on the type of the first argument
    import functools
    from collections import abc
    import numbers
    import html

    @functools.singledispatch # generic-function htmlize()
    def htmlize(obj):
        content = html.escape(repr(obj))
        return '<pre>{}</pre>'.format(content)

    @htmlize.register(str) 
    def _(text): 
        content = html.escape(text).replace('\n', '<br>\n')
        return '<p>{0}</p>'.format(content)

    @htmlize.register(numbers.Integral) 
    def _(n):
        return '<pre>{0} (0x{0:x})</pre>'.format(n)

    # several decorators can be stacked for multiple types
    @htmlize.register(tuple) # stacked decorators
    @htmlize.register(abc.MutableSequence)
    def _(seq):
        inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
        return '<ul>\n<li>' + inner + '</li>\n</ul>'

    print(htmlize({1, 2, 3}))
    print(htmlize(abs))
    print(htmlize('Heimlich & Co.\n- a game'))
    print(htmlize(42))
    print(htmlize(['alpha', 66, {3, 2, 1}]))
    # <pre>{1, 2, 3}</pre>
    # <pre>&lt;built-in function abs&gt;</pre>
    # <p>Heimlich &amp; Co.<br>
    # - a game</p>
    # <pre>42 (0x2a)</pre>
    # <ul>
    # <li><p>alpha</p></li>
    # <li><pre>66 (0x42)</pre></li>
    # <li><pre>{1, 2, 3}</pre></li>
    # </ul>


# - stacked decorators
# ; decorator2 first, decorator1 later
#
# @decorator1
# @decorator2
# def some_func():
#     ... ...
# 
# -> same as the following
# some_func = decorator1(decorator2(some_func)


if False:
    # - example 7-22. simple function registry
    registry = []

    def register(func):
        print('[dbg ] registering function %s ...' % func.__name__)
        registry.append(func)
        return func

    @register
    def f1():
        print('running f1() ...')

    @register
    def f2():
        print('running f2() ...')

    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    # [dbg ] registering function f1 ...
    # [dbg ] registering function f2 ...
    # running main()
    # registry -> [
    #    <function f1 at 0x0000026C91FA8F40>,
    #   <function f2 at 0x0000026C91FCA520>
    # ]
    # running f1() ...
    # running f2() ...


if False:
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


if True:
    # example 7-25. parameterized clock decorator
    import functools
    import time

    DEFAULT_FMT = '[{elapsed:0.8f}s] {funcname}({arg_str}) -> {result}'

    def clock(fmt=DEFAULT_FMT): 
        def clock_inner(func): # ---> requires 1 more level if nested structure
            @functools.wraps(func)
            def clocked(*args, **kwargs):
                t0 = time.perf_counter()
                result = func(*args, **kwargs)
                elapsed = time.perf_counter() - t0 #
                funcname = func.__name__ #
                arg_lst = []
                if args:
                    arg_lst.append(', '.join(repr(arg) for arg in args))
                if kwargs:
                    pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
                    arg_lst.append(', '.join(pairs))
                arg_str = ', '.join(arg_lst) #
                print(fmt.format(**locals())) # type(locals()) == dict
                return result
            return clocked
        return clock_inner


    @clock() # default format
    def snooze(seconds):
        time.sleep(seconds)

    @clock() # default format
    def factorial_0(n):
        '''factorial_0(n) returns n!'''
        return 1 if n < 2 else n * factorial_0(n-1)

    @clock('[dbg ] {funcname}({arg_str}) --- elapsed= {elapsed:0.8f}s') # different format!
    def factorial_1(n):
        '''factorial_1(n) returns n!'''
        return 1 if n < 2 else n * factorial_1(n-1)

    print('[info] calling snooze(.123) ...')
    snooze(.123)

    print('[info] calling factorial(6) ...')
    print('6!(0) =', factorial_0(6))
    print('6!(1) =', factorial_1(6))

    # ----------------------------------------------
    # [info] calling snooze(.123) ...
    # [0.12372100s] snooze(0.123) -> None
    # 
    # [info] calling factorial(6) ...
    # [0.00000070s] factorial_0(1) -> 1
    # [0.00003720s] factorial_0(2) -> 2
    # [0.00008030s] factorial_0(3) -> 6
    # [0.00011710s] factorial_0(4) -> 24
    # [0.00015030s] factorial_0(5) -> 120
    # [0.00018410s] factorial_0(6) -> 720
    # 6!(0) = 720
    # 
    # [dbg ] factorial_1(1) --- elapsed= 0.00000040s
    # [dbg ] factorial_1(2) --- elapsed= 0.00004080s
    # [dbg ] factorial_1(3) --- elapsed= 0.00023580s
    # [dbg ] factorial_1(4) --- elapsed= 0.00035670s
    # [dbg ] factorial_1(5) --- elapsed= 0.00049150s
    # [dbg ] factorial_1(6) --- elapsed= 0.00063000s
    # 6!(1) = 720
    # ----------------------------------------------
