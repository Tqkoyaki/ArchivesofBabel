### What do we do to a Python statement that is immediately after an if statement to indicate that the statement is to be executed only when the if statement is true?
a) Indent the line below the if statement

### Which of these operators is not a comparison / logical operator?
e) =

### What is true about the following code segment:
```python
if x == 5:
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
```
a) Depending on the value of x, either all three of the print statements will execute or none of the statements will execute

### When you have multiple lines in an if block, how do you indicate the end of the if block?
a) You de-indent the next line past the if block, how do you indicate the end of the if block?

### You look at the following text:
```python
if x == 6:
    print('Is 6')
    print('Is Still 6')
    print('Third 6')
```
### It looks perfect but Python is giving you an 'Indentation Error' on the second print statement. What is the most likely reason?
a) You have mixed tabs and spaces in the file

### What is the Python reserved word that we use in two-way if tests to indicate the block of code that is to be executed if the logical test is false?
a) else

### What will the following code print out?
```python
x = 0
if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
print('All done')
```
a) Small All done

### For the following code,
```python
if x < 2:
    print('Below 2')
elif x >= 2:
    print('Two or more')
else:
    print('Something else')
```
### What value of 'x' will cause 'Something else' to print out?
a) This code will never print 'Something else' regardless of the value of 'x'

### In the following code (numbers added) - what will be the last line to execute successfully?
```python
(1) astr = 'Hello bob'
(2) istr = int(astr)
(3) print('First', istr)
(4) astr = '123'
(5) istr = int(astr)
(6) print('Second', istr)
```
a) 1

### For the following code,
```python
astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
```
### What will the value be for istr after this code executes?
a) -1