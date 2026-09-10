# walrus operator is used to evaluate and assgin value to the variable

from datetime import datetime
import math
if(age := int(input(">>Enter age\n")) >= 18):
    print("Adult")
else:
    print("Teenager")
    
print(f"today is {(d := datetime.now())}, {d.time()}")
