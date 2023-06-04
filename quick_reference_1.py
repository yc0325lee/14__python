# vim: ft=python ts=4 sw=4 tw=999 expandtab
# ----------------------------------------------------------------------------
# File : quick_reference_1.py
# Description : 
# Author : yc0325lee
# Created : 2019-03-19 23:45:03 by yc0325lee
# Modified : 2019-03-26 23:39:12 by yc0325lee
# ----------------------------------------------------------------------------

# reference
- built-in functions
  ; https://docs.python.org/3/library/functions.html
- python standard library
  ; https://docs.python.org/3/library/index.html

# library
from random import *; # rand, randrange, ...
import sys
import pickle


# -------------------------------------
# built-in datatype
# - Text     Type:  str
# - Numeric  Types: int, float, complex
# - Sequence Types: list, tuple, range
# - Mapping  Type:  dict
# - Set      Types: set, frozenset
# - Boolean  Type:  bool
# - Binary   Types: bytes, bytearray, memoryview

# numeric types - int float


# '__name__' is a built-in variable which evaluates to the name of the current module

# -------------------------------------
# variable(변수)
# ; python에서의 변수들은 무조건 handle(data를 저장하고 있는 memory를 가리키는)임 

# declaration assignment
int a = x > 20 ? 100 : 0; # C style
a = 100 if x > 20 else 0 # Python style


a = [ 0, 1, 2 ]
print( type(a) ); # <class 'list'>
print( id(a) ); # 1220558016384 -> address
print( a is a ); # True

b = a;
print( type(b) ); # <class 'list'>
print( id(b) ); # 1220558016384 -> address
print( b is a ); # True

c = a[:]
print( type(c) ); # <class 'list'>
print( id(c) ); # 1220558016384 -> address
print( c is a ); # False

from copy import copy
d = copy(a)
print( type(d) ); # <class 'list'>
print( id(d) ); # 2143836101568
print( d is a ); # False

# same! tuple-style
  a, b   =   'AAA', 'BBB'
  a, b   = ( 'AAA', 'BBB' ); # tuple을 사용한 value assignment!
( a, b ) = ( 'AAA', 'BBB' )
  name, age, sex, hobby   =   "yclee", 46, "male", "coding"
( name, age, sex, hobby ) = ( "yclee", 46, "male", "coding" ) # same!


# -------------------------------------
# operators

# arithmetic operators
# +----+-----------------------------------------------------------+--------+
# |    | description                                               | x + y  |
# +----+-----------------------------------------------------------+--------+
# | +  | Addition: adds two operands                               | x + y  |
# | -  | Subtraction: subtracts two operands                       | x - y  |
# | *  | Multiplication: multiplies two operands                   | x * y  |
# | /  | Division (float): divides the first operand by the second | x / y  | 7 / 2 = 3.5
# | // | Division (floor): divides the first operand by the second | x // y | 7 // 2 = 3
# | %  | Modulus: returns the remainder when first operand is      | x % y  |
# |    |          divided by the second                            |        |
# | ** | Power : Returns first raised to power second              | x ** y | 3 ** 4 = 81
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

# special operators

# - identity operators
# +--------+----------------------------------------+
# | is     | True if the operands are identical     |
# +--------+----------------------------------------+
# | is not | True if the operands are not identical |
# +--------+----------------------------------------+
- equality operator (==) compares the values of both the operands and checks for value equality.
- the 'is' operator checks whether both the operands refer to the same object or not.

# - membership operators
# +--------+--------------------------------------------+
# | in     | True if value is found in the sequence     |
# +--------+--------------------------------------------+
# | not in | True if value is not found in the sequence |
# +--------+--------------------------------------------+



# -------------------------------------
# numbers
a = 123 # integers
a = -345
a = 0

a = 123.45 # float/double
a = -1234.5
a = 3.4e10

a = 0o34 # octal
a = 0o25

a = 0x2A # hexa-decimal
a = 0xFF

7 % 3 --> 1
7 / 4 --> 1.75
7 // 4 --> 1


# -------------------------------------
# string - class 'str', immutable
# - all quoted strings
# - 문자열은 "immutable" 자료형임 -> 변경할 수 없음!
string = "Hello, world!" # or
string = 'Hello, world!'
string = """Hello, world!"""
string = '''Hello, world!'''
string = "Python's favorite food is perl" # including single-quote mark - (1)
string = 'Python\'s favorite food is perl' # including single-quote mark - (2)

# 3 ways of making multi-line string
multiline = "Life is too short\nYou need python" # (1)
multiline="""
Life is too short
You need python
""" # (2)
multiline='''
Life is too short
You need python
''' # (3)

# writing header - string concatenation & multiplication
title = "string concatenation & multiplication"
print("# " + "-" * 76)
print("# " + "Title : %s" % title)
print("# " + "-" * 76)

