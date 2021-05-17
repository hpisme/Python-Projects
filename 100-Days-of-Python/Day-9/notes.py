# Creating a dictionary
travel_list = {
  'Mexico': 2021,
  'Iceland': 2020,
  'Italy': 2019,
  'Croatia': 2019,
}

print(travel_list,"\n")

# Accessing dictionary items.

# Items method (retrieves key:value pairs)
print(travel_list.items(), "\n")

# Values method (retreives the values in a dictionary)
print(travel_list.values(), "\n")

# Keys method (retrieves the keys in a dictionary)
print(travel_list.keys(), "\n")

# Get method (retrieves a specific key's value)
# Can add a value to return if the item doesn't exist
print(travel_list.get("Mexico"), "\n")
print(travel_list.get("Belize", "That destination doesn't exist."), "\n")

# Another way to get a key's value
print(travel_list["Mexico"], "\n")

# Changing dictionary items

# Method 1 
travel_list["Mexico"] = 2022
print(travel_list["Mexico"],"\n")

# Method 2
travel_list.update({"Mexico": 2023})
print(travel_list, "\n")

# Adding Items

# Method 1
travel_list["Costa Rica"] = 2021

# Method 2
travel_list.update({"Italy": 2022})

print(travel_list, "\n")

# Removing Items

# Method 1
travel_list.pop("Mexico")

# Method 2

travel_list.popitem() #removes last inserted item
print(travel_list, "\n")

# Method 3

del travel_list["Croatia"]
print(travel_list, "\n")

# Method 4 (clears the dictionary)

travel_list.clear()
print(travel_list, "\n")

# Looping through a dictionary 

travel_list = {
  'Mexico': 2021,
  'Iceland': 2020,
  'Italy': 2019,
  'Croatia': 2019,
}

# Method 1 (prints key names)
for x in travel_list:
  print(x)

print("\n")

# Method 2 (prints values)
for x in travel_list:
  print(travel_list[x])

print("\n")
# Method 3
for x in travel_list:
  print(travel_list.keys())

print("\n")
# Method 4
for x in travel_list:
  print(travel_list.values())

print("\n")

# Method 5
for x, y in travel_list.items():
  print(x, y)
print("\n")
# Nested Dictionaries
new_travel_list = {
  2021 : {
    "Mexico" : "Trip 1",
    "Costa Rica" : "Trip 2"
  }
}

print(new_travel_list)
