# Nested dictionaries
dict2 = {
    "name": "Mahenjeeb",
    "age": 12,
    "weight": 64.2,
    "isActive": True,
    "cars": ["Mercedez", "BMW", "Porsche"]
}
print(dict2)

# Accessing Dictionary elements
print(dict2["name"])
print(dict2["weight"])
print(dict2["cars"][1])

# dictionary methods
# fromkeys() used to create a dctionaries from the iterable keys and then you can specify their values in second arguments
print(dict.fromkeys("abc", "!"))
print(dict.fromkeys([1, 2, 3], 1))
# items() will return a set like object for tagged dictionries
dict3 = dict2.items()
print(dict3)
# keys() Return all the keys in dictionary in a form of list
print(dict2.keys())
# get() used to get the spefied value of the key
print(dict2.get("name"))


