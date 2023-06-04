# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# File : quick_reference_0.py
# Description : 
# Author : yc0325lee
# Created : 2021-07-17 14:17:31 by lee2103
# Modified : 2021-07-17 14:17:31 by lee2103
# ----------------------------------------------------------------------------
# References
#     https://docs.python.org/3/ - Python 3.9.6 documentation
# 
# Table of Contents:
#     imports
#     data types
#     math
#     comparisons and boolean operations
#     conditional statements
#     lists
#     tuples
#     strings
#     dictionaries
#     sets
#     defining functions
#     anonymous (lambda) functions
#     built-in functions
#     for loops and while loops
#     comprehensions
#     map and filter
# 
# Comments
#     pythonì—ì„œì˜ ë³€ìˆ˜ë“¤ì€ ë¬´ì¡°ê±´ handle(dataë¥¼ ì €ìž¥í•˜ê³  ìžˆëŠ” memoryë¥¼ ê°€ë¦¬í‚¤ëŠ”)ìž„



### -----------------------------------
### imports ###
#
# 1) importing module or attributes of a module
#   ; import mod
#   ; import mod1, mod2
#   ; import mod as alias
#   ; from mod import attr
#   ; from mod import attr1, attr2
#   ; from mod import *
#   ; from mod import attr as alias
#   ; from mod import attr1 as alias1, attr2 as alias2, attr3 as alias3
#
# 2) importing module or attributes of a module in packages
#   ; import pkg.mod
#   ; import pkg.mod1, pkg.mod2
#   ; import pkg.mod1.attr1
#   ; import pkg.mod1 as alias1, pkg.mod2 as alias2
#   ; from pkg.mod import attr
#   ; from pkg.mod import attr1, attr2, attr3
#   ; from pkg.mod import attr as alias
#   ; from pkg.mod import attr1 as alias1, attr2 as alias2, att3 as alias3

if False:
    # 'generic import' of math module
    import math
    math.sqrt(25)

    # import a function
    from math import sqrt
    sqrt(25)    # no longer have to reference the module

    # import multiple functions at once
    from math import cos, floor

    # import all functions in a module (generally discouraged)
    from csv import *

    # define an alias
    import datetime as dt


# show all functions in math module
# - dir([object])
#  ; Without arguments, return the list of names in the current local scope.
#  ; With an argument, attempt to return a list of valid attributes for that object.
if False:
    print(dir(math))
    for name in dir(math):
        print("name= {}".format(name))

# executing a module as script
if False:
    if __name__ == "__main__":
        import sys
        do_something(sys.argv[1])

# import searching order
# 1) built-in module
# 2) directories in sys.path
#   ; current directory
#   ; $PYTHONPATH
#   ; install-path

# adding module search path
if False:
    import sys
    sys.path.append("some_path")

# package example
# sound/                          Top-level package
#       __init__.py               Initialize the sound package
#       formats/                  Subpackage for file format conversions
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  Subpackage for sound effects
#               __init__.py
#               echo.py           include echofilter()
#               surround.py
#               reverse.py
#               ...
#       filters/                  Subpackage for filters
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#               ...

#import sound.effects.echo # importing 'echo' module
#sound.effects.echo.echofilter()

#from sound.effects import echo # importing 'echo' module
#echo.echofilter()

#from sound.effects.echo import echofilter # importing a function
#echofilter()

# 'from sound.effects import *'ë¡œ íŠ¹ì • directory(package)ì˜ moduleë“¤ì„ import
# í•˜ê¸° ìœ„í•´ì„œëŠ” ...
# -> '__init__.py' fileë‚´ì— '__all__' listì— moduleë“¤ì´ ëª…ì‹œë˜ì–´ì•¼ í•¨
# __all__ = ["echo", "surround", "reverse"]

#from sound.effects import *
# will import moudles in __all__ list variable!


### -----------------------------------
### data types ###
# - Text     Type:  str
# - Numeric  Types: int, float, complex
# - Sequence Types: list, tuple, range
# - Mapping  Type:  dict
# - Set      Types: set, frozenset
# - Boolean  Type:  bool
# - Binary   Types: bytes, bytearray, memoryview

