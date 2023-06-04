#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : 01_18_mapping_names_to_sequence_elements.py
# - author : yc0325lee
# - created : 2022-11-20 13:43:35 by yc032
# - modified : 2022-11-20 13:43:35 by yc032
# - description : 
# ----------------------------------------------------------------------------

if False:
    import collections

    Subscriber = collections.namedtuple('Subscriber', ['addr','joined'])
    someone = Subscriber('jonesy@example.com', '2012-10-19')

    print('someone=', someone)
    print('someone.addr =', someone.addr)
    print('someone.joined =', someone.joined)
    print('someone[0] =', someone[0])
    print('someone[1] =', someone[1])
    print('len(someone) =', len(someone))

    addr, joined = someone # tuple unpacking
    print('addr =', addr)
    print('joined =', joined)


if False:
    import collections
    Stock = collections.namedtuple('Stock',['name','shares','price'])

    # (1) depending on indices
    def compute_cost_0(records):
        total = 0
        for record in records:
            total += record[1] * record[2]
            #        ---------   ---------
            #         shares       price
        return total

    # (2) using collections.namedtuple
    # ; immutable
    def compute_cost_1(records):
        total = 0
        for record in records:
            stock = Stock(*records)
            total += stock.shares * stock.price
        return total



    stock = Stock('ACME', 100, 123.45)
    print('stock =', stock)
    #stock.shares = 75 # AttributeError: can't set attribute

    stock = stock._replace(shares=75) # using _replace()
    print('stock =', stock)


if True:
    import collections

    Stock = collections.namedtuple('Stock',['name','shares','price','date','time'])
    initializer = Stock('', 0, 0.0, None, None)

    def dict_to_stock(s):
        return initializer._replace(**s)


    a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
    print('a =', dict_to_stock(a))
    b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
    print('b =', dict_to_stock(b))

    #-------------------------------------------------------------------------
    # [note]
    # in case you have to change instance attributes frequently,
    # namedtuple is not the best choice.
    # you had better consider using __slots__ instead
    #-------------------------------------------------------------------------
