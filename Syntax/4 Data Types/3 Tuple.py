# tuple cannot be modified once it is created
# Ordered
# Immutable
# Allow duplicates

languages = ("Python", "Swift", "C++")

# access the first item
print(languages[0])  # Python

# access the third item
print(languages[2])  # C++

# trying to modify a tuple
# languages[0] = "Java"  # error

# Length
print("Total Items:", len(languages))

# Check
print("Python" in languages)  # True


# Iterate
for lang in languages:
    print(lang)
