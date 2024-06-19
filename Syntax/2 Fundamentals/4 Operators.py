# -------------- Arithmetic --------------
a = 7
b = 2

# addition, subtraction, multiplication, division
print("Sum: ", a + b)
print("Subtraction: ", a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b)

# floor division
print("Floor Division: ", a // b)

# modulo
print("Modulo: ", a % b)

# a to the power b
print("Power: ", a**b)

# -------------- Assignment --------------
# assign 10 to a
a = 10

# assign 5 to b
b = 5

a += b
print(a)  # 15

# -------------- Comparison --------------
print(a > b)
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# -------------- Logical --------------
# AND
print(True and True)
print(True and False)

# OR
print(True or False)

# NOT
print(not True)

# -------------- Bitwise --------------

# -------------- Special --------------
# They are used to check if two values are located at the same memory location

x1 = 5
y1 = 5
print(x1 is y1)  # True
print(x1 is not y1)  # False

x2 = "Hello"
y2 = "Hello"
print(x2 is y2)  # True

x3 = [1, 2, 3]
y3 = [1, 2, 3]
print(x3 is y3)  # False

# -------------- Membership --------------
# They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary)
message = "Hello world"
dict1 = {1: "a", 2: "b"}

print("H" in message)  # True

print("hello" not in message)  # True

print(1 in dict1)  # True

print("a" in dict1)  # False
