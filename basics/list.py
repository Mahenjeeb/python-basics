list1 = [6,7,8,9,1,3,4]

# Accessing List Element
# First element
print(list1[0])
# Last Element
print(list1[-1])

# List Methods
# append() - appends number 9 to the lst of the list index
print(list1.append(9))
print(list1)

# Makes a shallow copy
list2 = ["6", "9", [1,3,4]]
list3 = list2.copy()
list2[2] = "Mahenjeeb"
print(list3, list2)
# Insert value at specified index
list1.insert(-1, 78)
print(list1)
# Remove the first occerence of the value
list1.remove(7)
print(list1)
# removes the value at specified index
list1.pop(4)
print(list1)
# Sort elements in the list by ascending or descending order
# reverse = True is descending order False is asceding. by defualt it returns ascending order
list1.sort()
print(list1)

# Add some extra list item to existing list. new list will have the added values.
#Wwhere original list remains unchanged
listy = list1.__add__([50,80,90])
print("Added List",listy, list1)