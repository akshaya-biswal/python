# -------------- Output --------------
print("Python is powerful")

# End whitespace
print("Good Morning!", end=" ")
print("It is rainy today")
# Good Morning! It is rainy today

# Sep parameter
print("New Year", 2023, "See you soon!", sep=". ")
# New Year. 2023. See you soon!

# Concatenated Strings
print("World is " + "awesome.")
# World is awesome.

# Formatting
x = 5
y = 10
print("The value of x is {} and y is {}".format(x, y))

# -------------- Input --------------

num = input("Enter a number: ")
print("You Entered:", num)
print("Data type of num:", type(num))

# To convert user input into a number
num2 = int(input("Enter a number: "))
print("You Entered:", num2)
print("Data type of num:", type(num2))