if False:
    # determine/check the type of an object
    type(2)         # returns 'int'
    type(2.0)       # returns 'float'
    type('two')     # returns 'str'
    type(True)      # returns 'bool'
    type(None)      # returns 'NoneType'
    
    # check if an object is of a given type
    isinstance(2.0, int)            # returns False
    isinstance(2.0, (int, float))   # returns True
    
    # convert an object to a given type
    float(2)
    int(2.9)
    str(2.9)
    
    # zero, None, and empty containers are converted to 'False'
    bool(0)
    bool(None)
    bool('')    # empty string
    bool([])    # empty list
    bool({})    # empty dictionary
    
    # non-empty containers and non-zeros are converted to 'True'
    bool(2)
    bool('two')
    bool([2])



### -----------------------------------
### math ###

# arithmetic operators
# +----+-----------------------------------------------------------+--------+
# |    | description                                               | x + y  |
# +----+-----------------------------------------------------------+--------+
# | +  | Addition: adds two operands                               | x + y  |
# | -  | Subtraction: subtracts two operands                       | x - y  |
# | *  | Multiplication: multiplies two operands                   | x * y  |
# | /  | Division (float): divides the first operand by the second | x / y  |
# | // | Division (floor): divides the first operand by the second | x // y |
# | %  | Modulus: returns the remainder when first operand is      | x % y  |
# |    |          divided by the second                            |        |
# | ** | Power : Returns first raised to power second              | x ** y |
# +----+-----------------------------------------------------------+--------+

# relational operators
# +----------+--------------------------------------------------------------+--------+
# | Operator | Description                                                  | Syntax |
# +----------+--------------------------------------------------------------+--------+
# | >        | Greater than: True if left operand is greater than the right | x > y  |
# | <        | Less than: True if left operand is less than the right       | x < y  |
# | ==       | Equal to: True if both operands are equal                    | x == y |
# | !=       | Not equal to - True if operands are not equal                | x != y |
# | >=       | Greater than or equal to: True if left operand is greater    | x >= y |
# |          |  than or equal to the right                                  |        |
# | <=       | Less than or equal to: True if left operand is less than     | x <= y |
# |          |  or equal to the right                                       |        |
# +----------+--------------------------------------------------------------+--------+

# logical operators
# +----------+----------------------------------------------------+---------+
# | Operator | Description                                        | Syntax  |
# +----------+----------------------------------------------------+---------+
# | and      | Logical AND: True if both the operands are true    | x and y |
# | or       | Logical OR: True if either of the operands is true | x or y  |
# | not      | Logical NOT: True if operand is false              | not x   |
# +----------+----------------------------------------------------+---------+

# bitwise operators
# +----------+---------------------+--------+
# | Operator | Description         | Syntax |
# +----------+---------------------+--------+
# | &        | Bitwise AND         | x & y  |
# | |        | Bitwise OR          | x | y  |
# | ~        | Bitwise NOT         | ~x     |
# | ^        | Bitwise XOR         | x ^ y  |
# | >>       | Bitwise right shift | x >>   |
# | <<       | Bitwise left shift  | x <<   |
# +----------+---------------------+--------+

# ternary operator - ?: in c
# a, b = 10, 20
# min = a if a < b else b # ternary operator

# assignment operators
# +----------+----------------------------------------------------------------+--------------------------------------+
# | Operator | Description                                                    | Syntax                               |
# +----------+----------------------------------------------------------------+--------------------------------------+
# | =        | Assign value of right side of expression to left side operand  | x = y + z                            |
# | +=       | Add AND: Add right side operand with left side operand and then| a+=b     a=a+b                       |
# | -=       | Subtract AND: Subtract right operand from left operand and then| a-=b     a=a-b                       |
# | *=       | Multiply AND: Multiply right operand with left operand and then| a*=b     a=a*b                       |
# | /=       | Divide AND: Divide left operand with right operand and then ass| a/=b     a=a/b                       |
# | %=       | Modulus AND: Takes modulus using left and right operands and as| a%=b     a=a%b                       |
# | //=      | Divide(floor) AND: Divide left operand with right operand and t| a//=b    a=a//b                      |
# | **=      | Exponent AND: Calculate exponent(raise power) value using opera| a**=b    a=a**b                      |
# | &=       | Performs Bitwise AND on operands and assign value to left opera| a&=b     a=a&b                       |
# | |=       | Performs Bitwise OR on operands and assign value to left operan| a|=b     a=a|b                       |
# | ^=       | Performs Bitwise xOR on operands and assign value to left opera| a^=b     a=a^b                       |
# | >>=      | Performs Bitwise right shift on operands and assign value to le| a>>=b    a=a>>b                      |
# | <<=      | Performs Bitwise left shift on operands and assign value to lef| a <<= b  a= a << b                   |
# +----------+----------------------------------------------------------------+--------------------------------------+

