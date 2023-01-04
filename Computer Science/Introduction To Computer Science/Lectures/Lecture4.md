# Decomposition, Abstraction, Functions
- Functions are mechanisms to achieve decomposition and abstraction
- Abstraction idea is that we do not need to know how something works to use it
- Decomposition idea is that we can break a problem into smaller pieces and have them work together to achieve an end goal
- We divide code into modules. They are self contained, break up code, and are reusable. This lets our code be more organized and more coherent. For now we will do it with functions but we will also do it with classes.
- We achieve abstraction with function specifications or docstrings.
- Functions are reusable chunks of code. Functions are not run until they are called or invoked. They have a name, parameters (0 or more), a docstring (optional), a body, and a return value.
```python
def is_even(i):
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print("inside is_even")
    return i % 2 == 0

is_even(3)
```
- Formal parameters get bounded to the value of the actual parameter when the function is called.
- New scope/frame/environment are created when you enter a function.
- Scope is mapping of names to objects.
- Python returns the value None which represents the absence of a value.
- Returns only have meaning inside a function and prints can be used anywhere. There can also only be one return value while you can have multiple prints.
- Functions can be passed as parameters to other functions.
- When you are inside a function, you can access a variable defined outside unless it is shadowed by a variable with the same name inside the function. The function inside cannot modify a variable defined outside unless you use the `global` keyword but it is frowned upon.
- Code can be used many times but only has to be debugged once.