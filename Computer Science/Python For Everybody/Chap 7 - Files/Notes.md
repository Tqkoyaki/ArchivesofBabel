### Persistence
- So far our code has been communcating with the CPU using condition executions, function and iterations. We also have worked with main memory by creating data structures.
- Secondary memory is a storage that stores data permanently even when the computer is turned off. It also allows us to transport data from one computer to another.

### Opening files
- To read or write to a file, you must first open it so it involves telling the OS that you want to open the file.
```python
file = open("file.txt")
```
- The open function returns a file handle that doesn't contain the actual data but it gives us a way to read the data. You are given a handle only if the file exists and you have permission to read it.

### Text files and lines
- A text file can be thought of as a sequence of lines. Newline characters are used to seperate lines (\n).
- \n counts as a character

### Reading files
- A for in loop can be used to read a file line by line by using a line as a iteration variable.
- Open doesn't read the entire file because the file could be quite large.
- If you know the file is small, you can use the read method on the handle to read the entire file. It is stored as a string.
- rstrip() removes whitespaces from the right.

### Writing files
- To write to a file, you have to open it with mode 'w' as a second parameter.
```python
fout = open('output.txt', 'w')
```
- If the file already exists, opening it in write mode clears out the old data and starts fresh.
- Use handle.write(line) to write to a file.
- Always handle.close() to close the file to prevent data loss if power goes off.
- Python makes sure all open files are closed when the program ends. But it is a good practice to close the file as soon as you are done with it espically if you are writing to it.

### Debugging
- repr() is a built in function that takes a string and returns a string representation of the argument meaning its whitespace characters and escape characters are displayed. Not every system treats escape characters the same way. Like some use \n while others use \r.

### Glossary
- catch: to prevent an exception from terminating a program using a try and except statement.
- Pythonic: a technique that is idiomatic to Python.
- Quality Assurance: Testing the quality of a software and identifying problems before it is released.
- text file: a file that contains a sequence of characters.
- new line: a special character that marks the end of a line.