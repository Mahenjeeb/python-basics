# Python

**Definition:** Python is a high-level, general-purpose programming language designed with an emphasis on code readability and simplicity.

## Built-in I/O Functions

### print()
**Definition:** A built-in function used to output text or data to the console.

**Example:**
```python
print("Hello World")
```

### input()
**Definition:** A built-in function that reads user input from the console and returns it as a string.

**Example:**
```python
name = input("Enter your name ")
print(f"Hello, {name}")
```
## Type Casting

**Definition:** Type casting is the process of converting a variable from one data type to another. Python provides built-in functions to perform type casting.

### int()
**Definition:** Converts a value to an integer data type. Useful for converting strings from user input to integers for mathematical operations.

**Example:**
```python
# Add two numbers in python
x = int(input("Enter First Number "))
y = int(input("Enter Second Number "))
print(f"sum of {x} + {y} = {x + y}")
# Output: sum of 2 + 3 = 5
```

### float()
**Definition:** Converts a value to a floating-point (decimal) number data type. Used for calculations requiring decimal precision.

**Example:**
```python
# Divide two floating point numbers
x = float(input("Enter First Number "))
y = float(input("Enter Second Number "))
print(f"{x} divided by {y} = {x / y}")
# Output: 3 divided by 2 = 1.5
```
## Built-in Functions

**Definition:** Built-in functions are pre-defined functions that are integral to Python and do not require importing additional modules.

### Mathematical Operations

#### round(number, ndigits)
**Definition:** Rounds a number to a specified number of decimal places.

**Parameters:**
- `number`: The value to be rounded
- `ndigits`: The number of decimal places (optional)

**Returns:** An integer or float depending on the parameters

**Example:**
```python
print(round(6/7))      # Output: 1
print(round(6/7, 2))   # Output: 0.86
```

#### pow(base, exp, mod)
**Definition:** Calculates the power of a number (base raised to an exponent), with optional modulo operation.

**Parameters:**
- `base`: The base number
- `exp`: The exponent (power)
- `mod`: Optional modulo operation on the result

**Returns:** An integer representing the power calculation

**Example:**
```python
pow(4, 2)    # Output: 16 (4^2)
pow(3, 3)    # Output: 27 (3^3)
```

#### sum(iterable, start)
**Definition:** Calculates the sum of all numeric values in an iterable (like a list).

**Parameters:**
- `iterable`: A sequence of numeric values (list, tuple, etc.)
- `start`: Starting value for the sum (optional, default is 0)

**Returns:** An integer representing the total sum

**Example:**
```python
sum([1, 2, 3, 4, 5])  # Output: 15
```

#### Other Mathematical Functions
- `min(iterable)`: Returns the smallest value
- `max(iterable)`: Returns the largest value
- `abs(x)`: Returns the absolute value
- `divmod(a, b)`: Returns quotient and remainder
## User Defined Functions

**Definition:** User-defined functions are reusable blocks of code that perform specific tasks. They help improve code reusability, modularity, readability, and maintainability.

### Function Definition
**Definition:** Creating a function using the `def` keyword to define a reusable block of code.

**Syntax:**
```python
def function_name():
    # function body
    pass
```

**Example:**
```python
def main():
    print("I am a user defined function")
```

### Function Call
**Definition:** Executing a function by using its name followed by parentheses.

**Example:**
```python
main()  # Calls the main function
```
## Parameterized Functions

**Definition:** A parameterized function in Python is a function where one or more details of its behavior are defined as parameters rather than being hardcoded within the function itself.

### Parameters and Arguments

**Definition - Parameter:** A variable defined in a function's declaration that acts as a placeholder for data.

**Definition - Argument:** The actual concrete data supplied when calling a function.

**Example:**
```python
def main():
    name = input("Enter your name ")
    hello(name)

def hello(to):
    print(f"Hello, {to} 😊")

main()
```

In the above code:
- `to` is a **parameter** of the `hello()` function
- `name` is an **argument** passed to the `hello()` function

### Default Parameters

**Definition:** Default parameters allow you to define functions where certain arguments have predefined values. If a caller does not provide a value for a parameter, the default value is used instead.

**Example:**
```python
def main():
    name = input("Enter your name ")
    hello()        # Prints "Hello, World 😊"
    hello(name)    # Prints "Hello, [name] 😊"

def hello(to="World"):
    print(f"Hello, {to} 😊")

main()
```

In this example, `to="World"` is a default parameter. When the user does not provide any argument, "Hello, World 😊" will be printed.

## Conditionals

**Definition:** Conditionals are programming structures that execute code blocks based on specific logical conditions. They allow your program to make decisions and control the flow of execution.

### Conditional Operators

**Definition:** Operators used to compare values and create conditions for decision-making.

- `<` : Less than
- `<=` : Less than or equal to
- `>` : Greater than
- `>=` : Greater than or equal to
- `==` : Equals to
- `!=` : Not equals to

### if Statement

**Definition:** The `if` statement executes a block of code only if a specified condition is True.

