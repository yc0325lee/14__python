#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : E_Commerce_Shopping.py
# - author : yc0325lee
# - created : 2022-12-01 23:19:33 by yc032
# - modified : 2022-12-01 23:19:33 by yc032
# - description : 
# - case study
# ; refactoring strategy pattern
# - strategy design pattern
# ; define a family of algorithms, encapsulate each one, and make them
#   interchangeable.
# ; strategy lets the algorithm vary independently from clients that use it.
# - discount rules
# ; customers with 1,000 or more fidelity points get a global 5% discount per order - fidelity
# ; a 10% discount is applied to each line item with 20 or more units in the same order - bulkitem
# ; orders with at least 10 distinct items get a 7% global discount - largeorder
#   (fidelity : the quality of being faithful or loyal to a country, organization, etc)
# ----------------------------------------------------------------------------

if False:
    # - example 6-1
    # ; implementing order class with pluggable discount strategies
    # ; class-based design structure
    # ; abc.ABC abstract base class with @abstractmethod decorator
    #   for pure virtual function
    import abc
    import collections
    import random
    random.seed(a=4321) # seed-ing

    Customer = collections.namedtuple('Customer', 'name fidelity')

    def gen_customers(count=10):
        length = 3
        i = count
        while i > 0:
            name = ''
            for _ in range(length):
                #name += chr(random.randint(97, 122)) # a ~ z
                name += chr(random.randint(ord('a'), ord('z')))
            fidelity = random.randint(1, 20) * 100
            yield Customer(name, fidelity)
            i -= 1

    # ---------------------------------
    class LineItem:
        def __init__(self, product, quantity, price):
            self.product = product # str
            self.quantity = quantity # int
            self.price = price # float

        def total(self):
            return self.price * self.quantity

        def __repr__(self):
            fmt = "{}({!r}, {!r}, {:.2f})"
            return fmt.format(
                type(self).__name__, self.product, self.quantity, self.price
            )

    def gen_lineitems(count=10):
        length = 5
        i = count
        while i > 0:
            product = ''
            for _ in range(length):
                #product += chr(random.randint(97, 122)) # a ~ z
                product += chr(random.randint(ord('a'), ord('z')))
            quantity = random.randint(1, 19)
            price = random.random() * 20
            yield LineItem(product, quantity, price)
            i -= 1

    # ---------------------------------
    class Order: # the Context
        def __init__(self, customer, cart, promotion=None):
            self.customer = customer
            self.cart = list(cart) # cart -> iterable
            self.promotion = promotion

        def total(self):
            if not hasattr(self, '__total'):
                self.__total = sum(item.total() for item in self.cart)
            return self.__total

        def discount(self):
            if not hasattr(self, '__discount'):
                if self.promotion is None:
                    self.__discount = 0.0
                else:
                    self.__discount = self.promotion.discount(self)
                    #                                         ----
                    #                                      order object

            return self.__discount

        def due(self):
            return self.total() - self.discount()

        def __repr__(self):
            fmt = "{!r}({!r}, {!r}, {!r})"
            return fmt.format(
                type(self).__name__, self.customer, self.cart, self.promotion
            )

        def __str__(self):
            fmt = "{:s}(fidelity={:d})'s order total: {:.2f}, discount: {:.2f}, due: {:.2f}"
            return fmt.format(
                self.customer.name, self.customer.fidelity, self.total(),
                self.discount(), self.due()
            )

    # ---------------------------------
    # - strategy abstract base class
    # ; abc.ABC -> cannot be instantiated directly
    # ; methods with @abstractmethod decorator must be overriden
    #   in the derived class(-> pure virtual function)
    class Promotion(abc.ABC):
        @abc.abstractmethod
        def discount(self, order):
            """Return discount as a positive dollar amount"""
            raise NotImplementedError("pure virtual function")

    class Fidelity(Promotion): # 1st concrete strategy
        """5% discount for customers with 1000 or more fidelity points"""
        def discount(self, order):
            return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0.0

    class BulkItem(Promotion): # 2nd concrete strategy
        """10% discount for each LineItem with 20 or more units"""
        def discount(self, order):
            discount = 0.0
            for item in order.cart:
                if item.quantity >= 10:
                    discount += item.total() * 0.1 # 10% discount
            return discount

    class LargeOrder(Promotion): # 3rd concrete strategy
        """7% discount for orders with 10 or more distinct items"""
        def discount(self, order):
            distinct_items = {item.product for item in order.cart} # set comprehension
            if len(distinct_items) >= 10:
                return order.total() * 0.07 # 7% discount
            return 0.0

    class Special(Promotion): # 4th Concrete Strategy
        """20% discount for every orders"""
        # didn't implement discount()
        # -> cannot instantiate this class -> error!
        pass

    # trying to instantiate Promotion ABC
    # promotion = Promotion()
    # -> TypeError: Can't instantiate abstract class Promotion with abstract
    #               method discount

    # customers
    customers = list(gen_customers(10))
    print('\n# customers')
    for customer in customers:
        print(customer)

    # carts
    carts = list()
    for _ in range(10):
        carts.append(list(gen_lineitems(random.randint(1, 15))))
    print('\n# carts')
    for i, cart in enumerate(carts):
        total = 0.0
        print('\ncart[{}]'.format(i))
        for j, item in enumerate(cart):
            due = item.quantity * item.price
            print('item[{}]= {}, due= {:.2f}'.format(j, item, due))
            total += due
        print('total= {:.2f}'.format(total))

    # promotions
    promotions = [Fidelity(), BulkItem(), LargeOrder()] # concrete strategies

    # shoppings
    print('\n# all shoppings')
    for i, cart in enumerate(carts):
        print('\ncart[{}]'.format(i))
        for customer in customers:
            for promotion in promotions:
                print(
                    Order(customer, cart, promotion),
                    'with', type(promotion).__name__
                ) #         ------------------------
                  #            name of promotion

    # best shoppings
    print('\n# ' + '-' * 76)
    print('# best shoppings')
    for i, cart in enumerate(carts):
        print('\ncart[{}] - {} items'.format(i, len(cart)))
        for customer in customers:
            # getting the best discount & policy
            discount, policy = max(
                (Order(customer, cart, promotion).discount(), type(promotion).__name__)
                    for promotion in promotions
            )
            if discount > 0.0:
                print(
                    "{}'s best shopping is {} with discount= {:.2f}"
                    .format(customer, policy, discount)
                )
            else:
                print(
                    "{} is not qualified for any promotion. discount= {:.2f}"
                    .format(customer, discount)
                )


