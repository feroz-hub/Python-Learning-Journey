"""
Python Data Types - Examples and Explanations
"""

# 1. Numeric Types

# Integer (int) - Whole numbers
integer_value = 10
print(integer_value)  # Output: 10
print(type(integer_value))  # Output: <class 'int'>

# Float (float) - Decimal numbers
float_value = 10.5
print(float_value)  # Output: 10.5
print(type(float_value))  # Output: <class 'float'>

# Complex (complex) - Numbers with real and imaginary parts
complex_value = 3 + 4j
print(complex_value)  # Output: (3+4j)
print(type(complex_value))  # Output: <class 'complex'>


# 2. Sequence Types

# String (str) - Sequence of characters
string_value = "Hello, Python!"
print(string_value)  # Output: Hello, Python!
print(type(string_value))  # Output: <class 'str'>

# List (list) - Ordered, mutable collection
list_value = [1, 2, 3, "Python"]
print(list_value)  # Output: [1, 2, 3, 'Python']
print(type(list_value))  # Output: <class 'list'>

# List Example - Mutable (Can be changed)
cart_items = ["apple", "banana"]
cart_items.append("orange")  # Adding item dynamically
print(cart_items)  # Output: ['apple', 'banana', 'orange']

# Tuple (tuple) - Ordered, immutable collection
tuple_value = (10, 20, 30)
print(tuple_value)  # Output: (10, 20, 30)
print(type(tuple_value))  # Output: <class 'tuple'>

# Tuple Example - Immutable (Cannot be changed)
country_codes = ("US", "IN", "UK")
print(country_codes)  # Output: ('US', 'IN', 'UK')

# Explanation:
# - List is Mutable: Can add/remove elements dynamically.
# - Tuple is Immutable: Fixed structure, optimized for performance and safety.
# - Tuple can be used as dictionary keys; Lists cannot.

# Range (range) - Sequence of numbers
range_value = range(5)  # Generates numbers from 0 to 4
print(list(range_value))  # Output: [0, 1, 2, 3, 4]
print(type(range_value))  # Output: <class 'range'>


# 3. Set Types

# Set (set) - Unordered collection of unique items
s = {1, 2, 3, 3, 4}  # Duplicate 3 will be removed
print(s)  # Output: {1, 2, 3, 4}
print(type(s))  # Output: <class 'set'>

# Set Example - Mutable (Can be changed)
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")  # Adding a new element
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}
fruits.remove("banana")  # Removing an element
print(fruits)  # Output: {'apple', 'cherry', 'orange'}

# Frozenset (frozenset) - Immutable set
frozenset_value = frozenset([1, 2, 3, 4])
print(frozenset_value)  # Output: frozenset({1, 2, 3, 4})
print(type(frozenset_value))  # Output: <class 'frozenset'>

# Frozenset Example - Immutable (Cannot be changed)
im_frozen = frozenset({"car", "bike", "bus"})
print(im_frozen)  # Output: frozenset({'car', 'bike', 'bus'})
# im_frozen.add("train")  # This would raise an AttributeError because frozensets are immutable.

# Explanation:
# - Set is Mutable: Elements can be added or removed dynamically.
# - Frozenset is Immutable: Once created, elements cannot be modified.
# - Frozensets can be used as dictionary keys, whereas normal sets cannot.


# 4. Mapping Type

# Dictionary (dict) - Key-value pairs
dict_value = {"name": "Alice", "age": 25}
print(dict_value)  # Output: {'name': 'Alice', 'age': 25}
print(type(dict_value))  # Output: <class 'dict'>


# 5. Boolean Type

# Boolean (bool) - True or False values
bool_value = True
print(bool_value)  # Output: True
print(type(bool_value))  # Output: <class 'bool'>


# 6. Binary Types

# Bytes (bytes) - Immutable sequence of bytes
bytes_value = b"Hello"
print(bytes_value)  # Output: b'Hello'
print(type(bytes_value))  # Output: <class 'bytes'>

# Bytearray (bytearray) - Mutable sequence of bytes
bytearray_value = bytearray([65, 66, 67])  # Represents 'ABC'
print(bytearray_value)  # Output: bytearray(b'ABC')
print(type(bytearray_value))  # Output: <class 'bytearray'>

# Memoryview (memoryview) - View of binary data
memoryview_value = memoryview(bytes([1, 2, 3]))
print(memoryview_value)  # Output: <memory at 0x...>
print(type(memoryview_value))  # Output: <class 'memoryview'>


# 7. None Type

# NoneType - Represents absence of value
none_value = None
print(none_value)  # Output: None
print(type(none_value))  # Output: <class 'NoneType'>
