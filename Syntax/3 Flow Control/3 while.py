# Example 1
number = 1

while number <= 4:
    print(number)
    number = number + 1

# Example 2
number = int(input("Enter a number: "))
total = 0

while number != 0:
    total = total + number
    number = int(input("Enter a number: "))
print("The sum is", total)
