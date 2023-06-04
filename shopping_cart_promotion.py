# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : shopping_cart_promotion.py
# - author : yc0325lee
# - created : 2022-10-16 22:18:47 by lee2103
# - modified : 2022-10-16 22:18:47 by lee2103
# - description : 
# ----------------------------------------------------------------------------

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
        self.funcname = str()

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount, self.funcname = 0.0, None
        else:
            discount, self.funcname = self.promotion(self)
            #                         --------------------
            #                         function call with order argument
        print("[debug] type(discount)=", type(discount))
        print("[debug] discount=", discount)
        return self.total() - discount

    def __repr__(self):
        fmt = "total: {:.2f} due: {:.2f} with {:s}"
        return fmt.format(self.total(), self.due(), self.funcname)

def fidelity_promotion(order:'Order') -> float:
    """5% discount for customers with 1000 or more fidelity points"""
    #return order.total() * .05 if order.customer.fidelity >= 1000 else 0, fidelity_promotion.__name__
    if order.customer.fidelity >= 1000:
        return order.total() * .05, fidelity_promotion.__name__
    else:
        return 0.0, fidelity_promotion.__name__


def bulkitem_promotion(order:'Order') -> float:
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount, bulkitem_promotion.__name__

def largeorder_promotion(order:'Order') -> float:
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    #                -------------------------------------
    #                need to get list of unique items -> get comprehension
    if len(distinct_items) >= 10:
        return order.total() * .07, largeorder_promotion.__name__
    return 0.0, largeorder_promotion.__name__


if __name__ == '__main__':
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
    #def best_promotion(order):
    #    """select best discount available"""
    #    return max(promotion(order) for promotion in promotions)
    #    #          --------------------------------------------
    #    #                      generator expression

    def best_promotion(order):
        """select best discount available"""
        func_val = sorted(
            ((promotion, promotion(order)) for promotion in promotions),
            key=lambda pair: pair[1]
        )[-1] # promotion that gives the largest discount
        #  |  |
        #  |  function object
        #  maximum
        print("[xxx]", func_val)
        return discount, function.__name__
    
    for customer in customers:
        print("\n# {}'s best shopping".format(customer.name))
        for i, cart in enumerate(carts, 1):
            print("cart{}".format(i), Order(customer, cart, best_promotion))

    # ----------------------------------------------------------------
    # failure!!! 221016_231243
    # how can I retrieve both best promotion and corresponding policy?
    # ----------------------------------------------------------------
