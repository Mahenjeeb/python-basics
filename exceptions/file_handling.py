# creating file with 'open' and 'write' method
file = open("peti.txt", "w")
try:
    file.write("Dantha Ragudi")
except Exception as e:
    print("File Error", e)
finally:
    file.close()
    
# Creating and handling file with 'with' keyword
# It internally uses '__enter__' and '__exit__'
with open("Tinga_Bapa.txt", "w") as file:
    file.write("Kat Kati")