# - identity operators - special
# +--------+----------------------------------------+
# | is     | True if the operands are identical     |
# +--------+----------------------------------------+
# | is not | True if the operands are not identical |
# +--------+----------------------------------------+
# - equality operator (==) compares the values of both the operands and checks
#   for value equality.
# - the 'is' operator checks whether both the operands refer to the same object or not.
#   id(a) vs id(b)

# - membership(containment) operators - special
# +--------+--------------------------------------------+
# | in     | True if value is found in the sequence     |
# +--------+--------------------------------------------+
# | not in | True if value is not found in the sequence |
# +--------+--------------------------------------------+

# basic operations
# 10 + 4          # add (returns 14)
# 10 - 4          # subtract (returns 6)
# 10 * 4          # multiply (returns 40)
# 10 ** 4         # exponent (returns 10000)
# 5 % 4           # modulo (returns 1) - computes the remainder
# 10 / 4          # divide (returns 2 in Python 2, returns 2.5 in Python 3)
# 10 / float(4)   # divide (returns 2.5)
# 
# # force '/' in Python 2 to perform 'true division' (unnecessary in Python 3)
# from __future__ import division
# 10 / 4          # true division (returns 2.5)
# 10 // 4         # floor division (returns 2)



### -----------------------------------
### comparisons and boolean operations ###

# assignment statement
# x = 5

# comparisons (these return True)
# x > 3
# x >= 3
# x != 3
# x == 5

# boolean operations (these return True)
# 5 > 3 and 6 > 3
# 5 > 3 or 5 < 3
# not False
# False or not False and True     # evaluation order: not, and, or



### -----------------------------------
### CONDITIONAL STATEMENTS ###
if False:
    # if statement
    if x > 0:
        print('positive')
    
    # if/else statement
    if x > 0:
        print('positive')
    else:
        print('zero or negative')
    
    # if/elif/else statement
    if x > 0:
        print('positive')
    elif x == 0:
        print('zero')
    else:
        print('negative')
    
    # single-line if statement (sometimes discouraged)
    if x > 0: print('positive')
    
    # single-line if/else statement (sometimes discouraged)
    # known as a 'ternary operator'
    result = 'positive' if x > 0 else 'zero or negative'



### -----------------------------------
### LISTS ###
## properties: ordered, iterable, mutable, can contain multiple data types
if False:
    # create an empty list (two ways)
    empty_list = []
    empty_list = list()
    
    # create a list
    simpsons = ['homer', 'marge', 'bart']
    
    # examine a list
    simpsons[0]     # print element 0 ('homer')
    len(simpsons)   # returns the length (3)

    # modify a list (does not return the list)
    simpsons.append('lisa')                 # append element to end
    simpsons.extend(['itchy', 'scratchy'])  # append multiple elements to end
    simpsons.insert(0, 'maggie')            # insert element at index 0 (shifts everything right)
    simpsons.remove('bart')                 # search for first instance and remove it
    simpsons.pop(0)                         # remove element 0 and return it
    del simpsons[0]                         # remove element 0 (does not return it)
    simpsons[0] = 'krusty'                  # replace element 0

    # concatenate lists (slower than 'extend' method)
    neighbors = simpsons + ['ned', 'rod', 'todd']
    
    # find elements in a list
    simpsons.count('lisa')      # counts the number of instances
    simpsons.index('itchy')     # returns index of first instance

if False:
    # list slicing [start:end:step]
    weekdays = ['mon', 'tues', 'wed', 'thurs', 'fri']
    weekdays[0]         # element 0
    weekdays[0:3]       # elements 0, 1, 2
    weekdays[:3]        # elements 0, 1, 2
    weekdays[3:]        # elements 3, 4
    weekdays[-1]        # last element (element 4)
    weekdays[::2]       # every 2nd element (0, 2, 4)
    weekdays[::-1]      # backwards (4, 3, 2, 1, 0)

    # alternative method for returning the list backwards
    list(reversed(weekdays))

    # sort a list in place (modifies but does not return the list)
    simpsons.sort()
    simpsons.sort(reverse=True)     # sort in reverse
    simpsons.sort(key=len)          # sort by a key
    
    # return a sorted list (does not modify the original list)
    sorted(simpsons)
    sorted(simpsons, reverse=True)
    sorted(simpsons, key=len)
    
    # insert into an already sorted list, and keep it sorted
    num = [10, 20, 40, 50]
    from bisect import insort
    insort(num, 30)
    
    # create a second reference to the same list
    same_num = num
    same_num[0] = 0         # modifies both 'num' and 'same_num'
    
    # copy a list (two ways)
    new_num = num[:]
    new_num = list(num)
    
    # examine objects
    num is same_num         # returns True (checks whether they are the same object)
    num is new_num          # returns False
    num == same_num         # returns True (checks whether they have the same contents)
    num == new_num          # returns True
    
    # looping on list or tuple
    for member in neighbors:
        print("name= {}".format(member))


