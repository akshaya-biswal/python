# int - holds signed integers of non-limited length
# float - holds floating decimal points and it's accurate up to 15 decimal places
# complex - holds complex numbers

num1 = 5
num2 = 5.42
num3 = 8 + 2j

print(num1, "is of type", type(num1))
print(num2, "is of type", type(num2))
print(num3, "is of type", type(num3))

# Binary - 0b or 0B
# Octal	- 0o or 0O
# Hexadecimal -	0x or 0X

print(0b1101011)  # 107
print(0xFB + 0b10)  # 253
print(0o15)  # 13

# Explicit Type Conversion
num1 = int(2.3)
print(num1)  # 2

num2 = int(-2.8)
print(num2)  # -2

num3 = float(5)
print(num3)  # 5.0

num4 = complex("3+5j")
print(num4)  # (3 + 5j)

# Random Module

import random

print(random.randrange(10, 20))
print(random.random())  # random value between 0 and 1

list1 = ["a", "b", "c", "d", "e"]
print(random.choice(list1))  # get random item from list1

random.shuffle(list1)  # Shuffle list1
print(list1)

# Mathematics

import math

print(math.pi)
print(math.cos(math.pi))
print(math.exp(10))
print(math.log10(1000))
print(math.sinh(1))
print(math.factorial(6))
