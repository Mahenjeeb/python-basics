# def greetUser(name:str):
#     print(f"{name}")
# greetUser('Mahenjeeb')

# for _ in range(0,3):
#     print("Hello")

# square = lambda x: x*x
def result(num):
    return f"{num["name"]} and age is {num["age"]}"

res = map(result,[{"name" : "Mahenjeeb", "age" : 12}, {"name" : "Peti", "age" : 56}])
print(res)