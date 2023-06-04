# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : misc__comprehension.py
# - author : yc0325lee
# - created : 2022-10-09 18:35:04 by lee2103
# - modified : 2022-10-09 18:35:04 by lee2103
# - description : 
# - types
#  ; list comprehension
#  ; set comprehension
#  ; dict comprehension
#  ; generator expression
# - generator expression vs comprehension
# ----------------------------------------------------------------------------


if False:
    # list comprehension
    squares = list(map(lambda x: x**2, range(10)))
    squares = [x*x for x in range(10)] # simpler
    print("squares=", squares, end='\n\n')
    # ---------------------------------------------
    # type(codes)= <class 'list'>
    # squares= [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    # ---------------------------------------------

    symbols = 'abcdefghijklmnopqrstuvwxyz'
    codes = [ord(symbol) for symbol in symbols]
    print("codes= [")
    print(*codes[:10])
    print(*codes[10:20])
    print(*codes[20:])
    print("]", end='\n\n')
    # -------------------------------------------
    # codes= [
    #      97  98  99 100 101 102 103 104 105 106
    #     107 108 109 110 111 112 113 114 115 116
    #     117 118 119 120 121 122
    # ]
    # -------------------------------------------

    # excluding 'aeiou'
    codes = [ord(symbol) for symbol in symbols
                         if symbol not in ['a', 'e', 'i', 'o', 'u']]
    print("codes= [")
    print(*codes[:10])
    print(*codes[10:20])
    print(*codes[20:])
    print("]", end='\n\n')
    
    colors = ['black', 'white']
    sizes = ['small', 'medium', 'arge'] # cartesian product
    items = [color + '-' + size
                for color in colors
                    for size in sizes]
    print("items=")
    for item in items:
        print("    ", item)
     # [ 'black-small', 'black-medium', 'black-arge',
     #   'white-small', 'white-medium', 'white-arge' ]


if False:
    # list comprehension
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'clubs diamonds hearts spades'.split() # priority
    print("ranks=", ranks, len(ranks))
    print("suits=", suits, len(suits))

    import collections
    Card = collections.namedtuple('Card', 'rank suit')

    cards = [Card(rank, suit) for suit in suits
                              for rank in ranks]
    for i, card in enumerate(cards):
        print(f"card[{i:2d}]= {card}")
    # card[ 0]= Card(rank='2', suit='clubs')
    # card[ 1]= Card(rank='3', suit='clubs')
    # card[ 2]= Card(rank='4', suit='clubs')
    # card[ 3]= Card(rank='5', suit='clubs')
    # card[ 4]= Card(rank='6', suit='clubs')
    # ... ...
    # card[48]= Card(rank='J', suit='spades')
    # card[49]= Card(rank='Q', suit='spades')
    # card[50]= Card(rank='K', suit='spades')
    # card[51]= Card(rank='A', suit='spades')

    if False:
        # same as the following
        cards = []
        for suit in suits:
            for rank in ranks:
                cards.append(Card(rank, suit))

        for i, card in enumerate(cards):
            print(f"card[{i:2d}]= {card}")


if False:
    # dict comprehension
    # ; curly-braces instead of square brackets
    dial_codes = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]
    lookup = {country.lower(): code for code, country in dial_codes}
    #print("lookup=", lookup)
    print("lookup = {")
    for country, code in lookup.items():
        #print(country, '=>', code)
        print(f"    '{country}' : {code},")
    print("}")

if False:
    # set comprehension
    import random
    chars = {chr(random.randint(97, 122)) for _ in range(128)}
    print("chars=", chars, "len=", len(chars))
    print("type=", type(chars))

if False:
    # generator expression
    symbols = 'abcdefghijklmnopqrstuvwxyz'
    codes = (ord(symbol) for symbol in symbols) # generator object
    print("codes=", codes)

    for Upper, Lower in ((ord(symbol)-32, ord(symbol)) for symbol in symbols):
        print("upper= {}, lower= {}".format(Upper, Lower))

    print("sum=", sum(code-32 for code in codes))
    
    #colors = ['black', 'white']
    #sizes = ['small', 'medium', 'arge'] # cartesian product
    #items = [color + '-' + size for color in colors for size in sizes]
    #print("items=", items)


