# vim: ft=python ts=4 sw=4 tw=999 expandtab
# ----------------------------------------------------------------------------
# File : quick_reference_2.py
# Author : yc0325lee
# Created : 2022-03-05 21:49:12 by lee2103
# Modified : 2022-03-05 21:49:12 by lee2103
# Description : 
# Reference
# - Python Cookbook 3rd
# ----------------------------------------------------------------------------

# -------------------------------------
# numbers, dates, and times

# Unpacking a Sequence into Separate Variables
if False:
    data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
    name, shares, price, date = data
    name, shares, price, (year, mon, day) = data
    name, _, _, (year, mon, day) = data # discarding some items, _(throwaway variable)


# Unpacking Elements from Iterables of Arbitrary Length
if True:
    record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
    name, email, *phone_numbers = record
    print(name, email, phone_numbers)
    #                  -------------
    #                      list

if False:
    *trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
    # trailing = [10, 8, 7, 1, 9, 5, 10]
    # current = 3

if False:
    records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4),
    ]
    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)

#  Keeping the Last N Items
if False:
    from collections import deque
    def search(lines, pattern, history=5):
        previous_lines = deque(maxlen=history)
        for line in lines:
            if pattern in line:
                yield line, previous_lines
            previous_lines.append(line)

    if __name__ == '__main__':
        filename = 'somefile.txt'
        with open(filename) as infile:
            for line, prevlines in search(infile, 'python', 5):
                for pline in prevlines:
                    print(pline, end='')
                print(line, end='')
                print('-'*20)

