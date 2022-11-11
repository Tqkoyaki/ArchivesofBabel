### How are Python dictionaries different from Python lists?
b) Python lists maintain order and dictionaries do not maintain order

### How are Python dictionaries different from Python lists?
b) Python lists are indexed using integers and dictionaries can use strings as indexes

### What is a term commonly used to describe the Python dictionary feature in other programming languages?
b) Associative arrays

### What would the following Python code print out?
```python
stuff = dict()
print(stuff['candy'])
```
b) The program would fail with a traceback

### What would the following Python code print out? 
```python
stuff = dict()
print(stuff.get('candy',-1))
```
b) -1

### (T/F) When you add items to a dictionary they remain in the order in which you added them.
a) False

### What is a common use of Python dictionaries in a program?
b) Building a histogram counting the occurrence of various strings in a file

### Which of the following lines of Python is equivalent to the following sequence of statements assuming that counts is a dictionary?
```python
if key in counts:
    counts[key] = counts[key] + 1
else:
    counts[key] = 1
```
c) counts[key] = counts.get(key,0) + 1

### In the following Python, what does the for loop iterate through?
```python
x = dict()
...
for y in x :
     ...
```
b) It loops through the keys in the dictionary

### Which method in a dictionary object gives you a list of the values in the dictionary?
a) values()

### What is the purpose of the second parameter of the get() method for Python dictionaries?
b) To provide a default value if the key is not found