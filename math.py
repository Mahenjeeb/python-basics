import math

float1 = 12.96
int1 = 45

# Math Methods
# math.ceil() - given float type value + 1
print(math.ceil(float1))
# math.floor() - base value before decimal of float type data
print(math.floor(float1))
# math.factorial() - Factorial of number 5! = 5*4*3*2*1 = 120
print(math.factorial(5))
# math.gcd() - greatest common divisor between int data type provided comma separated
print(math.gcd(2,4,6))
# math.lcm() - largest common multiple between int data type provided comma separated
print(math.lcm(2,4,6))
# PI value and it's a readonly value
print(math.pi)

# Area of circle pi * radius * radius
radius = 4
print("Area of circle",math.pi * radius * radius)
# Perimeter of circle 2 * pi * radius
print("Perimeter of circle", 2 * math.pi * radius)