# string handling
head = "python"
tail = " is fun!"
joined = head + tail # concatenation
print joined
print("length= " + len(joined)) # length of string

# indexing
var = "Life is too short"
#      0         1
#      01234567890123456
var[0] --> 'L'
var[3] --> 'e'
var[-1] --> 't'
var[-2] --> 'r'
var[-0] --> 'L'

# slicing
piece = var[0] + var[1] + var[2] + var[3] # --> 'Life'
piece = var[0:4] # --> 'Life', 0 <= idx < 4
a = "abcde"
sub = a[0:3]; # "abc", 0 <= x < 3
sub = a[3:5]; # "de"
sub = a[2:]; # "cde"
sub = a[:3]; # "abc"

# length
length = len(price); # 4

date = "2021/06/19"
year = date[:4] # [0:4]
month = date[5:7]
day = date[8:] # [8:10]

# format
year= 2021; month="May"; day=4;
print("year= %d, month= %d, day= %s" % (year, month, day))
print("year= %s, month= %s, day= %s" % (year, month, day)); # %s는 flexible함. context를 보고 형변환으로 맞춤

# string functions
str.count('c') # count
str.find('b'); # returns -1 if not exists
str.index('t'); # error if not exists
",".join("abcde"); # -> a,b,c,d,e
",".join( ['a', 'b', 'c', 'd', 'e'] ); # -> a,b,c,d,e
str.upper(); # upper-case
str.lower(); # lower-case
if str[0].isupper(): # upper-case
if str[0].islower(): # upper-case
str.lstrip(); # remove white-spaces in the left
str.rstrip(); # remove white-spaces in the right
str.strip(); # remove white-spaces in the left & right
str.replace("https://", ""); # "aaa" -> "bbb"
str.split() or str.split(',') # split()

scores = { "math":60, "english":70, "writing":80, "sports":90 }
for subject, score in scores.items()
    print( subject.ljust(10), str(score).rjust(4), sep=":")


# -------------------------------------
# boolean
x = True
y = False


# -------------------------------------
# list - mutable
# - function
#  ; len()
#  ; sort()
#  ; sum()
#  ; index()
x = list()
y = [ 0, 1, 2, 3, 4 ]
strings = [ "aaa", "bbb", "ccc", "ddd", "eee" ]
val1 = y[1]
val2 = strings[4]
y[4] = 5
numElements = len(y)
a = sorted(y)
print(a)

for s in strings:
    print("str= %s" % s)

location = y.index(3)
location = strings.index("ddd")

if "bbb" in strings
    print("bbb exists!")

fruits = ["apple", "apple", "banana", "apple", "pineapple", "grape", "watermalon", "grape", "tomato"]
table = dict()
for this in fruits:
    if this in table:
        table[this] = table[this] + 1 # increment
    else:
        table[this] = 0 # initial

print(table)

# list functions
a = [0, 1, 2, 3, 4]; del(a[1]); # [0, 2, 3, 4]
a = [0, 1, 2, 3, 4]; del(a[2:]); # [0, 1]
a = [0, 1, 2, 3, 4]; a.append(5); # [0, 1, 2, 3, 4, 5]
a = [0, 1, 2, 3, 4]; a.append([5, 6]); # [0, 1, 2, 3, 4, 5, 6]
a = [4, 3, 2, 1, 0]; a.sort(); # [0, 1, 2, 3, 4]
a = [4, 3, 2, 1, 0]; a.reverse(); # [0, 1, 2, 3, 4]
a = [4, 3, 2, 1, 0]; a.index(1); # 3
a = [4, 3, 2, 1, 0]; a.index(5); # error
a = [4, 3, 2, 1, 0]; a.insert(1, 5); # [4, 5, 3, 2, 1, 0]
a = [4, 3, 2, 1, 0, 3]; a.remove(3); # [4, 2, 1, 0, 3]
                        a.remove(3); # [4, 2, 1, 0]
a = [0, 1, 2, 3, 4]; print( a.pop() ); # prints '4' & remaining= [0, 1, 2, 3]
a = [0, 1, 2, 3, 4]; print( a.pop(2) ); # prints '2' & remaining= [0, 1, 3, 4]
a = [4, 3, 2, 1, 0, 3]; a.count(3); # 2

a = [0, 1, 2, 3, 4]; print("a=", a)



# -------------------------------------
# tuple - immutable
# - assigment to tuple not possible(immutable)
# - faster that list
x = tuple() # emtpy, but useless
y = ()
y = ( 0, 1, 2, 3, 4 )
strings = ("aaa", "bbb", "ccc", "ddd", "eee")


# -------------------------------------
# dictionary - mutable
# - associative array or hash
# - functions
#  ; keys(), values(), items()
x = dict()
y = {}
table = {
    "james" : 32,
    "danniel" : 24,
    "jane" : 17,
    "thomas" : 22,
    "sara" : 43,
}
print(table)

