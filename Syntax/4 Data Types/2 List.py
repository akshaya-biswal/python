# -------------- Characteristics --------------
# Ordered (Like an array)
# Mutable (can be changed)
# Allow duplicates

# -------------- List Methods --------------
# Creation
fruits = ["apple", "banana", "orange"]

# index() - returns the index
index = fruits.index("orange")
print("index: ", index)


# append() - adds an item to the end
fruits.append("cherry")
print("fruits: ", fruits)

# extend() - adds all the items
numbers1 = [3, 4, 5]
numbers2 = [10, 20]
numbers2.extend(numbers1)
print("extend :", numbers2)

# insert() - inserts an element to the list at the specified index
vowel = ["a", "e", "i", "u"]
vowel.insert(3, "o")
print("vowel:", vowel)  # ['a', 'e', 'i', 'o', 'u']

prime_numbers = [2, 3, 5, 7]
prime_numbers.insert(4, 11)
print("prime_numbers:", prime_numbers)  # [2, 3, 5, 7, 11]

mixed_list = [{1, 2}, [5, 6, 7]]
number_tuple = (3, 4)
mixed_list.insert(1, number_tuple)
print("mixed_list:", mixed_list)  # [{1, 2}, (3, 4), [5, 6, 7]]

# remove() - removes the first matching element
prime_numbers = [2, 3, 5, 7, 9, 11]
prime_numbers.remove(9)
print("prime_numbers: ", prime_numbers)  # [2, 3, 5, 7, 11]

# count() - returns the number of times the specified element appears
numbers = [2, 3, 5, 2, 11, 2, 7]
count = numbers.count(2)
print("count:", count)

# pop() - removes the item at the specified index
prime_numbers = [2, 3, 5, 7]
removed_element = prime_numbers.pop(2)
print("pop:", prime_numbers)  # [2, 3, 7]

# remove the last item
prime_numbers.pop()
print("pop:", prime_numbers)  # [2, 3]

# reverse() - reverses the elements of the list
prime_numbers = [2, 3, 5, 7]
prime_numbers.reverse()
print("reverse:", prime_numbers)  # [7, 5, 3, 2]

# Accessing Elements in Reversed Order
systems = ["Windows", "macOS", "Linux"]
for o in reversed(systems):
    print(o)

# sort() - sorts the elements
prime_numbers = [11, 3, 7, 5, 2]
prime_numbers.sort()
print(prime_numbers)  # [2, 3, 5, 7, 11]

# Descending order
numbers = [7, 3, 11, 2, 5]
numbers.sort(reverse=True)  # [11, 7, 5, 3, 2]
print(numbers)

# String sort
cities = ["Tokyo", "London", "Washington D.C"]
cities.sort()
print("cities", cities)
cities.sort(reverse=True)
print("cities Reverse", cities)

# Reverse Strings Based on Length
text = ["abc", "wxyz", "gh", "a"]

text.sort(key=len)
print(text)  # ['a', 'gh', 'abc', 'wxyz']

# copy() - returns a shallow copy
prime_numbers = [2, 3, 5]
numbers = prime_numbers.copy()
print("copy:", numbers)  # [2, 3, 5]

# clear() - method removes all items
prime_numbers = [2, 3, 5, 7, 9, 11]
prime_numbers.clear()
print("clear:", prime_numbers)  # []


# -------------- String -> List --------------
x = "axz"
result = list(x)
print(result)  # ['a', 'x', 'z']
