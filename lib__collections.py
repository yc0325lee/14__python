# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# File : lib__collections.py
# Author : yc0325lee
# Created : 2022-03-12 21:55:00 by lee2103
# Modified : 2022-03-12 21:55:00 by lee2103
# Description : 
# - specialized container datatypes
#   +--------------+----------------------------------------------------------------------+
#   | type         | description                                                          |
#   +--------------+----------------------------------------------------------------------+
#   | namedtuple() | factory function for creating tuple subclasses with named fields     |
#   | deque        | list-like container with fast appends and pops on either end         |
#   | ChainMap     | dict-like class for creating a single view of multiple mappings      |
#   | Counter      | dict subclass for counting hashable objects                          |
#   | OrderedDict  | dict subclass that remembers the order entries were added            |
#   | defaultdict  | dict subclass that calls a factory function to supply missing values |
#   | UserDict     | wrapper around dictionary objects for easier dict subclassing        |
#   | UserList     | wrapper around list objects for easier list subclassing              |
#   | UserString   | wrapper around string objects for easier string subclassing          |
#   +--------------+----------------------------------------------------------------------+
# ----------------------------------------------------------------------------
import collections
import pprint


if False:
    # -------------------------------------
    # - collections.namedtuple(
    #     typename, field_names, *, rename=False, defaults=None, module=None
    # )
    # ; returns a new tuple subclass named typename
    # ; the new subclass is used to create tuple-like objects that have fields
    #    accessible by attribute lookup as well as being indexable and iterable.
    # ; factory function for creating tuple subclasses with named fields
    # ; used to build classes of objects that are just bundles of attributes with
    #   no custom methods
    # ; built-in tuple attributes and method + additional 3 methods and 2 attributes
    #   -> classmethod somenamedtuple._make(iterable)
    #   -> somenamedtuple._asdict()
    #   -> somenamedtuple._replace(**kwargs)
    #   -> somenamedtuple._fields
    #   -> somenamedtuple._field_defaults
    Point = collections.namedtuple('Point', ['x', 'y'])
          # collections.namedtuple('Point', 'x y')
          # collections.namedtuple('Point', 'x, y')
    p = Point(x=3, y=4)

    # accessing by name
    print("p=", p)          # p= Point(x=3, y=4)
    print("type=", type(p)) # type= <class '__main__.Point'>
    print("p.x=", p.x)      # p.x= 3
    print("p.y=", p.y)      # p.y= 4

    # accessing like tuple - indexible
    for i, item in enumerate(p):
        print(f"item[{i}]= {item}")

    print("p[0] + p[1] =", p[0] + p[1])
    
    # tuple unpacking allowed
    x, y = p
    print("x=", x) # x= 3
    print("y=", y) # y= 4

    # classmethod somenamedtuple._make(iterable)
    # ; makes a new instance from an existing sequence or iterable
    coords = [5, 6]
    p = Point._make(coords)
    print("Point._make(coords)=", p)
    # Point._make(coords)= Point(x=5, y=6)

    # somenamedtuple._asdict()
    # ; return a new built-in dict which maps field names to their corresponding values
    print("p._asdict()=", p._asdict())
    # p._asdict()= {'x': 5, 'y': 6}

    # somenamedtuple._fields
    # ; tuple of strings listing the field names, for inspection
    print("p._fields=", p._fields)

if False:
    # -------------------------------------
    # - somenamedtuple._fields
    # ; useful for creating new named tuple types from existing named tuples.
    Point = collections.namedtuple('Point', 'x y')
    Color = collections.namedtuple('Color', 'red green blue')
    Pixel = collections.namedtuple('Pixel', Point._fields + Color._fields)
    #                                       -------------   -------------
    #                                       ('x', 'y')    + ('red', 'green', 'blue')

    print("Point._fields=", Point._fields)
    print("Color._fields=", Color._fields)
    print("Pixel._fields=", Pixel._fields)
    # Point._fields= ('x', 'y')
    # Color._fields= ('red', 'green', 'blue')
    # Pixel._fields= ('x', 'y', 'red', 'green', 'blue')

if False:
    # -------------------------------------
    # - example of namedtuple
    Card = collections.namedtuple('Card', ['rank', 'suit'])

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    # list comprehension
    cards = [Card(rank, suit) for suit in suits
                              for rank in ranks]
    for card in cards:
        print("card=", card, type(card), card.rank, card.suit)
        #              ----  ----------  ---------  ---------

    rank, suit = cards[13]
    print(cards[13][0]) # card[13].rank
    print(cards[13][1]) # card[13].suit
    print(cards[13].rank)
    print(cards[13].suit)


