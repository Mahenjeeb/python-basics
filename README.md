# Python

**Python** is a high-level, general-purpose programming language designed with an emphasis on code readability and simplicity.

#### print()
Printing 'Hello World'
```python
print("Hello World")
```
#### input()
Taking user input
```python
name = input("Enter your name ")
print(f"Hello, {name}")
```
## Type Casting
Type Casting refers to changing a datatype of a variable to another

#### int()
>Casting _string_ to _integer(int)_
```python
#Add two numbers in python
x = int(input("Enter First Number "))
y = int(input("Enter Second Number "))
print(f"sum of {x} + {y} = {x + y}")
# sum of 2 + 3 = 5
```
#### float()
>Casting _string_ to _float_

```python
# Divide two floting point numbers
x = float(input("Enter First Number "))
y = float(input("Enter Second Number "))
print(f"{x} divided by {y} = {x / y}")
# 3 divided by 2 = 1.5
```
## Built-in functions
**Python** provides several built-in mathematical functions that are integral to the language and do not require importing additional modules
### Mathmetical Operations
>#### round(_number_, _ndigits_)
Round a number to a given precision in decimal digits.

Takes two parameters
1. *number* is the value provided by the user
2. *ndigits* is number of digits/decimal places

Returns single value as a **_integer_**
```python
print(f"{round(6/7)}")
# 0.8571428571428571
print(f"{round(z,2)}")
# 0.86
```
>#### pow(_base, exp, mod_)
To calculate a power of given number

Takes three parameters
1. *base* is the number you want calulate the power
2. *exp* is sqare of a number means 2 or cube is 3 and so on
3. *mod _(optional)_* is a modulo operation of the numbers you got after calculatind the power

Returns single value as a **_integer_**
```python
pow(4,2) # 4 to the power 2 is 16
pow(3,3) # 3 to the power 3 is 27
```
>#### sum(_iterable, start_)
To Calculate sum of numberic values in an array

Takes two parameters
1. *iterable* can be an array of numeric values
2. *start* starting index of an iterable

Returns single value as a **_integer_**
```python
sum([1,2,3,4,5]) # 15
```
Other mathmatical functions are follows
```code
min(iter), max(iter), abs(x), divmod(a/b)
```
## User defined functions
Python **functions** are reusable block of statements that does a specific tasks. Helps in code resusability, modularity, redability and maintainability.

>#### Function Defination
Python functions are created using **_def_** keyword.
```python
def main():
    print("I am a user defined function")
```
>#### Function Call
Functions are called using their name enclosed with right and left paranthesis **_'()'_**

```python
main()
```
## Parameterized Function
A **_parameterized_** function in Python is a function where one or more details of its behavior are defined as parameters rather than being hardcoded within the function itself

```python
def main():
    name = input("Enter your name ")
    hello(name)
def hello(to):
    print(f"Hello, {name} 😊")
main()
```
on above code _'to'_ is a parameter to _'hello()'_ function and we passed _'name' _as and argument to '_hello()_' inside _'main()'_

**Note :**
 >_Parameter_ are variables defined in a function or method's declaration
 _Arguments_ are the concrete data supplied during a function call 

#### Default parameter
In Python, a parameterized function with _**default**_ parameters allows you to define functions where certain arguments have predefined values. This means that if a caller does not provide a value for a parameter, the _**default**_ value is used instead.

```python
def main():
    name = input("Enter your name ")
    hello() #Prints "Hello, World 😊"
    hello(name)
def hello(to = "World"):
    print(f"Hello, {to} 😊")
main()
```
Here '_to = "World"_' is a default parameter to _'hello()'_.
When user does not provide any parmeter then _'Hello, World 😊'_ will be printed.