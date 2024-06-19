# String
# Immutable

# create string type variables

name = "Python"
message = "I love Python."

print(name[0])
print(name[0:6])

# Multiline
# multiline string
greet = """
Never gonna give you up
Never gonna let you down
"""

print(greet)

# Compare
str1 = "Hello, world!"
str2 = "I love Swift."
str3 = "Hello, world!"

# compare str1 and str2
print(str1 == str2)

# compare str1 and str3
print(str1 == str3)

# Iterate
greet = "Hello"
for letter in greet:
    print(letter)

# Length
print(len(greet))

# Membership
print("a" in "program")  # True
print("at" not in "battle")  # False

# upper()
message = "python is fun"
print(message.upper())  # PYTHON IS FUN

# swapcase()
sentence1 = "THIS SHOULD ALL BE LOWERCASE."

print(sentence1.swapcase())
sentence2 = "this should all be uppercase."  # uppercase to lowercase

print(sentence2.swapcase())
sentence3 = "ThIs ShOuLd Be MiXeD cAsEd."  # lowercase to uppercase

# capitalize()
sentence = "i love PYTHON"
capitalized_string = sentence.capitalize()
print(capitalized_string)  # I love python

# center()
sentence = "Python is awesome"
new_string1 = sentence.center(24, "*")
new_string2 = sentence.center(24)

print(new_string1)  # ***Python is awesome****
print(new_string2)  #    Python is awesome
