# num_list = [5,1,7,8,9,3]
# for num in num_list:
#     print(num)
# # len(list/dict/set) - used for getting number of items in list, set and dictinaries
# dict1 = {
#     "name": "Mahenjeeb",
#     "age": 12
# }
# set1 = {"orange", "apple", "bananna"}
# print(len(dict1), len(set1))

# # range(start, stop, step) - used to limit our loops. start = 0, stop = 6 (len(num_list)), step = 2
# for num in range(0, len(num_list), 2):
#     print(num_list[num])

# number = 10  
# while number >= 1:
#     print(number)
#     number -= 1
    
# iter = 10
# for i in range(1, iter):
#     if i == 2:
#         # continue - skips the element if condition is true
#         continue
#     if i == 9:
#         # break - Terminate loop if condtion is true
#         break
#     print(i)
    
# Enumurate - Useful for indexed List
enumList = ["Hello", "How", "Are", "You", "?"]
for index, item in enumerate(enumList, start=1):
    print(index, item)

# Zip - 
for name, bill in zip(['Peti Lata', 'Tinga Bapa'],['500','1']):
    print(name, bill)