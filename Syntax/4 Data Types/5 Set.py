# unique data, set cannot be duplicated.
student_id = {112, 114, 116, 118, 115}
vowel_letters = {"a", "e", "i", "o", "u"}
mixed_set = {"Hello", 101, -2, "Bye"}

print("student_id:", student_id)
print("vowel_letters:", vowel_letters)
print("mixed_set:", mixed_set)

# Duplicate
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)  # {8, 2, 4, 6}

# Add
numbers = {21, 34, 54, 12}
numbers.add(32)
print("Add:", numbers)

# Update
companies = {"Lacoste", "Ralph Lauren"}
tech_companies = ["apple", "google", "apple"]
companies.update(tech_companies)
print(companies)  # {'Lacoste', 'Ralph Lauren', 'google', 'apple'}

# Discard
languages = {"Swift", "Java", "Python"}
removedValue = languages.discard("Java")
print("discard:", languages)

# Length
even_numbers = {2, 4, 6, 8}
print("even_numbers:", len(even_numbers))

# Union
A = {1, 3, 5}
B = {0, 2, 4}
print("union:", A.union(B))

# Intersection
A = {1, 3, 5}
B = {1, 2, 3}
print("intersection:", A.intersection(B))

# Difference
A = {2, 3, 5}
B = {1, 2, 6}
print("difference:", A.difference(B))

# symmetric_difference: includes all elements of A and B without the common elements
A = {2, 3, 5}
B = {1, 2, 6}
print("symmetric_difference:", A.symmetric_difference(B))

# check if two sets are equal
A = {1, 3, 5}
B = {3, 5, 1}
if A == B:
    print("Set A and Set B are equal")
else:
    print("Set A and Set B are not equal")

# dictionary
