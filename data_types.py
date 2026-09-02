# Data Types

# int
x = 1 
# str
y = "Mahenjeeb"
# float
z = 2.1
print(z)
print(y)
print(x)

# List
# List of type int
list1 = [1,2,3,4,5]
# List of type str
list2 = ["1","2", "3"]
# List of type float
list3 = [1.1, 2.2, 3.3]
# This will give run time error. if we use 'mypy' and 'pydantic'
list4: list[int] = [{"name": "Mahenjeeb"}, {"name": "Chukra"}]
# List of type bool
list5: list[bool] = [True, False, False, True]

print(list1)
print(list2)
print(list3)
print(list4)

# Dictionaries
# Dictionary with mixed data type (bool, int, str, float)
dict1 = {
    "name": "Mahenjeeb",
    "age": 12,
    "weight": 64.2,
    "isActive": True,
}
print(dict1)
