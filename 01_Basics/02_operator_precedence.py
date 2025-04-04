"""
Python Operator Precedence - Examples and Explanations
"""

# Operator precedence determines the order in which operations are performed in an expression.
# Operators with higher precedence are executed before those with lower precedence.

# 1. Parentheses () - Highest precedence
result = (2 + 3) * 4  # Parentheses ensure addition happens first
print(result)  # Output: 20

# 2. Exponentiation **
result = 2 ** 3 ** 2  # Right-to-left associativity (3**2 is computed first, then 2**9)
print(result)  # Output: 512

# 3. Unary operators: +, -
result = -3 + 5
print(result)  # Output: 2

# 4. Multiplication, Division, Floor Division, Modulus (*, /, //, %)
result = 10 / 3  # Division
print(result)  # Output: 3.3333
result = 10 // 3  # Floor Division
print(result)  # Output: 3
result = 10 % 3  # Modulus (Remainder)
print(result)  # Output: 1

# 5. Addition and Subtraction (+, -)
result = 5 + 3 - 2
print(result)  # Output: 6

# 6. Bitwise Operators: &, |, ^, <<, >>
result = 5 & 3  # Bitwise AND
print(result)  # Output: 1
result = 5 | 3  # Bitwise OR
print(result)  # Output: 7

# 7. Comparison Operators: <, >, <=, >=, ==, !=
result = 10 > 5
print(result)  # Output: True
result = 10 == 10
print(result)  # Output: True

# 8. Logical Operators: not, and, or
result = not False  # NOT has highest precedence in logical operators
print(result)  # Output: True
result = True and False
print(result)  # Output: False
result = True or False
print(result)  # Output: True

# 9. Assignment Operators (=, +=, -=, *=, /=, etc.)
x = 10
x += 5  # Equivalent to x = x + 5
print(x)  # Output: 15

# 10. Identity and Membership Operators: is, is not, in, not in
x = [1, 2, 3]
y = x
print(x is y)  # Output: True (Same memory reference)
print(2 in x)  # Output: True (Checks membership)

# Operator precedence table (Highest to Lowest):
# 1. ()
# 2. **
# 3. +x, -x, ~x (Unary Operators)
# 4. *, /, //, %
# 5. +, -
# 6. <<, >> (Bitwise Shift)
# 7. &
# 8. ^
# 9. |
# 10. <, <=, >, >=, ==, !=
# 11. not
# 12. and
# 13. or
# 14. =, +=, -=, *=, /=, etc.
# 15. is, is not, in, not in


# Using parentheses is the best way to ensure clarity in complex expressions.

# Big Example demonstrating multiple operators and precedence
x = 5
y = 2
z = 3

result = (x + y) * z ** 2 / y - x % z + (x // y)
# Breakdown:
# 1. z ** 2 -> 3 ** 2 = 9 (Exponentiation)
# 2. (x + y) * 9 -> (5 + 2) * 9 = 7 * 9 = 63 (Parentheses & Multiplication)
# 3. 63 / y -> 63 / 2 = 31.5 (Division)
# 4. x % z -> 5 % 3 = 2 (Modulus)
# 5. x // y -> 5 // 2 = 2 (Floor Division)
# 6. 31.5 - 2 + 2 -> 31.5 + 0 = 31.5 (Subtraction & Addition)
print(result)  # Output: 31.5
