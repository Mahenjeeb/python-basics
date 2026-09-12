# Catching exception
value = 10
try:
    if(value > '9'):
        print("value is less")
except TypeError as e:
    print(e)
else:
    print("lata")
finally:
    print("done")
    
# Raising Exception
name = "Mah"
if(len(name) <= 3):
    # raise key is use to raise an exception
    raise ValueError("Name must be grater than 3")
else:
    print("Name is fine")

# Creatin custom exception
class LengthException(Exception):
    pass

name2 = "io"
if(len(name2) <= 3):
    raise LengthException("Short length")
else:
    print("All good")