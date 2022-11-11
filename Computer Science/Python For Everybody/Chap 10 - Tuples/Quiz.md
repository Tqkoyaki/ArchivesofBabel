### What is the difference between a Python tuple and Python list?
b) Lists are mutable and tuples are not mutable

### Which of the following methods are available for both Python lists and Python tuples?
c) index()

### What will end up in the variable y after this code is executed?
```python
x , y = 3, 4
```
c) 4

### In the following Python code, what will end up in the variable y?
```python
x = \{ 'chuck' : 1 , 'fred' : 42, 'jan': 100\}
y = x.items()
```
b) A list of tuples

### Which of the following tuples is greater than x in the following Python sequence? 
```python
x = (5, 1, 3)
if ??? > x :
   ...
```
b) (6, 0, 0)

### What does the following Python code accomplish, assuming the c is a non-empty dictionary?
```python
tmp = list()
for k, v in c.items() :
    tmp.append( (v, k) )
```
b) It creates a list of tuples where each tuple is a value, key pair

### If the variable data is a Python list, how do we sort it in reverse order?
b) data.sort(reverse=True)

### Using the following tuple, how would you print 'Wed'?
```python
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
```
d) print(days[2])

### In the following Python loop, why are there two iteration variables (k and v)?
```python
c = \{'a':10, 'b':1, 'c':22\}
for k, v in c.items() :
    ...
```
b) Because the items() method in dictionaries returns a list of tuples

### Given that Python lists and Python tuples are quite similar - when might you prefer to use a tuple over a list?
b) For a temporary variable that you will use and discard without modifying