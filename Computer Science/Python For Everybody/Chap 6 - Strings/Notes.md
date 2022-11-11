### A String is a sequence
- You can access the characters one at a time with the bracket operator.
```python
fruit = 'banana'
letter = fruit[1]
# letter is 'a'
# The expression in brackets is called an index
```
- The index starts at 0 and must be an integer.
- You can use `len` to get the length of a string.
- You get an index error if you try to access an index that is too large.
- Negative indices count backward from the end of the string.
- You can slice a string using a colon operator.
```python
s = 'Monty Python'
print(s[0:4]) # Prints 'Mont'
print(s[6:7]) # Prints 'P'
```
- The index before the colon is the starting index and the index after the colon is the ending index. The ending index is not included.
- If you omit the first index, the slice starts at the beginning of the string.
- If you omit the second index, the slice goes to the end of the string.

### Strings are immutable
- Strings are  immutable objects which means you cannot change an existing string.
- Concatenation is the process of combining two strings using the `+` operator.

### The in operator
- The `in` operater takes two strings and return `True` if the first appears as a substring in the second.
```python
'na' in 'banana' # True
'mon' in 'banana' # False
```

### String comparison
- The `==` operator works on strings.
- You can use `<` and `>` to organize strings alphabetically. The comparison is done based on the alphabetical order of the characters in the strings. Do note that capital letters come before lowercase letters.

### String methods
- Strings are an example of python object which contain data and functions (methods) and are available to any instance of the object.
- You can use dir to get a list of the methods available for a particular object. The tyoe function shows you the type of an object.
```python
stuff = 'Hello world'
type(stuff) # <class 'str'>
dir(stuff) # Shows all the methods available for the string object
```
- You can run help on an objects method to get more information about it.
```python
help(str.lower) # Shows the documentation for the lower method
```
- Upper uses dot notation but doesn't take any arguments. Instead it applies the method to the string and returns a new string. This method call is called an invocation.
```python
# More string methods
stuff = ' Hello world '
stuff.upper() # HELLO WORLD
stuff.lower() # hello world
stuff.find('o') # 4
stuff.strip() # 'Hello world'
stuff.startswith('Hello') # True
stuff.endswith('world') # False
```

### Format operator
- The format operator `%` allows you to construct strings where parts of the string are replaced by variable data.
```python
camels = 42
'I have spotted %d camels.' % camels # I have spotted 42 camels.
```
- You can look at the documentation for the `%` operator to see the list of formatting sequences.

### Glossary
- Empty String: A string with no characters and length 0, represented by two quotation marks.
- Format sequence: A format sequence is a special code that tells Python what type of data to expect and how to format it.
- Flag: A boolean variable used to indicate whether a condition is true or false.
- Method: A function that is associated with an object and called using dot notation.
- Search: A pattern of traversal that stops when it finds what it is looking for.
- Sequence: An ordered set
- Slice: A part of a string specified by a range of indices.
- Traverse: To iterate through the items in a sequence, performing a similar operation on each.