# Finding the Largest or Smallest N Items
if False:
    import heapq
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print("largest_3=", heapq.nlargest(3, nums)) # Prints [42, 37, 23]
    print("smallest_3=", heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

    heap = list(nums)
    heapq.heapify(heap)
    print("heap=", heap)


# -------------------------------------
# strings and text

# 2.1. splitting strings on any of multiple delimiters
if False:
    import re
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    fields = re.split(r'[;,\s]\s*', line)
    print(fields) # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 2.2. matching text at the start or end of a string
if False:
    import os

    for name in os.listdir('.'):
        if name.startswith("lib__") and name.endswith(".py"):
            print("file=", name)

    for name in os.listdir('.'):
        if name.startswith("lib__") and name.endswith((".py", ".png")):
            print("file=", name)                    # ---------------
                                                    #      tuple

# 2.3. matching strings using shell wildcard patterns
# ; like unix shell matching
if False:
    from fnmatch import fnmatch, fnmatchcase
    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py', 'Dat3.CSV']
    for name in names:
        if fnmatch(name, 'Dat*.csv'): # fnmatchcase(name, 'Dat*.csv')
            print(name)

# 2.4. matching and searching for text patterns
if False:
    import re
    inFile = open("input.txt", "r", encoding="utf8")
    pattern = re.compile(r'\d+/\d+/\d+')
    while True:
        line = inFile.readline()
        if line and pattern.match(line): # line.startswith('pattern')
            print(line, end="")          # line.endswith('pattern')
        else:
            break
    inFile.close()

# 2.5. searching and replacing text
if False:
    inFile = open("input.txt", "r", encoding="utf8")
    while True:
        line = inFile.readline()
        if line:
            #print(line, end="")
            print(line.replace('yeah', 'yep'), end="")
        else:
            break
    inFile.close()

if False:
    import re
    inFile = open("input.txt", "r", encoding="utf8")
    pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
    while True:
        line = inFile.readline()
        if line:
            line_ = pattern.sub(r'\3-\1-\2', line)
            print(line, end="")
            print(line_, end="")
        else:
            break
    inFile.close()

# 2.6. searching and replacing case-insensitive text
# ; re.sub('pattern_0', 'pattern_1', text, flags=re.IGNORECASE)

# 2.7. Specifying a Regular Expression for the Shortest Match
if False:
    pattern = re.compile(r'\"(.*)\"') # greedy
    pattern = re.compile(r'\"(.*?)\"') # non-greedy

# 2.11. stripping unwanted characters from strings
# ; str.strip()
# ; str.lstrip()
# ; str.rstrip()

# 2.13. Aligning Text Strings
# ; aligned = text.ljust(20)
# ; aligned = text.rjust(20)
# ; aligned = text.center(20)
# ; aligned = format(text, '>20')
# ; aligned = format(text, '<20')
# ; aligned = format(text, '^20')

# 2.14. combining and concatenating strings
if False:
    parts = ['aaa', 'bbb', 'ccc', 'ddd']
    combined = ','.join(parts) # for csv
    combined = parts[0] + ' ' + parts[1]

    data = ['ACME', 50, 91.1]
    ','.join(str(val) for val in data)

# 2.15. interpolating variables in strings
if False:
    text = '{name} has {n} messages.'
    text.format(name='Guido', n=37)

# 2.16. reformatting text to a fixed number of columns
if False:
    import textwrap
    print(textwrap.fill(text, 78))
    print(textwrap.fill(text, 78, initial_indent='    '))
    print(textwrap.fill(text, 78, subsequent_indent='    '))

    import os
    termwidth = os.get_terminal_size().columns
    print(textwrap.fill(text, termwidth))

# 2.18. tokenizing text
if False:
    import re
    text = 'foo = 23 + 42 * 10'

    NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
    NUM = r'(?P<NUM>\d+)'
    PLUS = r'(?P<PLUS>\+)'
    TIMES = r'(?P<TIMES>\*)'
    EQ = r'(?P<EQ>=)'
    WS = r'(?P<WS>\s+)'

    pattern = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
    scanner = pattern.scanner(text)

    #print(scanner.match())
    #print(scanner.match())
    #print(scanner.match())
    #print(scanner.match())
    #print(scanner.match())
    #print(scanner.match())
    #print(scanner.match())
    #print(scanner.match())
    #print(scanner.match())
    #print(scanner.match())
    #print(scanner.match())
    #print(scanner.match())
    #print(scanner.match())
    #print(scanner.match())

    m = scanner.match()
    while m:
        print(m)
        print(m.lastgroup, m.group()) # doesn't work!
        m = scanner.match()


# -------------------------------------
# numbers, dates, and times

# 3.1. rounding numerical values
# ; round(value, ndigits)

# 3.3. formatting numbers for output
# use format() or str.format()
if False:
    print("dec: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
    print("dec: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))
    print("dec: {0:5d};  hex: {0:#06x};  oct: {0:#08o};  bin: {0:#012b}".format(42))
    print("={0:0.2f}; ={0:>10.1f}; ={0:<10.1f}; ={0:^10.1f}; ={0:0,.1f}".format(1234.56789))

# 3.4. working with binary, octal, and hexadecimal integers
# for complex result of 'sqrt(-1), we need 'import cmath' instead of 'import math'!
if False:
    a = complex(2, 4)
    print("a= {0}, real= {0.real}, imag= {0.imag}".format(a))
    b = 3-5j
    print("b= {0}, real= {0.real}, imag= {0.imag}".format(b))
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(abs(a/b))

    import numpy as np
    a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
    print(a)
    print(a + 3.141592 + 3.141592j)
    print(np.sin(a))

# 3.7. working with infinity and nans
if False:
    a = float('inf')
    b = float('-inf')
    c = float('nan')
    print("inf= {0}, -inf= {1}, nan= {2}".format(float('inf'), float('-inf'), float('nan')))

# 3.8. calculating with fractions
# ; from fractions import Fraction
if False:
    from fractions import Fraction
    a = Fraction(5, 4) # (numerator, denominator)
    b = Fraction(7, 16)
    print(a.numerator, a.denominator)
    print(a, b)
    print(a + b)
    print(a * b)

# 3.9. calculating with large numerical arrays
# use 'numpy'

# 3.11. picking things at random
if False:
    import random
    values = list(range(10))
    for i in range(10):
        print("val=", random.choice(values))
    print()
    for i in range(10):
        print("sample=", random.sample(values, 3))

    print("values=", values)
    random.shuffle(values)
    print("values=", values)

    for i in range(10):
        print("randint=", random.randint(0,9))

    for i in range(10): # uniform floating-point value [0.0, 1.0)
        print("random=", random.random())

    # seeding
    random.seed() # system-time
    random.seed(12345) # fixed seed


# -------------------------------------
# iterators and generators

# 4.1. manually consuming an iterator
if False:
    basket = range(3) # basket itself is not an iterator
    print("basket=", basket)
    print("type=", type(basket))

    print()

    iterator = iter(basket) # invokes basket.__iter__()
    print("item=", next(iterator)) # invokes basket.__next__()
    print("item=", next(iterator))
    print("item=", next(iterator), end="\n\n")
    #print("item=", next(iterator)) # -> StopIteration exception

    print()
    
    iterator = iter(basket) # invokes basket.__iter__()
    try:
        while True:
            print("item=", next(iterator))
    except StopIteration as ex:
        pass

    print()
    
    iterator = iter(basket) # invokes basket.__iter__()
    while True:
        item = next(iterator, None) # None -> sentinel
        if item is None:
            break
        print("item=", item)


# 4.2. delegating iteration in a custom container
if False:
    class Node:
        def __init__(self, value):
            self._value = value
            self._children = []

        def __repr__(self):
            return 'Node({!r})'.format(self._value)

        def add_child(self, node):
            self._children.append(node)

        def __iter__(self):
            return iter(self._children) # returns iter object of a list!!!

        def __len__(self):
            return len(self._children)

    parent = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    child3 = Node(3)
    child4 = Node(4)
    parent.add_child(child1)
    parent.add_child(child2)
    parent.add_child(child3)
    parent.add_child(child4)

    for i, child in enumerate(parent, 1):
        print("child[{}]= {}".format(i, child))

    print()

    print("len(parent)=", len(parent)) # invokes parent.__len__()
    iterator = iter(parent)
    while True:
        item = next(iterator, None) # None -> sentinel
        if item is None:
            break
        print("item=", item)


# 4.3. creating new iteration patterns with generators
if False:
    def some_range(start, stop, increment):
        val = start
        while val < stop:
            yield val # generator!
            val += increment

    for value in some_range(0.0, 4.0, 0.5):
        print("item=", value)

    print()
    
    #iterator = iter(some_range(0.0, 4.0, 0.5)) # ???
    iterator = some_range(0.0, 4.0, 0.5) # ???
    print("iterator=", iterator)
    print("type=", type(iterator))
    while True:
        item = next(iterator, None) # None -> sentinel
        if item is None:
            break
        print("item=", item)
    
    # -------------------------------------------------------------
    # [note]
    # - range() is not an iterator -> iter() required
    # - list() is not an iterator -> iter() required
    # - generator object is an iterator -> iter() not required
    # -------------------------------------------------------------

# 4.9. iterating over all possible combinations or permutations
if False:
    from itertools import permutations, combinations, combinations_with_replacement
    items = ['a', 'b', 'c']

    for permute in permutations(items): # permute(3,3)
        print("permute=", permute)
    print()
    for permute in permutations(items, 2): # permute(3,2)
        print("permute=", permute)
    print()
    for combo in combinations(items, 3): # combo(3,3)
        print("combo=", combo)
    print()
    for combo in combinations(items, 2): # combo(3,2)
        print("combo=", combo)
    print()
    for combo in combinations_with_replacement(items, 3):
        print("combo=", combo)

# 4.10. iterating over the index-value pairs of a sequence
# ; use 'enumerate(sequence)'

# 4.11. iterating over multiple sequences simultaneously
# ;  Iteration stops whenever one of the input sequences is exhausted.
if False:
    xpts = [1, 5, 4, 2, 10, 7]
    ypts = [101, 78, 37, 15, 62, 99]
    for x, y in zip(xpts, ypts):
        print(x, y)

# 4.12. iterating on items in separate containers
# use itertools.chain()
if False:
    from itertools import chain
    a = [1, 2, 3, 4]
    b = ['x', 'y', 'z']
    for x in chain(a, b):
        print(x)


# -------------------------------------
# files and i/o

# 5.11. manipulating pathnames
if False:
    import os

    path = '/users/beazley/Data/data.csv'
    print("path=", path)
    print("basename=", os.path.basename(path))
    print("dirname=", os.path.dirname(path))
    print("joined=", os.path.join(r'\user', 'yclee03', os.path.basename(path)))
    print("splitext=", os.path.splitext(path))

    path = '~/Data/data.csv'
    print("expanded=", os.path.expanduser(path))

# 5.12. testing for the existence of a file
if False:
    import os
    print( os.path.exists('/etc/passwd')              )
    print( os.path.exists('/tmp/spam')                )
    print( os.path.isfile('/etc/passwd')              )
    print( os.path.isdir('/etc/passwd')               )
    print( os.path.islink('/usr/local/bin/python3')   )
    print( os.path.realpath('/usr/local/bin/python3') )
    print( os.path.getsize('/etc/passwd')             )
    print( os.path.getmtime('/etc/passwd')            )
    import time
    print(time.ctime(os.path.getmtime('/etc/passwd')) )

# 5.13. getting a directory listing
# ; os.listdir(dirname)
if False:
    import os
    files = [name for name in os.listdir(".") if os.path.isfile(name)] # files
    dirs = [name for name in os.listdir(".") if os.path.isdir(name)] # directories

    for item in os.listdir("."):
        if os.path.isfile(item):
            print("[file]", item)
        elif os.path.isdir(item):
            print("[dir ]", item)
        else:
            print("[unkn]", item)

    for item in os.listdir("."):
        if item.endswith(".py"):
            print("[python]", item)

    import glob
    for i, item in enumerate(glob.glob(r'D:\WORK\14__python\*.py')):
        print("[{}] {}".format(i, item))

# 5.19. making temporary files and directories
# ; tempfile.TemporaryFile()
# ; tempfile.TemporaryDirectory()
if False:
    from tempfile import TemporaryFile
    with TemporaryFile('w+t') as tempFile:
        tempFile.write('Hello World\n')
        tempFile.write('Testing\n')
        tempFile.seek(0)
        data = tempFile.read()
        print("data=", data)


# -------------------------------------
# functions

# 7.3. attaching informational metadata to function arguments
if False:
    def add(x:int=3, y:int=3) -> int:
        "description: adds two values x and y"
        return x + y

    help(add)
    print(add.__annotations__)

# 7.6. defining anonymous or inline functions
if False:
    names_0 = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
    print("list=", names_0)
    print("type=", type(names_0), end="\n\n")

    names_1 = sorted(names_0, key=lambda name: name.split()[-1].lower())
    print("sorted=", names_1)
    print("type=", type(names_1), end="\n\n")

    names_2 = reversed(names_1)
    print("reversed=", names_2)
    print("type=", type(names_2), end="\n\n")
    
# 7.8. making an n-argument callable work as a callable with fewer arguments
if False:
    def spam(a, b, c, d):
        print(f"a= {a}, b= {b}, c= {c}, d= {d}")
    
    spam(1, 2, 3, 4)

    from functools import partial
    spam_1 = partial(spam, a=1, b=2, c=3)
    spam_1(4)