### -----------------------------------
### TUPLES ###
## properties: ordered, iterable, immutable, can contain multiple data types
## like lists, but they don't change size
if False:
    # create a tuple
    digits = (0, 1, 'two')          # create a tuple directly
    digits = tuple([0, 1, 'two'])   # create a tuple from a list
    zero = (0,)                     # trailing comma is required to indicate it's a tuple
    
    # examine a tuple
    digits[2]           # returns 'two'
    len(digits)         # returns 3
    digits.count(0)     # counts the number of instances of that value (1)
    digits.index(1)     # returns the index of the first instance of that value (1)
    
    # elements of a tuple cannot be modified
    digits[2] = 2       # throws an error
    
    # concatenate tuples
    digits = digits + (3, 4)
    
    # create a single tuple with elements repeated (also works with lists)
    (3, 4) * 2          # returns (3, 4, 3, 4)
    
    # sort a list of tuples
    tens = [(20, 60), (10, 40), (20, 30)]
    sorted(tens)        # sorts by first element in tuple, then second element
                        #   returns [(10, 40), (20, 30), (20, 60)]
    
    # tuple unpacking
    bart = ('male', 10, 'simpson')  # create a tuple
    (sex, age, surname) = bart      # assign three values at once
    
    # the followings are all the same!
    a, b   =   'AAA', 'BBB'
    a, b   = ( 'AAA', 'BBB' ); # tupleì„ ì‚¬ìš©í•œ value assignment!
    ( a, b ) = ( 'AAA', 'BBB' )
    name, age, sex, hobby   =   "yclee", 46, "male", "coding"
    ( name, age, sex, hobby ) = ( "yclee", 46, "male", "coding" ) # same!


### -----------------------------------
### STRINGS ###
## properties: iterable, immutable
if False:
    # create a string
    s = str(42)         # convert another data type into a string
    s = 'I like you'
    
    # examine a string
    s[0]                # returns 'I'
    len(s)              # returns 10
    
    # string slicing is like list slicing
    s[:6]               # returns 'I like'
    s[7:]               # returns 'you'
    s[-1]               # returns 'u'
    
    # basic string methods (does not modify the original string)
    s.lower()           # returns 'i like you'
    s.upper()           # returns 'I LIKE YOU'
    s.startswith('I')   # returns True
    s.endswith('you')   # returns True
    s.isdigit()         # returns False (returns True if every character in the string is a digit)
    s.find('like')      # returns index of first occurrence (2), but doesn't support regex
    s.find('hate')      # returns -1 since not found
    s.replace('like', 'love')    # replaces all instances of 'like' with 'love'
    
    # split a string into a list of substrings separated by a delimiter
    s.split(' ')        # returns ['I', 'like', 'you']
    s.split()           # equivalent (since space is the default delimiter)
    s2 = 'a, an, the'
    s2.split(',')       # returns ['a', ' an', ' the']
    
    # join a list of strings into one string using a delimiter
    stooges = ['larry', 'curly', 'moe']
    ' '.join(stooges)   # returns 'larry curly moe'
    
    # concatenate strings
    s3 = 'The meaning of life is'
    s4 = '42'
    s3 + ' ' + s4       # returns 'The meaning of life is 42'
    
    # remove whitespace from start and end of a string
    s5 = '  ham and cheese  '
    s5.strip()          # returns 'ham and cheese'
    
    # string substitutions: all of these return 'raining cats and dogs'
    'raining %s and %s' % ('cats', 'dogs')                       # old way
    'raining {} and {}'.format('cats', 'dogs')                   # new way
    'raining {arg1} and {arg2}'.format(arg1='cats', arg2='dogs') # named arguments
    
    # string formatting
    # more examples: https://mkaz.blog/code/python-string-format-cookbook/
    'pi is {:.2f}'.format(3.14159)      # returns 'pi is 3.14'
    
    # normal strings versus raw strings
    print('first line\nsecond line')    # normal strings allow for escaped characters
    print(r'first line\nfirst line')    # raw strings treat backslashes as literal characters
    
    # multi-line string
    multiline="""
    Life is too short
    You need python
    """
    multiline='''
    Life is too short
    You need python
    '''
    
    # writing header - concatenation & multiplication
    print( "# " + "-" * 76 )
    print( "# " + "Title : ")
    print( "# " + "-" * 76 )


