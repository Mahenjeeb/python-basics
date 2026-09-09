# List Comprehensions
natNumList = [1,2,3,4,5,6]
numListRes = [num for num in natNumList if num % 2 == 0]
print(numListRes)

# Set Comprehensions
amntSet = {10000, 5000, 7889, 4567, 8867}
amntSetRes = {x for x in amntSet if x % 2 == 0}
print(amntSetRes)

# Dict comprehensions
dictAge = {
    "Revathy": 15,
    "Divya": 18,
    "Guduly": 43,
    "Sangeeta": 54,
    "Manaswini": 90,
    "Padmaja": 25,
    "Mahenjeeb": 56
}
dictAgeRes = {prop:age/2 for prop, age in dictAge.items()}
print(dictAgeRes)

# Generator Comprehensions
total = 0
sumNatNum = sum(res for res in natNumList if res > 3)
print(sumNatNum)

