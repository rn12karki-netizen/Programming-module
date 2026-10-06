# PYTHON OPERATORS

# Arithmetic Operators

# Arithmetic operators are used to perform mathematical calculations.

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


# Addition Operator (+)

a = 15
b = 5

result = a + b
print(result)

# The + operator adds two values.
# 15 + 5 = 20


# Subtraction Operator (-)

a = 15
b = 5

result = a - b
print(result)

# The - operator subtracts the second value from the first.
# 15 - 5 = 10


# Multiplication Operator (*)

a = 6
b = 4

result = a * b
print(result)

# The * operator multiplies two values.
# 6 × 4 = 24


# Division Operator (/)

a = 10
b = 2

result = a / b
print(result)

# The / operator divides one value by another.
# Division returns a float.
# 10 / 2 = 5.0


# Floor Division Operator (//)

a = 17
b = 5

result = a // b
print(result)

# // returns the floor value after division.
# 17 / 5 = 3.4
# 17 // 5 = 3


# Modulus Operator (%)

a = 17
b = 5

result = a % b
print(result)

# % returns the remainder.
# 17 divided by 5 gives a remainder of 2.
# Therefore, 17 % 5 = 2


# Exponent Operator (**)

a = 2
b = 4

result = a ** b
print(result)

# ** raises the first number to the power of the second.
# 2 ** 4 = 2 × 2 × 2 × 2
# 2 ** 4 = 16


# Comparison Operators

# Comparison operators compare two values.
# The result is always True or False.


# Equal To (==)

a = 10
b = 10

print(a == b)

# == checks whether both values are equal.


# Not Equal To (!=)

a = 10
b = 5

print(a != b)

# != checks whether the two values are different.


# Greater Than (>)

a = 10
b = 5

print(a > b)

# > checks whether the first value is greater than the second.


# Less Than (<)

a = 5
b = 10

print(a < b)

# < checks whether the first value is less than the second.


# Greater Than or Equal To (>=)

age = 18

print(age >= 18)

# >= checks whether the value is greater than or equal to another value.


# Less Than or Equal To (<=)

age = 16

print(age <= 18)

# <= checks whether the value is less than or equal to another value.


# Assignment Operators

# Assignment operators are used to store or update values in variables.


# Assignment (=)

x = 10

print(x)

# The value 10 is assigned to x.


# Addition Assignment (+=)

x = 10

x += 5

print(x)

# x += 5 means:
# x = x + 5

# The original value of x was 10.
# 10 + 5 = 15


# Subtraction Assignment (-=)

x = 10

x -= 3

print(x)

# x -= 3 means:
# x = x - 3


# Multiplication Assignment (*=)

x = 10

x *= 3

print(x)

# x *= 3 means:
# x = x * 3


# Division Assignment (/=)

x = 10

x /= 2

print(x)

# x /= 2 means:
# x = x / 2


# Floor Division Assignment (//=)

x = 17

x //= 5

print(x)

# x //= 5 means:
# x = x // 5


# Modulus Assignment (%=)

x = 17

x %= 5

print(x)

# x %= 5 means:
# x = x % 5


# Exponent Assignment (**=)

x = 2

x **= 4

print(x)

# x **= 4 means:
# x = x ** 4


# Logical Operators

# Logical operators are used to combine or reverse conditions.

# and
# or
# not


# AND Operator

age = 20

print(age >= 18 and age <= 30)

# Both conditions must be True.
#
# age >= 18 → True
# age <= 30 → True
#
# True and True → True


# Another AND Example

age = 35

print(age >= 18 and age <= 30)

# age >= 18 → True
# age <= 30 → False
#
# True and False → False


# OR Operator

age = 15

print(age < 18 or age > 60)

# Only one condition needs to be True.
#
# age < 18 → True
# age > 60 → False
#
# True or False → True


# NOT Operator

is_student = True

print(not is_student)

# not reverses the Boolean value.
#
# True becomes False.
# False becomes True.


# Bitwise Operators

# Bitwise operators work with numbers at the binary level.

# &
# |
# ^
# ~
# <<
# >>


# Bitwise AND (&)

a = 5
b = 3

result = a & b
print(result)

# 5 = 0101
# 3 = 0011
#
# 0101
# 0011
# ----
# 0001
#
# & gives 1 only when both bits are 1.


# Bitwise OR (|)

a = 5
b = 3

result = a | b
print(result)

# 5 = 0101
# 3 = 0011
#
# 0101
# 0011
# ----
# 0111
#
# | gives 1 when at least one bit is 1.


# Bitwise XOR (^)

a = 5
b = 3

result = a ^ b
print(result)

# 5 = 0101
# 3 = 0011
#
# 0101
# 0011
# ----
# 0110
#
# XOR gives 1 when the bits are different.


# Bitwise NOT (~)

a = 5

result = ~a
print(result)

# ~ flips the bits of a number.
#
# Formula:
# ~n = -(n + 1)
#
# ~5 = -(5 + 1)
# ~5 = -6


# Left Shift (<<)

a = 5

result = a << 1
print(result)

# 5 in binary:
# 0101
#
# 0101 << 1
# 1010
#
# 1010 = 10
#
# Left shifting by 1 is equivalent to multiplying by 2.
#
# 5 << 1 = 10
# 5 << 2 = 20
# 5 << 3 = 40


# Right Shift (>>)

a = 20

result = a >> 1
print(result)

# 20 in binary:
# 10100
#
# 10100 >> 1
# 01010
#
# 01010 = 10
#
# Right shifting by 1 is equivalent to dividing by 2
# for positive integers.
#
# 20 >> 1 = 10
# 20 >> 2 = 5
# 20 >> 3 = 2


# Identity Operators

# Identity operators check whether two variables
# refer to the same object.

# is
# is not


# is Operator

a = [1, 2, 3]
b = a

print(a is b)

# b = a means b refers to the exact same list as a.
#
# a
# ↓
# [1, 2, 3]
# ↑
# b


# is not Operator

a = [1, 2, 3]
b = [1, 2, 3]

print(a is not b)

# The values are the same,
# but they are different objects.


# == vs is

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

# == checks whether the values are equal.
# is checks whether they are the same object.


# ID() Function

# id() returns the identity of an object.

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(id(a))
print(id(b))
print(id(c))

# id(a) and id(c) are the same.
# id(a) and id(b) are different.


# Membership Operators

# Membership operators check whether a value
# exists inside another object such as a list or string.

# in
# not in


# in Operator

numbers = [10, 20, 30, 40]

print(20 in numbers)

# 20 exists inside the list.


# Another Example

numbers = [10, 20, 30, 40]

print(50 in numbers)

# 50 does not exist inside the list.


# not in Operator

numbers = [10, 20, 30, 40]

print(50 not in numbers)

# 50 is not present in the list.


# Membership with Strings

name = "Python"

print("P" in name)

print("z" in name)

# "P" exists inside the string.
# "z" does not exist inside the string.


# Operator Precedence

# Operator precedence determines which operation
# Python performs first.

result = 10 + 5 * 2

print(result)

# Multiplication happens before addition.
#
# 5 * 2 = 10
# 10 + 10 = 20


# Parentheses can change the order.

result = (10 + 5) * 2

print(result)

# Parentheses are calculated first.
#
# 10 + 5 = 15
# 15 * 2 = 30


# Common Operator Precedence

# 1.  ()
# 2.  **
# 3.  +x, -x, ~x
# 4.  *, /, //, %
# 5.  +, -
# 6.  <<, >>
# 7.  &
# 8.  ^
# 9.  |
# 10. ==, !=, >, <, >=, <=
# 11. not
# 12. and
# 13. or