### -----------------------------------
### dictionary or dictionaries ###
## properties: unordered, iterable, mutable, can contain multiple data types
## made of key-value pairs
## keys must be unique, and can be strings, numbers, or tuples
## values can be any type
if False:
    # create an empty dictionary (two ways)
    empty_dict = {}
    empty_dict = dict()
    
    # create a dictionary (two ways)
    family = {'dad':'homer', 'mom':'marge', 'size':6}
    family = dict(dad='homer', mom='marge', size=6)
    
    # convert a list of tuples into a dictionary
    list_of_tuples = [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]
    family = dict(list_of_tuples)
    
    # examine a dictionary
    family['dad']       # returns 'homer'
    len(family)         # returns 3
    'mom' in family     # returns True
    'marge' in family   # returns False (only checks keys)
    
    # returns a list (Python 2) or an iterable view (Python 3)
    family.keys()       # keys: ['dad', 'mom', 'size']
    family.values()     # values: ['homer', 'marge', 6]
    family.items()      # key-value pairs: [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]
    
    # modify a dictionary (does not return the dictionary)
    family['cat'] = 'snowball'              # add a new entry
    family['cat'] = 'snowball ii'           # edit an existing entry
    del family['cat']                       # delete an entry
    family['kids'] = ['bart', 'lisa']       # dictionary value can be a list
    family.pop('dad')                       # remove an entry and return the value ('homer')
    family.update({'baby':'maggie', 'grandpa':'abe'})   # add multiple entries
    
    # access values more safely with 'get'
    family['mom']                       # returns 'marge'
    family.get('mom')                   # equivalent
    family['grandma']                   # throws an error since the key does not exist
    family.get('grandma')               # returns None instead
    family.get('grandma', 'not found')  # returns 'not found' (the default)
    
    # access a list element within a dictionary
    family['kids'][0]                   # returns 'bart'
    family['kids'].remove('lisa')       # removes 'lisa'
    
    # string substitution using a dictionary
    'youngest child is %(baby)s' % family   # returns 'youngest child is maggie'
    
    # operation and looping
    if "mom" in family:
        print("mon's name is {}".format(family['mom']))
    
    for key in family.keys():
        print("key= {}, value= {}".format(key, family[key]))
    
    for val in family.values():
        print("value=", val)
    
    for key, value in family.items():
        print("key= {}, value= {}".format(key, valiue))


### -----------------------------------
### sets ###
## properties: unordered, iterable, mutable, can contain multiple data types
## made of unique elements (strings, numbers, or tuples)
## like dictionaries, but with keys only (no values)
if False:
    # create an empty set
    empty_set = set()
    
    # create a set
    languages = {'python', 'r', 'java'}         # create a set directly
    snakes = set(['cobra', 'viper', 'python'])  # create a set from a list
    
    # examine a set
    len(languages)              # returns 3
    'python' in languages       # returns True
    
    # set operations
    languages & snakes          # returns intersection: {'python'}
    languages | snakes          # returns union: {'cobra', 'r', 'java', 'viper', 'python'}
    languages - snakes          # returns set difference: {'r', 'java'}
    snakes - languages          # returns set difference: {'cobra', 'viper'}
    
    # modify a set (does not return the set)
    languages.add('sql')        # add a new element
    languages.add('r')          # try to add an existing element (ignored, no error)
    languages.remove('java')    # remove an element
    languages.remove('c')       # try to remove a non-existing element (throws an error)
    languages.discard('c')      # remove an element if present, but ignored otherwise
    languages.pop()             # remove and return an arbitrary element
    languages.clear()           # remove all elements
    languages.update(['go', 'spark'])  # add multiple elements (can also pass a set)
    
    # get a sorted list of unique elements from a list
    for item in sorted(set([9, 0, 2, 1, 0])): # returns [0, 1, 2, 9]
        print("item=", item)



