### Values and Types
- Values are basic things a program works with like numbers and text.
- 2 is an example of an integer.
- "Hello, World!" is an example of a string.
- print also works for integers.
```python
# This command tells you the type of a value
type('Hello, World!')
type(17)
```
- floating points (floats) are numbers with decimal points.
- Anything in quotes is a string.
```python
# An assignment statement creates new variable and gives them values.
n = 17
```

### Variable Names and Keywords
- Variable names can be long, contain both letters and numbers, but they can't start with a number. It is legal to use uppercase letters. Underscores are legal in variable names and can even be the first character.
- Variable names cannot be keywords.

### Statements
- A statement is a unit of code that the Python interpreter can execute.

### Operators and Operands
- Operators are special symbols that represent compuations like addition and multiplication. The values the operator is applied to are called operands.
- Operations inlcude +, -, *, /, and ** (exponent).
- In Python 2, the / operator performs integer division so 59 / 60 would equal 0. In Python 3, the / operator performs floating point division so 59 / 60 would equal a decimal number. To perform integer division in Python 3, you must use //.

### Expressions
An expression is a combination of values, variables, and operators. 7, x, x + 1 are all examples of expressions assuming x has been assigned a value.

### Order of Operations
- The order of operations is the same as in math. Parentheses have the highest precedence then comes exponents. Multiplication and division are performed are exponents but before addition and subtraction. Operators with the same precedence are evaluated from left to right.
  
### Modulus Operator
- The modulus operator works on integers and yields the remainder when the first operand is divided by the second. The modulus operator is a percent sign (%).

### String Operations
- The + operator works with strings by performing concatenation meaning it joins the strings together by linking them end to end.
- The * operator also works with strings by repeating the string a given number of times. This means that one operand must be a string and the other must be an integer.
  
### Asking the User for Input
```python
# This takes an input from a user, the program will pause and wait for the user to type something and press enter or return before continuing the program. The input function was raw_input in Python 2. The parameter is a prompt that is displayed to the user.
inp = input()
```
- The sequence \n at the end of the prompt represents the newline character which is a special character that causes a line break.
- You can convert a value to an integer using the `int()` function. It will return an error if a string that is not a string of digits is entered. (ValueError)
  
### Comments
- Comments are notes in programs that are ignored by Python. They start with the # symbol and last from that spot until the end of the line.

### Choosing mnemonic variable names
- You should pick variables names that help deliver the intent of the program making it easier to read and understand.

### Debugging
- Variables are case-sensitive. Common errors include misspelling a variable name or forgetting to assign a value to a variable. One can also mess up the order of operations.

### Glossary
- Evaluate: To simplify an expression to yield a single value.
- Floating point: A type that represents numbers with fractional parts.
- Rules of precedence: The set of rules governing the order in which expressions involving multiple operators and operands are evaluated.
- Type: A category of values like ints, floats, and strings.

