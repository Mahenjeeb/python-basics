# Type Casting default string input to integer(int)
a = int(input("What is a? "))
b = int(input("What is b? "))

print(f"Added {a}, {b} and sum is {a+b} ")
# Formated to comma between 3 digits, if number of digits are more than 3
print(f"Added {a}, {b} and sum is {(a+b):,} ")

x = float(input("What is X? "))
y = float(input("What is Y? "))
z = x / y;
# Rounding the floating number to a nearest whole number 
print(f"{round(z)}")
# Rounding the number and keep 2 decimal places (if any)
print(f"{round(z,2)}")
# short-hand to keep number upto 2 decimal places
print(f"{(z):.2f}")

pow()
sum()