### -----------------------------------
### defining functions ###
# - if no 'return value' statement, 'None' returned
# - multiple value return -> function ¿ÜºÎ·Î tupleÀÌ Àü´ÞµÊ
# - ¸Å°³º¯¼ö(parameter) vs ÀÎ¼ö(arguments)
# - 'global' to access global variable inside a function
# - return value°¡ »ý·«µÇ¸é 'None'ÀÌ returnµÊ
# - multiple valueµéÀÌ return½Ã tuple·Î Àü´ÞµÊ
if False:
    # define a function with no arguments and no return values
    def print_text():
        print('this is text')
    
    # call the function
    print_text()
    
    # define a function with one argument and no return values
    def print_this(x):
        print(x)
    
    # call the function
    print_this(3)       # prints 3
    n = print_this(3)   # prints 3, but doesn't assign 3 to n
                        #   because the function has no return statement
    
    # define a function with one argument and one return value
    def square_this(x):
        return x**2
    
    # include an optional docstring to describe the effect of a function
    def square_this(x):
        """Return the square of a number."""
        return x**2
    
    # call the function
    square_this(3)          # prints 9
    var = square_this(3)    # assigns 9 to var, but does not print 9
    
if False:
    # function definition with parameters and docstring
    def SomeFunc(name, age, sex):
        "SomeFunc() : prints information of a persion" # docstring
        print("name= %s, age= %d, sex= %s" % (name, age, sex))

    SomeFunc("james", 29, "male") # invoking functions with positional arguments
    SomeFunc(sex="male", name="james", age=29) # invoking functions with keyword arguments

if False:
    # with default arguments
    def SomeFunc(name = "anonymous", age = 20, sex = "female"):
        "SomeFunc() : prints information of a persion" # docstring
        print("name= %s, age= %d, sex= %s" % (name, age, sex))
    
    print(SomeFunc.__doc__) # prints docstring of 'SomeFunc'
    SomeFunc() # invoking functions
    SomeFunc("james", 29, "male") # invoking functions
    SomeFunc("sara", 22, "female")
    SomeFunc("james", 29, "male")
    SomeFunc("sara", 22, "female")
    
    SomeFunc(name="james", age=29, sex="male") # invoking functions
    SomeFunc(name="sara", age=22, sex="female") # with keyword argument
    SomeFunc(name="james", age=29, sex="male")
    SomeFunc(name="sara", age=22, sex="female")
    
if False:
    # define a function with two 'positional arguments' (no default values) and
    # one 'keyword argument' (has a default value)
    def calc(a, b, op='add'):
        if op == 'add':
            return a + b
        elif op == 'sub':
            return a - b
        else:
            print('valid operations are add and sub')
    
    # call the function
    calc(10, 4, op='add')   # returns 14
    calc(10, 4, 'add')      # also returns 14: unnamed arguments are inferred by position
    calc(10, 4)             # also returns 14: default for 'op' is 'add'
    calc(10, 4, 'sub')      # returns 6
    calc(10, 4, 'div')      # prints 'valid operations are add and sub'
    
if False:
    # use 'pass' as a placeholder if you haven't written the function body
    def stub():
        pass
    
    # return two values from a single function
    def min_max(nums):
        return min(nums), max(nums)
    
    # return values can be assigned to a single variable as a tuple
    nums = [1, 2, 3]
    min_max_num = min_max(nums) # min_max_num = (1, 3), tuple!
    
    # return values can be assigned into multiple variables using tuple unpacking
    minimum, maximum = min_max(nums) # minimum = 1, max_num = 3
    
