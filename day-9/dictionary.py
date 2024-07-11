# Dictionaries in python

# Creating a dictionary
dict = {
    "one" : "value1",
    "two" : "value2",
    "three" : "value3",
    "four" : "value4",
}

# Accessing values
print(dict["one"])
print(dict["two"])
print(dict["three"])
print(dict["four"])

# Printing dictionary
print(dict)

# Adding new key value pair
dict["five"] = "value5"

# Printing dictionary
print(dict)

# Removing key value pair
del dict["two"]

# Printing dictionary
print(dict)

# Checking if key exists
print("one" in dict)