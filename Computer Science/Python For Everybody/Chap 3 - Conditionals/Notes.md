### Boolean Expressions
- A boolean expression is an expression that is either true or false.
- True and False belong to the bool class.
```python
x == y # x is equal to y
x != y # x is not equal to y
x > y # x is greater than y
x < y # x is less than y
x >= y # x is greater than or equal to y
x <= y # x is less than or equal to y
x is y # x is the same as y
x is not y # x is not the same as y
```
- Single = is an assignment operator, while == is a comparison operator. Also =< and => do not exist.

### Logical Operators
- Logical operators are and, or, and not.
- Ex. x > 0 and x < 10 is true only if x is greater than 0 and less than 10.
- Any nonzero number is interpreted as true.

### Conditional Execution
- Conditional statements give us the ability to check conditions and change the behavior of the program accordingly.
```python
if x > 0:
    print('x is positive')
```
- The stament consists of a header line that ends with the colon character (:) followed by an indented block. These statements are called compound statements.
- There needs to be at least one statement in the body, you can bypass this requirement by using the pass statement which does nothing (A placeholder).
  
### Alternative Execution
- An alternative execution is an alternative set of statements that are executed when an if statement is false.
```python
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')
```
- This follows an If-Then-Else pattern. The alternatives are called branches and exactly one of the branches will be executed.

### Chain Conditionals
- A chain conditional is a series of if statements where each statement is a branch of the previous one.
```python
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')
```
- There are no limits on the number of elif statements. If there is an else clause, it has to be at the end, but there doesn't have to be one.

### Nested Conditionals
- One conditional can also be nested within another.
```python
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
```
- Usually a good idea to avoid nested conditionals because they become hard to read very quickly. Use them sparingly.

### Catching Exceptions Using try and except
- The try and except statements catch and handle exceptions. Treat them like an insurance policy for your code.
```python
inp = input('Enter Fahrenheit Temperature: ')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')
```

### Short-circuit Evaluation of Logical Expressions
- Take and for example, a logical expression with and is run from left to right and if one operand is false, there is no point running the rest because the whole statement will be false no matter what. This early stop is short-circuit evaluation.
```python
# Guardian pattern
x = 1
y = 0
x >= 2 and (x/y) > 2
# This will pose no error if x >= 2 is false because the 
# second operand will not be evaluated. If it is there is a
# ZeroDivisionError.
y != 0 and (x/y) > 2
# y != 0 is the guard to insure that the second operand is
# not evaluated if y is 0.
```

### Glossary
Body: The sequence of statements inside a compound statement.
Branch: One of the alternative sequences of statements in a conditional statement.
Comparison operator: One of the operators that compares its operands: ==, !=, >, <, >=, and <=.
Guardian pattern: A pattern that takes advantage of short-circuit evaluation.
Logical operator: One of the operators that combines boolean expressions: and, or, and not.
Traceback: A list of the functions that were executing when an exception occurred.

