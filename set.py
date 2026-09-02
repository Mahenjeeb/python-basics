# Set contains unique data types
set1 = {"Apple", "Orange", "Mango", "WaterMelon", "Bananna", "Apple"}
print(set1); # This will print unique elements

set2 = {"Jack Fruit", "Watermelon", "Mango"}
# Fing the diffrence btween two sets
diff = set1.difference(set2)
print(diff)
# Common between both the sets
intr = set1.intersection(set2)
print(intr)
# Adds two sets including duplicates
unn = set1.union(set2)
print(unn)
# Add vaues to existing set
set1.update({1,2})
print(set1)
# delete all elements in set
set1.clear()
print(set1)