if True:
    # - example 6-3. order class with discount strategies
    #   implemented as functions
    # ; replacing the concrete strategies with simple functions and
    #   removing the Promo abstract class
    import collections
    import random
    random.seed(a=4321) # seed-ing

    Customer = collections.namedtuple('Customer', 'name fidelity')

    def gen_customers(count=10):
        length = 3
        i = count
        while i > 0:
            name = ''
            for _ in range(length):
                #name += chr(random.randint(97, 122)) # a ~ z
                name += chr(random.randint(ord('a'), ord('z')))
            fidelity = random.randint(1, 20) * 100
            yield Customer(name, fidelity)
            i -= 1

    # ---------------------------------
    class LineItem:
        def __init__(self, product, quantity, price):
            self.product = product # str
            self.quantity = quantity # int
            self.price = price # float

        def total(self):
            return self.price * self.quantity

        def __repr__(self):
            fmt = "{}({!r}, {!r}, {:.2f})"
            return fmt.format(
                type(self).__name__, self.product, self.quantity, self.price
            )

    def gen_lineitems(count=10):
        length = 5
        i = count
        while i > 0:
            product = ''
            for _ in range(length):
                #product += chr(random.randint(97, 122)) # a ~ z
                product += chr(random.randint(ord('a'), ord('z')))
            quantity = random.randint(1, 19)
            price = random.random() * 20
            yield LineItem(product, quantity, price)
            i -= 1

    # ---------------------------------
    class Order: # the Context
        def __init__(self, customer, cart, promotion=None):
            self.customer = customer
            self.cart = list(cart) # cart -> iterable
            self.promotion = promotion
            #                ---------
            #                function object(callable)

        def total(self):
            if not hasattr(self, '__total'):
                self.__total = sum(item.total() for item in self.cart)
            return self.__total

        def discount(self):
            if not hasattr(self, '__discount'):
                if self.promotion is None:
                    self.__discount = 0.0
                else:
                    self.__discount = self.promotion(self)
                    #                                ----
                    #                             order object
            return self.__discount

        def due(self):
            return self.total() - self.discount()

        def __repr__(self):
            fmt = "{!r}({!r}, {!r}, {!r})"
            return fmt.format(
                type(self).__name__, self.customer, self.cart, self.promotion
            )

        def __str__(self):
            fmt = "{:s}(fidelity={:d})'s order total: {:.2f}, discount: {:.2f}, due: {:.2f}"
            return fmt.format(
                self.customer.name, self.customer.fidelity, self.total(),
                self.discount(), self.due()
            )

    # ---------------------------------
    # - functions for strategy pattern
    def fidelity_promotion(order:'Order') -> float:
        """5% discount for customers with 1000 or more fidelity points"""
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0.0

    def bulkitem_promotion(order:'Order') -> float:
        """10% discount for each LineItem with 20 or more units"""
        discount = 0.0
        for item in order.cart:
            if item.quantity >= 10:
                discount += item.total() * 0.1 # 10% discount
        return discount

    def largeorder_promotion(order:'Order') -> float:
        """7% discount for orders with 10 or more distinct items"""
        distinct_items = {item.product for item in order.cart}
        #                -------------------------------------
        #                need to get list of unique items -> set comprehension
        if len(distinct_items) >= 10:
            return order.total() * 0.07 # 7% discount
        return 0.0

    # concrete strategies
    if False:
        promotions = [fidelity_promotion, bulkitem_promotion, largeorder_promotion]
        # -> hard-coded! hmm... is this the best?
    else:
        # acquiring enrolled promotions automatically
        # ; this approach is not good if somebody doesn't follow
        #   the naming rule for promotion policy.
        symtable = dict(globals())
        promotions = [symtable[name] for name in symtable
                                  if name.endswith('_promotion')
                                  and not name.startswith('best_')]
    print('\n# ' + '-' * 76)
    print('# all promotions')
    for i, promotion in enumerate(promotions):
        print('{}. {}'.format(i, promotion))


    # customers
    customers = list(gen_customers(10))
    print('\n# customers')
    for customer in customers:
        print(customer)

    # carts
    carts = list()
    for _ in range(10):
        carts.append(list(gen_lineitems(random.randint(1, 15))))
    print('\n# carts')
    for i, cart in enumerate(carts):
        total = 0.0
        print('\ncart[{}]'.format(i))
        for j, item in enumerate(cart):
            due = item.quantity * item.price
            print('item[{}]= {}, due= {:.2f}'.format(j, item, due))
            total += due
        print('total= {:.2f}'.format(total))

    # shoppings
    print('\n# ' + '-' * 76)
    print('# all shoppings')
    for i, cart in enumerate(carts):
        print('\ncart[{}]'.format(i))
        for customer in customers:
            for promotion in promotions:
                print(
                    Order(customer, cart, promotion),
                    'with', promotion.__name__
                ) #         ------------------
                  #          name of function

    # best shoppings
    print('\n# ' + '-' * 76)
    print('# best shoppings')
    for i, cart in enumerate(carts):
        print('\ncart[{}] - {} items'.format(i, len(cart)))
        for customer in customers:
            # getting the best discount & policy
            discount, policy = max(
                (Order(customer, cart, promotion).discount(), promotion.__name__)
                    for promotion in promotions
            )
            if discount > 0.0:
                print(
                    "{}'s best shopping is {} with discount= {:.2f}"
                    .format(customer, policy, discount)
                )
            else:
                print(
                    "{} is not qualified for any promotion. discount= {:.2f}"
                    .format(customer, discount)
                )


