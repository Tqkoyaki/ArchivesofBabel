### Updating variables
- You need to initialize a variable before you can update it.
- Updating a variable by adding 1 is called an increment; subtracting 1 is called a decrement.

### The while statement
- A while statement repeatedly executes a target statement as long as a condition is true.
```python
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
```
- The flow of execution for a while statement is to evaluate the condition, if its false exit the loop, otherwise execute the body and then go back to the first step.
- An iteration variable controls when the loop finishes and should be changed every time through the loop. If there is no iteration variable, the loop will repeat forever, resulting in an infinite loop.

### Infinite loops
- You can use a break statement to get out of an infinite loop. Once the break statement is executed, the program execution immediately resumes after the loop.
```python
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')
```
- You can also use a continue statement to skip the rest of the loop and immediately jump to the next iteration.
```python
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
```

### Definite loops using for
- A while statement is an indefinite loop because it loops until a condition is met vs a definite loop which loops a specific number of times.
```python
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
    # The variable friend changes per iteration and is used to refer to the current element of the list.
print('Done!')
```
- for and in are reserved words.
- Loops generally have one or more variable initialized before the loop, the there some computation run in the body and then you look at the resulting variable when the loop completes.

### Debugging
- One wawy to cut debbugging time is through "debugging by bisection". Break the problem in half and then test each half and root out the problem that way.

### Glossary
- accumulator: A variable used in a loop to add up or accumulate a result.
