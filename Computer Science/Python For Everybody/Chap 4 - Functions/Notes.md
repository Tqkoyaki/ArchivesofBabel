### Function calls
- A function is a named sequence of statements that perform a computation.
```python
# An example of a function call
type(32)
```
- Expressions in parentheses are called the arguments of the function.
- It is common to say that a function takes arguments and returns a result. The result is called the return value.
  
### Built-in functions
- Python provides numerous built-in functions
```python
max('Hello world')
min('Hello world')
# These give you the largest character and the smallest character in the string
# They serve to give you the largest and smallest values in a list
```
```python
# Gives you the length of the string or any list
len('Hello world')
```
- Avoid using the name of a built-in function as a variable name. It is considered bad practice.

### Type conversion functions
- There are many functions that convert values from one type to another.
```python
int('32') # Converts any argument to an integer
float('3.14159') # Converts any argument to a floating point number
str(32) # Converts any argument to a string
```

### Math functions
- Python has a math module that can be used after importing it.
```python
import math
print(math) # Shows us that this is a module object which contains functions and variables defined in the module.

# To use functions from math module, we need to use the dot notation
math.log10(1000) # Gives us the log base 10 of 1000
math.sin(0.5) # Gives us the sine of 0.5 radians
math.pi # Gives us the value of pi
```

### Random numbers
- Given the same inputs, most computers generate the same outputs everytime making them deterministic.
- Making a program truly nondeterministic is difficult, but we can write programs that seem to be nondeterministic by generating psudeorandom numbers.
- Psudeorandom numbers are not truly random because they are generated by a deterministic computation but they are almost impossible to distinguish from random.
```python
import random # Module has functions that generate pseudorandom numbers
random.random() # Gives us a random float between 0.0 and 1.0
random.randint(5, 10) # Gives us a random integer between 5 and 10
t = [1, 2, 3]
random.choice(t) # Chooses a random element from a sequence
```

### Adding new functions
- A function definition specifies the name of a new function and the sequence of statements that execute when the function is called.
```python
def print_hello():
    print('Hello world!')
# The def keyword indicates that this is a function definition. 
# The name is print_hello (same rules as variable names)
```
- The first line of a function definition is called the header; the rest is called the body. Headers have to end with a colon and body has to be indented.
- The type of a function is a function object. so print_hello is a function object.
- You can have functions instead functions
```python
def repeat():
    print_hello()
    print_hello()
```

### Flow of execution
- Execution always begins at the first statement of the program. Statements are executed one at a time, in order from top to bottom.
- Statements inside a function do not run until the function is called (functions are like detours in the flow of execution).
  
### Parameters and arguments
- You are pass arguments to a function when you call it.
- To allow the function to accept arguments, you have to assign them to variables called parameters.
```python
def print_twice(bob):
    print(bob)
    print(bob)
# bob is a parameter
```
- The arguments are evaluated before the function is called.

### Fruitful functions and void functions
- Functions like math functions yield results while functions like print_twice don't return a value but only perform an action. These are called void functions.
- None is a special type of value that means nothing.
```python
def addtwo(a, b):
    added = a + b
    return added
# The return statement ends the function and returns the value to the caller.
```

### Why functions?
- Creating a new function gives you an opportunity to name a group of statements making it easier to read and understand
- You can eliminate repetitive code
- Dividing a long program into functions allows you to debug parts of it.
- Allows for more reusability

### Debugging
- Becareful of tabs and spaces in your code. They can cause errors if the text editor you are using is not configured properly or you are missing spaces or tabs.

### Glossary
- Algorithm: A general process for solving a category of problems.
- Composition: Using an expression as part of a larger expression, or a statement as part of a larger statement.


