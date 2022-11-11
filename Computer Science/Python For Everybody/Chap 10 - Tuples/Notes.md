### Tuples
- A tuple is a sequence of values like a list but the values are immutable. They are also comparable and hashable so it can be sorted and used as keys in dictionaries.
- A tuple is created as a list seperated with commas and nothing else. They can be closed with parentheses but it is not necessary.
```python
t = 'a', 'b', 'c', 'd', 'e'
t = ('a', 'b', 'c', 'd', 'e')
```
- To create a tuple with a single element, you need to include a comma at the end.
- You can also create an empty tuple using tuple().
- Placing a string in the parentheses creates a tuple of characters. Same works with list and tuple in parenthesis.
- You can index and slice tuples like lists.
- You cannot modify the elements of a tuple but you can replace one tuple with another.

### Comparing tuples
= For tuples you compare the first elements and keep going until you find a difference. Anything after the difference is ignored.
- Sorting sorts the first element first and then the second and so on and in case of a tie, it uses the next element to break the tie. This feature is a pattern called DSU (Decorate, Sort, Undecorate).

### Python Features
- Python allows for tuple assignment. You can assign multiple variables at once.
```python
m = ['have', 'fun']
x, y = m
print(x, y)
# Output: have fun
```
- x, y is a tuple in this situation, we just omit the parentheses. You can write (x, y) = m as well.
- A cool way to swap variables is to use tuple assignment.
```python
a, b = b, a
```
- The number of variables on the left and right must be the same.
- Dictionaries have a method called items that returns a list of tuples, where each tuple is a key value pair.

### Advaanced Tuple Uses
- You can do tuple assignment in for loops too.
```python
for key, val in list(d.items()):
    print(key, val)
```
- Tuples are hasable and lists are not. This means you can use tuples as keys in dictionaries but not lists. Syntax is dict[tuple] = value or dict[(tuple)] = value.
- A string is immutable and can only hold chars. A tuple is immutable and can hold any type of data. A list is mutable and can hold any type of data.
- sort and reverse only work on mutable lists but you can use sorted and reversed which takes in a list as a parameter and returns a new list. This works great for immutable lists.

### List Comprehension
- Allows you to create a new list using a for loop and a conditional expression but in a compact way.
```python
list = [x for x % 2 == 0 in range(10)]
# Output: [0, 2, 4, 6, 8]
```
- Lists, dictionaries, and tuples are data structures.

### Glossary
- Comparable: able to be compared using the relational operators.
- Data Structure: a collection of related values often organized.
- DSU: Decorate, Sort, Undecorate. A pattern that involves building a list of tuples, sorting it, and extracting the sorted values.
- Gather: Assemble a variable-length argument tuple.
- Hashable: A type that has a hash function. Immutable types like integers, floats, and strings are hashable; mutable types like lists and dictionaries are not.
- Scatter: The operation of treating a sequence as a list of arguments.
- Shape (of a data structure): The composition of a data structure.
- Singleton: A sequence with a single element.

