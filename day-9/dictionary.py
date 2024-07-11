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

# loops in dictionary
for key in dict:
    print(key, dict[key])

for value in dict.values():
    print(value)

# nesting in dictionary

# 1. nesting list in dictionary
travel_log = {
    "france" : ["paris", "lyon"],
    "germany" : ["berlin", "munich"],
}

print(travel_log)

# 2. nesting dictionary in dictionary
travel_log = {
    "france" : {
        "cities_visited" : ["paris", "lyon"],
        "total_visits" : 3,
    },
    "germany" : {
        "cities_visited" : ["berlin", "munich"],
        "total_visits" : 12,
    }
}

print(travel_log)

for country in travel_log:
    print(country)
    print(travel_log[country])

# 3. nesting dictionary in list
travel_log = [
    {
        "country" : "India",
        "total_visits" : 12,
        "cities_visited" : ["Delhi", "Mumbai", "Indore"],
    },
    {
        "country" : "Korea",
        "total_visits" : 2,
        "cities_visited" : ["Seoul", "Busan"],
    },
]

print(travel_log)

for country in travel_log:
    print(country)