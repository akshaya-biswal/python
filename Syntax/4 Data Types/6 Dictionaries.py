# valid
my_dict = {1: "one", 2: "two", 3: "three"}
my_dict = {(1, 2): "one two", 3: "three"}
my_dict = {"USA": ["Chicago", "California", "New York"]}

# invalid
# Error: list as a key is not allowed
# my_dict = {1: "Hello", [1, 2]: "Hello Hi"}

# Access
country_capitals = {"Germany": "Berlin", "Canada": "Ottawa", "England": "London"}
print(country_capitals["Germany"])  # Berlin
print(country_capitals["England"])  # London

# Add
country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
}
country_capitals["Italy"] = "Rome"
print(country_capitals)

# Delete
country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
}
del country_capitals["Germany"]
print(country_capitals)

# Clear
country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
}
country_capitals.clear()
print(country_capitals)

# Change
country_capitals = {"Germany": "Berlin", "Italy": "Naples", "England": "London"}
country_capitals["Italy"] = "Rome"
print(country_capitals)