if True:
    # - example 7-3. the functions for promotions are gathered by
    #   the promotion decorator
    # ; better implementation for flexible policy management
    #   using registration decorator
    import collections
    import random
    random.seed(a=4321) # seed-ing

    Customer = collections.namedtuple('Customer', 'name fidelity')

    def gen_customers(count=10):
        length = 3
        i = count
        while i > 0:
            name = ''
            for _ in range(length):
                #name += chr(random.randint(97, 122)) # a ~ z
                name += chr(random.randint(ord('a'), ord('z')))
            fidelity = random.randint(1, 20) * 100
            yield Customer(name, fidelity)
            i -= 1

    # ---------------------------------
    class LineItem:
        def __init__(self, product, quantity, price):
            self.product = product # str
            self.quantity = quantity # int
            self.price = price # float

        def total(self):
            return self.price * self.quantity

        def __repr__(self):
            fmt = "{}({!r}, {!r}, {:.2f})"
            return fmt.format(
                type(self).__name__, self.product, self.quantity, self.price
            )

    def gen_lineitems(count=10):
        length = 5
        i = count
        while i > 0:
            product = ''
            for _ in range(length):
                #product += chr(random.randint(97, 122)) # a ~ z
                product += chr(random.randint(ord('a'), ord('z')))
            quantity = random.randint(1, 19)
            price = random.random() * 20
            yield LineItem(product, quantity, price)
            i -= 1

    # ---------------------------------
    class Order: # the Context
        def __init__(self, customer, cart, promotion=None):
            self.customer = customer
            self.cart = list(cart) # cart -> iterable
            self.promotion = promotion
            #                ---------
            #                function object(callable)

        def total(self):
            if not hasattr(self, '__total'):
                self.__total = sum(item.total() for item in self.cart)
            return self.__total

        def discount(self):
            if not hasattr(self, '__discount'):
                if self.promotion is None:
                    self.__discount = 0.0
                else:
                    self.__discount = self.promotion(self)
                    #                                ----
                    #                             order object
            return self.__discount

        def due(self):
            return self.total() - self.discount()

        def __repr__(self):
            fmt = "{!r}({!r}, {!r}, {!r})"
            return fmt.format(
                type(self).__name__, self.customer, self.cart, self.promotion
            )

        def __str__(self):
            fmt = "{:s}(fidelity={:d})'s order total: {:.2f}, discount: {:.2f}, due: {:.2f}"
            return fmt.format(
                self.customer.name, self.customer.fidelity, self.total(),
                self.discount(), self.due()
            )

    # ---------------------------------
    # - functions for strategy pattern

    promotions = [] # decorator will fill this list!
                    # (1) no need to maintain the function naming
                    # (2) the purpose for function is clear
                    # (3) strategies can be maintained in another module
                    #     (separation -> easy to handle)

    def promotion(func): # decorator
        print("[info] registering {} at import-time ...".format(func.__name__))
        promotions.append(func)
        return func

    @promotion
    def fidelity_promotion(order:'Order') -> float:
        """5% discount for customers with 1000 or more fidelity points"""
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0.0

    @promotion
    def bulkitem_promotion(order:'Order') -> float:
        """10% discount for each LineItem with 20 or more units"""
        discount = 0.0
        for item in order.cart:
            if item.quantity >= 10:
                discount += item.total() * 0.1 # 10% discount
        return discount

    @promotion
    def largeorder_promotion(order:'Order') -> float:
        """7% discount for orders with 10 or more distinct items"""
        distinct_items = {item.product for item in order.cart}
        #                -------------------------------------
        #                need to get list of unique items -> set comprehension
        if len(distinct_items) >= 10:
            return order.total() * 0.07 # 7% discount
        return 0.0

    print('\n# ' + '-' * 76)
    print('# all promotions')
    for i, promotion in enumerate(promotions):
        print('{}. {}'.format(i, promotion))


    # customers
    customers = list(gen_customers(10))
    print('\n# customers')
    for customer in customers:
        print(customer)

    # carts
    carts = list()
    for _ in range(10):
        carts.append(list(gen_lineitems(random.randint(1, 15))))
    print('\n# carts')
    for i, cart in enumerate(carts):
        total = 0.0
        print('\ncart[{}]'.format(i))
        for j, item in enumerate(cart):
            due = item.quantity * item.price
            print('item[{}]= {}, due= {:.2f}'.format(j, item, due))
            total += due
        print('total= {:.2f}'.format(total))

    # shoppings
    print('\n# ' + '-' * 76)
    print('# all shoppings')
    for i, cart in enumerate(carts):
        print('\ncart[{}]'.format(i))
        for customer in customers:
            for promotion in promotions:
                print(
                    Order(customer, cart, promotion),
                    'with', promotion.__name__
                ) #         ------------------
                  #          name of function

    # best shoppings
    print('\n# ' + '-' * 76)
    print('# best shoppings')
    for i, cart in enumerate(carts):
        print('\ncart[{}] - {} items'.format(i, len(cart)))
        for customer in customers:
            # getting the best discount & policy
            discount, policy = max(
                (Order(customer, cart, promotion).discount(), promotion.__name__)
                    for promotion in promotions
            )
            if discount > 0.0:
                print(
                    "{}'s best shopping is {} with discount= {:.2f}"
                    .format(customer, policy, discount)
                )
            else:
                print(
                    "{} is not qualified for any promotion. discount= {:.2f}"
                    .format(customer, discount)
                )
