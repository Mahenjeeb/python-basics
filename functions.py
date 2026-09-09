import math
# parameterized function
def greetUser(name:str):
    print(f"{name}")
greetUser('Mahenjeeb')

def areaOfCirlce(radius):
    area = math.pi * radius * radius
    return area
print(areaOfCirlce(2))

# Anonymous function aka lamda. one time use only 
even = lambda x:x/2
print(even(12))

name = lambda name: name
print(name("Mahenjeeb"))

numList = [1,2,3]
# Using normal function
def sqNum(num):
    return num ** 2
print(list(map(sqNum, numList)))
# Using lamda function
print(list(map(lambda x:x ** 2, numList)))

nmAgeList = [{"name": "Mahenjeeb", "age": 18}, {"name": "Peti", "age": 54}, {"name": "tinga bapa", "age": 56}]
filNmAgeList = list(filter(lambda nmDict: nmDict["age"] > 50, nmAgeList))
print(filNmAgeList)