### Given the architecture and terminology we introducted in Chapter 1, where are files stored?
d) Secondary memory

### What is stored in a "file handle" that is returned from a successful open call?
d) The handle is a connection to the file's data

### What do we use the second parameter of the open() call to indicate?
d) Whether we want to read data from the file or write data to the file

### What Python function would you use if you wanted to prompt the user for a file name to open?
d) input()

### What is the purpose of the newline character in text files?
d) It indicates the end of one line of text and the beginning of another line of text

### If we open a file as follows:
```python
xfile = open('mbox.txt')
```
### What statement would we use to read the file one line at a time?
d) for line in xfile:

### What is the purpose of the following Python code?
```python
fhand = open('mbox.txt')
x = 0
for line in fhand:
    x = x + 1
print(x)
```
d) Count the lines in the file 'mbox.txt'

### If you write a Python program to read a text file and you see extra blank lines in the output that are not present in the file input as shown below, what Python string function will likely solve the problem?
```
From: stephen.marquard@uct.ac.za
 
From: louis@media.berkeley.edu
 
From: zqian@umich.edu
 
From: rjlowe@iupui.edu

```
d) rstrip()

### The following code sequence fails with a traceback when the user enters a file that does not exist. How would you avoid the traceback and make it so you could print out your own error message when a bad file name was entered?
```
fname = input('Enter the file name: ')
fhand = open(fname)
```
d) try / except

### What does the following Python code do?
```python
fhand = open('mbox-short.txt')
inp = fhand.read()
```
d) Reads the entire file into the variable inp as a string