if False:
    #-------------------------------------------------------------------------
    # - class collections.deque([iterable[, maxlen]])
    # ; list-like container with fast appends and pops on either end
    #   (doubly-linked-list)
    # ; returns a new deque object initialized left-to-right (using append())
    #   with data from iterable.
    # ; if iterable is not specified, the new deque is empty.
    # ; if maxlen is not specified or is none, deques may grow to an arbitrary length.
    #   otherwise, the deque is bounded to the specified maximum length.
    # ; when new items are added and the queue is full, the oldest item is
    #   automatically removed(when maxlen is specified)
    # ; problem of built-in list
    #   -> inserting and removing from the left of a list is costly(not efficient)
    #     (the 0-index end using pop(0))
    # ; double-ended queue (doubly linked-list)
    # ; append(x) and appendleft(x)
    #   add x to the right(left) side of the deque.
    # ; extend(iterable) and extendleft(iterable)
    #   extend the right side of the deque by appending elements from the iterable argument.
    # ; pop() and popleft()
    #   remove and return an element from the right(left) side of the deque.
    #-------------------------------------------------------------------------
    queue = collections.deque(range(10), maxlen=10); print("queue=", queue) # fixed-size
    # queue= deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

    queue.rotate(3); print("queue=", queue)
    # queue= deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)

    queue.rotate(-4); print("queue=", queue)
    # queue= deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)

    queue.appendleft(-1); print("queue=", queue)
    # queue= deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

    queue.extend([11, 22, 33]); print("queue=", queue)
    # queue= deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)

    queue.extendleft([10, 20, 30, 40]); print("queue=", queue)
    # queue= deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)


if False:
    # -------------------------------------
    # - class collections.defaultdict(default_factory=None, /[, ...])
    # ; dict subclass that calls a factory function to supply missing values
    # ; default_factory
    #   this attribute is used by the __missing__() method; it is initialized
    #   from the first argument to the constructor, if present, or to none, if
    #   absent.
    s = [
            ('yellow', 1),
            ('blue',   2),
            ('yellow', 3),
            ('blue',   4),
            ('red',    1),
        ] # sequence of pairs

    d = collections.defaultdict(list) # default_factory=list
    for key, val in s:
        d[key].append(val) # if d[key] not exists, it'll be defaulted using
                           # default_factory=list
    s = 'mississippi'
    d = defaultdict(int) # default_factory=int -> zero
    for key in s:
        d[key] += 1


if False:
    # -------------------------------------
    # - class collections.UserList([list])
    # ; class that simulates a list
    class CustomizedList(collections.UserList):
        pass

    values = CustomizedList()
    for val in range(3, 10):
        values.append(val)
    for i in range(len(values)):
        print(f"values[{i}] = {values[i]}")

if False:
    # -------------------------------------
    # - class collections.Counter([iterable-or-mapping])
    # ; a counter is a dict subclass for counting hashable objects. it is a
    #   collection where elements are stored as dictionary keys and their counts
    #   are stored as dictionary values.
    pass


if True:
    # -------------------------------------
    # - class collections.ChainMap(*maps)
    # ; a ChainMap groups multiple dicts or other mappings together to create
    #   a single, updateable view.
    a = {'x':1, 'z':3}
    b = {'y':2, 'z':4}
    combined = collections.ChainMap(a, b)

    print("\n# before update")
    for key in combined.keys():
        val = combined[key]
        print(f"combined[{key}]= {val}")
    # combined[y]= 2
    # combined[z]= 3
    # combined[x]= 1

    a['x'] = 5
    b['w'] = 6 # 'combined' will be updated also!

    print("\n# after update")
    for key in combined.keys():
        val = combined[key]
        print(f"combined[{key}]= {val}")
    # combined[y]= 2
    # combined[z]= 3
    # combined[w]= 6
    # combined[x]= 5


if False:
    # -------------------------------------
    # - class collections.OrderedDict([items])
    # ; return an instance of a dict subclass that has methods specialized for
    #   rearranging dictionary order.
    # - popitem(last=True)
    # ; the popitem() method for ordered dictionaries returns and removes a
    #   (key, value) pair. the pairs are returned in lifo order if last is true
    #   or fifo order if false.
    pass