if False:
    # variable-length arguments with *args
    def SomeFunc(*args):
        for i, arg in enumerate(args):
            print("arg[{}]= {}".format(i, arg))
        print()

    SomeFunc("sara", 22, "female", [0, 1, 2, 3])
    # arg[0]= sara
    # arg[1]= 22
    # arg[2]= female
    # arg[3]= [0, 1, 2, 3]
    
    def SomeFunc(name, age, sex, *hobbies):
        "SomeFunc() : prints information of a persion" # docstring
        print("name= %s, age= %d, sex= %s" % (name, age, sex))
        print("hobbies=", hobbies, type(hobbies))
        for i, hobby in enumerate(hobbies):
            print("hobby[{0}]= {1}".format(i, hobby), end=" ")
        print("\n")

    SomeFunc("james", 32, "male", "fishing", "cycling")
    # name= james, age= 32, sex= male
    # hobbies= ('fishing', 'cycling') <class 'tuple'>
    # hobby[0]= fishing hobby[1]= cycling

    SomeFunc("sara", 22, "female", "coding", "fishing", "reading", "cycling")
    # name= sara, age= 22, sex= female
    # hobbies= ('coding', 'fishing', 'reading', 'cycling') <class 'tuple'>
    # hobby[0]= coding hobby[1]= fishing hobby[2]= reading hobby[3]= cycling
    
    # keyword arguments, variable-length arguments with **kwargs
    def SomeFunc(**kwargs):
        print('kwargs=', kwargs, type(kwargs))
        for key, value in kwargs.items():
            print("{0} = {1}".format(key, value))
        print('\n')

    SomeFunc( name="sara", age=22, sex="female" )
    # kwargs= {'name': 'sara', 'age': 22, 'sex': 'female'} <class 'dict'>
    # name = sara
    # age = 22
    # sex = female

if False:
    # def some_func(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    #               ----------     ----------     ----------
    #                 |             |                  |
    #                 |        Positional or keyword   |
    #                 |                                - Keyword only
    #                  -- Positional only
    #
    # some_func(1, 2, 3, kwd1=4, kwd2=5)
    # some_func(1, 2, pos_or_kwd=3, kwd1=4, kwd2=5) # only these 2 styles are allowed!
    
    def some_func(name, **kwargs):
        print("name=", name)
        for key in kwargs:
            print("{}={}".format(key, kwargs[key]))

    some_func("james", fld1="aaa", fld2="bbb", fld3="ccc") # ok
    some_func(name="james", fld1="aaa", fld2="bbb", fld3="ccc") # ok
    #some_func("james", name="xxx", fld1="aaa", fld2="bbb", fld3="ccc") # error!
    #           -+---   ---------
    #            |         ???
    #            |
    #            this becomes 'name'

    def some_func(name, /, **kwargs):
        print("name=", name)
        for key in kwargs:
            print("{}={}".format(key, kwargs[key]))

    some_func("james", name="xxx", fld1="aaa", fld2="bbb", fld3="ccc") # ok!

if False:
    # unpacking function arguments from a list or dictionary
    print(list(range(3, 6))) # -> normal

    # - tuple/list unpacking with *expr
    # if the syntax *expression appears in the function call, expression must
    # evaluate to an iterable. elements from these iterables are treated as if
    # they were additional positional arguments.
    args = [3, 6] # a list!
    #list(range(args)) # error! -> unpacking required
    list(range(*args)) # ok

    def some_func(name, age, sex):
        print("name= %s, age= %d, sex= %s" % (name, age, sex))

    # - dict unpacking with **expr
    # if the syntax **expression appears in the function call, expression must
    # evaluate to a mapping, the contents of which are treated as additional
    # keyword arguments.
    kwargs = dict(name="james", age=23, sex="male")
    #some_func(kwargs) # error! -> unpacking required
    some_func(**kwargs) # ok -> (name="james", age=23, sex="male")



### -----------------------------------
### anonymous (lambda) functions ###
# ; primarily used to temporarily define a function for use by another function
# ; lambda_expr ::=  "lambda" [parameter_list] ":" expression
if True:
    # define a function the "usual" way
    def squared_0(x):
        return x**2

    print("squared_0=", squared_0)
    
    # define an identical function using lambda
    squared_1 = lambda x: x**2
    print("squared_1=", squared_1)
    
    # sort a list of strings by the last letter (without using lambda)
    simpsons = ['homer', 'marge', 'bart']
    def last_letter(word):
        return word[-1]
    print(sorted(simpsons, key=last_letter))
    
    # sort a list of strings by the last letter (using lambda)
    print(sorted(simpsons, key=lambda word: word[-1]))