table["bruce"] = 44 # mutable

print("thomas" in table)
print("chales" in table)
if "danniel" in table:
    print("danniel's table is %d" % table["danniel"])

print( table.keys() )
print( table.values() )

for key in table:
    print("key= %s, value= %d" % (key, table[key]))


# -------------------------------------
# set
# - Set is an unordered collection of data type that is iterable, mutable
# - has no duplicate elements
group = set(["aaa", "bbb", "ccc", "ddd"])
print(group)
group.add("eee")
print(group)
group.update(["fff", "ggg"])
print(group)

for item in group:
    print("item=", item)

if "eee" in group :
    print("eee exists!")

print( "eee" in group )

group.remove("aaa")
print(group)
#group.remove("aaa") # error
group.discard("aaa")
print(group)

# update() method accepts lists, strings, tuples and sets
group.update( ["hhh", "iii"])
print(group)

print( group.pop() )
print( group.pop() )
print( group.pop() )
print( group.pop() )
group.clear()
print("group=", group)

set1 = set( ["aaa", "bbb", "ccc"] )
set2 = set( ["bbb", "ccc", "ddd"] )
print("union=", set1 | set2)
print("union=", set1.union(set2))
print("intersection=", set1 & set2)
print("intersection=", set1.intersection(set2))
print("difference=", set1 - set2)
print("difference=", set1.difference(set2))

set1 = list(set1) # casting
set2 = list(set2) # casting
print(set1, type(set1))
print(set2, type(set2))



# -------------------------------------
# string formatting

# (1) formatting with '%'
year= 2021; month="May"; day=4;
print("year= %d" % year) # single argument
print("year= %d, month= %d, day= %s" % (year, month, day)) # multiple arguments with tuple
print("year= %s, month= %s, day= %s" % (year, month, day)); # %s는 flexible함. context를 보고 형변환으로 맞춤
print("Error rate is %d%%." % 99) # %% -> '%' character

# (2) formatting with format()
year= 2021; month="May"; day=4;
print("year= {0}, month= {1}, day= {2}".format(year, month, day))
print("year= {year}, month= {month}, day= {day}"
    .format(year=2021, month="May", day=4) # 'name=value' pair
)
print("pi= {0:0.10f}".format(3.141592))

# combining positional and keyword arguments
print("Number one portal is {0}, {1}, and {other}.".format('Geeks', 'For', other='Geeks'))
 
# using format() method with number format specifiers
print("Geeks :{0:2d}, Portal :{1:8.2f}".format(12, 0.546))
 
# Changing positional argument
print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42, 11))
 
print("Geeks: {a:5d},  Portal: {p:8.2f}" .format(a = 453, p = 59.058))

# adjusting to left/right/center & filling
# :<10 - left
# :>10
# :^10
print("year= {0:0>6}, month= {1:->6}, day= {2: >4}".format(year, month, day))

# (3) formatting with 'f' -> python v3.6 or later
name = "Daniel"; age = 45
print( f"My name is {name} and I'm {age} years old." )
print( f"I'll be {age+1} years old next year." )

me = {"name":"Daniel", "age":45}; # using dictionary
print( f"My name is {me["name"]} and I'm {me["age"]} years old." )
print( f"I'll be {me["age"]+1} years old next year." )

pi = 3.1415926
print( f"pi= {pi:10.4f}" ) # floating-point format

# -------------------------------------
# condition
x = 5
if x > 3 and x < 5 :
    print("true")

x = 5
y = 2
min = x if x < y else y # ternary operator


# -------------------------------------
# loop/iteration - for, while
# - for and while
# - break and continue
# - range(10) : 0, 1, ..., 9
# - range(1, 11) : 1, 2, ..., 10
# - In python, for loops only implements the 'collection-based' iteration
#  ; iterables -> list, tuple, ...
for item in iterable:
    any_statements()

for i in range(10): # 1st way
    print("i= " + i)

i = 0
while  i < 10: # 2nd way
    print("i= %d" % i)
    i = i + 1

# endless loop
val = 0
while True:
    do_something()
    if val > 100:
        break

array = [90, 25, 67, 45, 80]
for i in range(len(array)):
    if array[i] >= 60:
        print("array[%d]= %d -> passed!" % (i, array[i]))
    else:
        print("array[%d]= %d -> failed!" % (i, array[i]))

array = [90, 25, 67, 45, 80]
for i in range(len(array)):
    if array[i] < 60:
        continue
    print("array[%d]= %d -> passed!" % (i, array[i]))

# in-line for-loop (List comprehension)
array = [90, 25, 67, 45, 80]
print(array)
array = [ item - 20 for item in array ]
print(array)


# -------------------------------------
# class and object


