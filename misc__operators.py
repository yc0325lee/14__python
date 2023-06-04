# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : misc__operators.py
# - author : yc0325lee
# - created : 2022-10-16 12:32:37 by lee2103
# - modified : 2022-10-16 12:32:37 by lee2103
# - description : 
# ; 
# ----------------------------------------------------------------------------

# arithmetic operators
# ; see 'operator' library also.
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
# equality operator (==) compares the values of both the operands and checks for value equality.
# the 'is' operator checks whether both the operands refer to the same object or not.

# - membership(containment) operators
# +--------+--------------------------------------------+
# | in     | True if value is found in the sequence     |
# +--------+--------------------------------------------+
# | not in | True if value is not found in the sequence |
# +--------+--------------------------------------------+