### -----------------------------------
### for loops and while loops ###
# - for and while
# - break and continue
# - range(10) : 0, 1, ..., 9
# - range(1, 11) : 1, 2, ..., 10
# - In python, 'for' loops only implements the 'collection-based' iteration
#  ; iterables -> list, tuple, ...
# - for-loop usage
#   for item in iterable:
#       any_statements()
if False:
    # range returns a list of integers (Python 2) or a sequence (Python 3)
    range(0, 3)     # returns [0, 1, 2]: includes start value but excludes stop value
    range(3)        # equivalent: default start value is 0
    range(0, 5, 2)  # returns [0, 2, 4]: third argument is the step value
    
    # Python 2 only: use xrange to create a sequence rather than a list (saves memory)
    xrange(100, 100000, 5)
    
    # for loop (not the recommended style)
    fruits = ['apple', 'banana', 'cherry']
    for i in range(len(fruits)):
        print(fruits[i].upper())
    
    # for loop (recommended style)
    for fruit in fruits:
        print(fruit.upper())
    
    # iterate through two things at once (using tuple unpacking)
    family = {'dad':'homer', 'mom':'marge', 'size':6}
    for key, value in family.items():
        print(key, value)
    
    # use enumerate if you need to access the index value within the loop
    for i, fruit in enumerate(fruits):
        print(i, fruit)
    
    # for/else loop
    for fruit in fruits:
        if fruit == 'banana':
            print('Found the banana!')
            break    # exit the loop and skip the 'else' block
        else:
            # this block executes ONLY if the for loop completes without hitting 'break'
            print("Can't find the banana")
    
    # while loop
    count = 0
    while count < 5:
        print('This will print 5 times')
        count += 1    # equivalent to 'count = count + 1'
    
    # continue
    array = [90, 25, 67, 45, 80]
    for i in range(len(array)):
        if array[i] < 60:
            continue
        print("array[%d]= %d -> passed!" % (i, array[i]))
    
    # in-line for-loop (List comprehension)
    array = [90, 25, 67, 45, 80]
    print(array)
    array = [ item-20 for item in array ]
    print(array)


### -----------------------------------
### Comprehensions ###
if False:
    # for loop to create a list of cubes
    nums = [1, 2, 3, 4, 5]
    cubes = []
    for num in nums:
        cubes.append(num**3)
    
    # equivalent list comprehension
    cubes = [num**3 for num in nums]    # [1, 8, 27, 64, 125]
    
    # for loop to create a list of cubes of even numbers
    cubes_of_even = []
    for num in nums:
        if num % 2 == 0:
            cubes_of_even.append(num**3)
    
    # equivalent list comprehension
    # syntax: [expression for variable in iterable if condition]
    cubes_of_even = [num**3 for num in nums if num % 2 == 0]    # [8, 64]
    
    # for loop to cube even numbers and square odd numbers
    cubes_and_squares = []
    for num in nums:
        if num % 2 == 0:
            cubes_and_squares.append(num**3)
        else:
            cubes_and_squares.append(num**2)
    
    # equivalent list comprehension (using a ternary expression)
    # syntax: [true_condition if condition else false_condition for variable in iterable]
    cubes_and_squares = [num**3 if num % 2 == 0 else num**2 for num in nums]    # [1, 8, 9, 64, 25]
    
    # for loop to flatten a 2d-matrix
    matrix = [[1, 2], [3, 4]]
    items = []
    for row in matrix:
        for col in row:
            items.append(col)
    
    # equivalent list comprehension
    items = [item for row in matrix
                  for item in row]      # [1, 2, 3, 4]
    
    # set comprehension
    fruits = ['apple', 'banana', 'cherry']
    unique_lengths = {len(fruit) for fruit in fruits}   # {5, 6}
    
    # dictionary comprehension
    fruit_lengths = {fruit:len(fruit) for fruit in fruits}              # {'apple': 5, 'banana': 6, 'cherry': 6}
    fruit_indices = {fruit:index for index, fruit in enumerate(fruits)} # {'apple': 0, 'banana': 1, 'cherry': 2}



### -----------------------------------
### Map and Filter ###
if False:
    # 'map' applies a function to every element of a sequence
    # ...and returns a list (Python 2) or iterator (Python 3)
    simpsons = ['homer', 'marge', 'bart']
    map(len, simpsons)                      # returns [5, 5, 4]
    map(lambda word: word[-1], simpsons)    # returns ['r', 'e', 't']
    
    # equivalent list comprehensions
    [len(word) for word in simpsons]
    [word[-1] for word in simpsons]
    
    # 'filter' returns a list (Python 2) or iterator (Python 3) containing
    # ...the elements from a sequence for which a condition is True
    nums = range(5)
    filter(lambda x: x % 2 == 0, nums)      # returns [0, 2, 4]
    
    # equivalent list comprehension
    [num for num in nums if num % 2 == 0]