**Syntax:**
```python
if condition:
    # executes if condition is True
```

**Example:**
```python
x = int(input("Enter first number "))
y = int(input("Enter second number "))

if(x > y):
    print("X is Greater Than Y")
if(y > x):
    print("Y is Greater Than X")
if(x == y):
    print("X is Equal To Y")
```

**Output:**
```
Enter first number 5
Enter second number 6
Y is Greater Than X
```

### if-elif-else Statement

**Definition:** The `if-elif-else` structure allows you to test multiple conditions and execute different blocks of code based on which condition is True.

**Syntax:**
```python
if condition:
    # executes if condition is True
elif another_condition:
    # executes if previous conditions are False and this is True
else:
    # executes if all conditions are False
```

**Example:**
```python
x = int(input("Enter first number "))
y = int(input("Enter second number "))

if(x > y):
    print("X is Greater Than Y")
elif(y > x):
    print("Y is Greater Than X")
elif(x == y):
    print("X is Equal To Y")
else:
    print("Invalid input")
```

**Output:**
```
Enter first number 5
Enter second number 5
X is Equal To Y
```

### Logical OR Operator

**Definition:** The `or` keyword combines multiple conditions and executes code if ANY one condition is True.

**Syntax:**
```python
if(condition1 or condition2):
    # executes if any one condition is True
else:
    # executes if all conditions are False
```

**Example:**
```python
x = int(input("Enter first number "))
y = int(input("Enter second number "))

if(x < y or x > y):
    print("X is not Equal To Y")
else:
    print("X is Equal To Y")
```

**Output:**
```
Enter first number 6
Enter second number 7
X is not Equal To Y
```

### Logical AND Operator

**Definition:** The `and` keyword combines multiple conditions and executes code only if ALL conditions are True.

**Syntax:**
```python
if(condition1 and condition2):
    # executes if all conditions are True
else:
    # executes if any condition is False
```

**Example:**
```python
score = int(input("Enter score number "))
if(score > 90):
    print("Grade A")
elif(score <= 90 and score >= 80):
    print("Grade B")
elif(score <= 80 and score >= 60):
    print("Grade C")
elif(score <= 60 and score >= 40):
    print("Grade D")
elif(score < 40):
    print("Failed")
else:
    print("Invalid Code")
```

**Output:**
```
Enter score number 81
Grade B
```

### Ternary Operator (Short-hand If-else)

**Definition:** A concise way to write an if-else statement in a single line. Returns one value if a condition is True, and another value if False.

**Syntax:**
```python
value_if_true if condition else value_if_false
```

### match Statement

**Definition:** The `match` statement (Python 3.10+) is used for pattern matching. It compares a variable against multiple case values and executes the corresponding code block.

**Syntax:**
```python
match variable:
    case value1:
        # statements
    case value2:
        # statements
    case _:
        # default statements (underscore represents any other value)
```

**Example:**
```python
selection = int(input("Select your choice "))
match selection:
    case 1 | 10 | 100:
        print("King")
    case 2:
        print("Queen")
    case _:
        print("Invalid selection")
```

**Output:**
```
Select your choice 7
Invalid selection
```
## Loops

**Definition:** Loops are control flow statements that allow the repetition of a block of code multiple times. They are essential for automating repetitive tasks.

### While Loop

**Definition:** The `while` loop executes a block of code repeatedly as long as a specified condition is True.

**Syntax:**
```python
while(condition):
    # executable statements
```

**Example:**
```python
i = 1
while(i <= 3):
    print(i)
    i += 1
```

**Output:**
```
1
2
3
```

### For Loop

**Definition:** The `for` loop iterates over a sequence (list, tuple, string, etc.) and executes a block of code for each element.

**Syntax:**
```python
for variable in sequence:
    # executable statements
```

#### Iterating Over Lists

**Definition:** Looping through each element in a list.

**Example:**
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
cherry
```

#### Iterating with `range()`

**Definition:** The `range()` function generates a sequence of integers, commonly used with for loops to repeat code a specific number of times.

**Syntax:**
```python
range(stop)              # Start at 0, go up to stop-1
range(start, stop)       # Start at start, go up to stop-1
range(start, stop, step) # Start at start, go up to stop-1, increment by step
```

**Example 1 - Using range(stop):**
```python
for i in range(5):
    print(i)
```

**Output:**
```
0
1
2
3
4
```

**Example 2 - Using range(start, stop):**
```python
for i in range(2, 5):
    print(i)
```

**Output:**
```
2
3
4
```

**Example 3 - Using range(start, stop, step):**
```python
for i in range(0, 10, 2):
    print(i)
```

**Output:**
```
0
2
4
6
8
```

#### Loop Control Statements

**Definition:** Keywords used to alter the flow of a loop.

- `break`: Terminates the loop immediately
- `continue`: Skips the current iteration and moves to the next

**Example - Using break:**
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

**Output:**
```
0
1
2
```

**Example - Using continue:**
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

**Output:**
```
0
1
3
4
```