# -------------------------------------
# package and module
# - package
#  ; library
# - module
#  ; file



# -------------------------------------
# file i/o

# write
import sys
outFile = open("temp.txt", "w", encoding="utf8")
print("[info] writing to temp.txt ...", file=sys.stderr)
print("0: This is for test!!!", file=outFile)
print("1:", file=outFile)
print("2:", file=outFile)
print("3:", file=outFile)
print("4:", file=outFile)
print("5:", file=outFile)
print("[info] closing temp.txt ...", file=sys.stderr)
outFile.close()

# read
inFile = open("temp.txt", "r", encoding="utf8")
print( inFile.readline(), end="" )
print( inFile.readline(), end="" )
print( inFile.readline(), end="" )
print( inFile.readline(), end="" )
print( inFile.readline(), end="" )
inFile.close()

# read
inFile = open("temp.txt", "r", encoding="utf8")
while True:
    line = inFile.readline()
    if line:
        print(line, end="")
    else:
        break
inFile.close()

# read
inFile = open("temp.txt", "r", encoding="utf8")
lines = inFile.readlines()
for line in lines:
    print(line, end="")
inFile.close()

# read using 'with' statement -> simpler and manageable
with open("temp.txt", "r", encoding="utf8") as inFile:
    lines = inFile.readlines()
    for line in lines:
        print(line, end="")

# inFile.read([n])
#  ; Returns the read bytes in form of a string.
#  ; Reads n bytes, if no n specified, reads the entire file.
# inFile.readline([n])
#  ; Reads a line of the file and returns in form of a string.
#  ; For specified n, reads at most n bytes.
#  ; However, does not reads more than one line,
#  ; even if n exceeds the length of the line.
# inFile.readlines()
#  ; Reads all the lines and return them as each line a string element in a list


# -------------------------------------
# exception handling
# - use 'try: ~ except: ~ else: ~' block!
# - Exception class hierarchy in python
#   ; https://docs.python.org/2/library/exceptions.html#exception-hierarchy
#
#     BaseException
#      +-- SystemExit
#      +-- KeyboardInterrupt
#      +-- GeneratorExit
#      +-- Exception
#           +-- StopIteration
#           +-- StandardError
#           |    +-- BufferError
#           |    +-- ArithmeticError
#           |    |    +-- FloatingPointError
#           |    |    +-- OverflowError
#           |    |    +-- ZeroDivisionError
#           |    +-- AssertionError
#           |    +-- AttributeError
#           |    +-- EnvironmentError
#           |    |    +-- IOError
#           |    |    +-- OSError
#           |    |         +-- WindowsError (Windows)
#           |    |         +-- VMSError (VMS)
#           |    +-- EOFError
#           |    +-- ImportError
#           |    +-- LookupError
#           |    |    +-- IndexError
#           |    |    +-- KeyError
#           |    +-- MemoryError
#           |    +-- NameError
#           |    |    +-- UnboundLocalError
#           |    +-- ReferenceError
#           |    +-- RuntimeError
#           |    |    +-- NotImplementedError
#           |    +-- SyntaxError
#           |    |    +-- IndentationError
#           |    |         +-- TabError
#           |    +-- SystemError
#           |    +-- TypeError
#           |    +-- ValueError
#           |         +-- UnicodeError
#           |              +-- UnicodeDecodeError
#           |              +-- UnicodeEncodeError
#           |              +-- UnicodeTranslateError
#           +-- Warning
#                +-- DeprecationWarning
#                +-- PendingDeprecationWarning
#                +-- RuntimeWarning
#                +-- SyntaxWarning
#                +-- UserWarning
#                +-- FutureWarning
#                +-- ImportWarning
#                +-- UnicodeWarning
#                +-- BytesWarning

# IndexError
items = [ 0, 1, 2 ]
try:
    print("item[%d] = %d" % (0, items[0]))
    print("item[%d] = %d" % (1, items[1]))
    print("item[%d] = %d" % (2, items[2]))
    print("item[%d] = %d" % (3, items[3]))
except Exception as err:
    print("[err ] something's wrong!")
    print("       message= ", err)
else:
    print("[info] it's ok!")


# ZeroDivisionError
dividend = 8;
divisor = 0;

try:
    result = dividend / divisor;
except Exception as err:
    print("[err ] something's wrong!")
    print("       message= ", err)
else:
    print("[info] result= ", result)


# raising error - user-defined exception
class SpecialError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    num1 = 64
    num2 = 9

    if num1 >= 10 or num2 >= 10:
        raise SpecialError("input num1= {0}, num2= {1}".format(num1,num2))

    print("{0} / {1] = {2}".format(num1, num2, int(num1/num2)))

except SpecialError as err:
    print("[err ] wrong value on input!")
    print("       message=", err)
finally:
    print("[info] end of execution...")

