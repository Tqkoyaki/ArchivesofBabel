### Why Program?
- Computers are very good at doing repetitive and mundane tasks that humans find boring and tedious. We do the creative stuff and let the computer do the rest.

### Computer Hardware Architecture
- Central Processing Unit (CPU):  Does the computation
- Main Memory: Stores information that the CPU needs in a hurry
- Secondary Memory: Stores information but slower than main memory. The advantage is that it can store information even without power.
- Input and Output Devices: Ways to interact with the computer like screens, keyboards, and mice.
- Network Connection: Allows a computer to retrieve information over a network.

### Understanding Programming
- Programs are stored instructions for a CPU to execute. Programming is the process of creating these instructions and making sure they are correct.
- Reserved Words for Python are like the vocabulary of the language. These are wrods that have special meaning.
- Your own made up words are the variables. You can't use reserved words as variables.
- The list of reserved words for Python are: {and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield} (nonlocal and exec included but not mentioned in the book)

```python
# Example of a program
print("Hello World")
```
- Use quit() to exit the Python interpreter

### Interpreters and Compilers
- The CPU understands machine language which is a series of 1s and 0s.
- An intrepreter reads source code of a program and interprets the instructions on the fly.
- Variables refer to the labels we use to refer to this stored data.
- A complier needs to be given the entire program so that it can run a process to translate that source code to machine language and puts the resulting machine language instructions into a file for later execution.
- Examples of executable machine language programs are .exe or .dll files.
- The python interpreter is a program written in C that reads and executes Python source code. The executable file is called python.exe.

### Writing a program
- Python scripts have names that end with .py
- To run a Python script called hello.py, you would type...
```
python hello.py
```
- A python program at its most basic is a sequence of Python statements that have been crafted to do something.

### Definitions
- Inputs are data from the "outside world".
- Outputs are displayed results of the program.
- Sequential Execution perform statements one after another.
- Conditional Execution check for certain conditions and then execute or skip a sequence of statements.
- Reuse is the ability to write a set of instructions once and give them a name to reuse those instructions as many times as you want.
- Syntax errors are errors that have violated the grammer rules of the language.
- Logic errors are errors where there is good syntax but there is a mistake in the logic of the program. Order of the statements can be wrong or statements are related to each other incorrectly.
- Semantic errors are errors where there is simply a mistake in the program.

### Debugging
- Reading: Examine your code and make sure that is what you intended to write.
- Running: Experiment by making changes and running again.
- Ruminating: Take some time to think. Figure out the type of error, the information from the error messages or the output of the program. What changed last before the problem appeared.
- Retreating: If all else fails, back up to a known good state and start over.


### Extra Glossary Words
- Bug: An error in a program.
- High-level language: A programming language that is easy for humans to read and write.
- Interative mode: A mode of the Python interpreter where you can type in one statement at a time and immediately see the result.
- Low-level language: A programming language that is close to the machine language of the computer.
- Parse: To examine a program and analyze the syntactic structure.
- Portablity: A property of a program that can run on more than one kind of computer.
- Print function: A function that displays the value on the screen.
- Problem solving: The process of formulating a problem, finding a solution, and expressing it.
- Source code: The human readable version of a program.
