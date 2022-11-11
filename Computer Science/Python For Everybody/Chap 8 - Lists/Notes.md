### A list is a sequence
- Like a string, a list is a sequence of values. In a string they are characters but in a list they can be any type. Lists are made by closed brackets and commas.
```python
[10, 20, 30, 40]
['crunchy frog', 'ram bladder', 'lark vomit']
['spam', 2.0, 5, [10, 20]]
```
- A list within another list is nested.
- A list that contains no elements is called an empty list.
- You can assign a list to a variable.


### Lists are mutable
- You can index a list like you index a string.
- You can also set a value is a list using an index like `list_name[index] = value`.
- Indices work exactly like strings. The in operator also works on lists.

### Traversing a list
- You can use a for in loop or a for i in range(len(list_name)) loop to traverse a list.
- A for loop over an empty list never executes the body.

### List operations
- The + operator concatenates lists.
- The * operator repeats a list a given number of times.
- You can slice a list like a string where [start:end] returns a new list that starts at the start index and ends at the end index.
- You can do [:] to make a copy of a list.
- A slice operation on the left can be used to update multiple elements.
```python
t = ['a', 'b' , 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)
# ['a', 'x', 'y', 'd', 'e', 'f']
```

### List methods
- append adds a new element to the end of a list.
- extend takes a list as an argument and appends all of the elements.
- sort arranges the elements of the list from low to high. It is a void function that sorts the list in place.

### Deleting elements
- pop(index) removes the element at the given index and returns it. If you don't provide an index, it deletes and returns the last element.
- del list_name[index] removes element at index in place.
- You can remove an element from a list if you don't know its index by using the remove method. Returns none and does the operation in place.
- You can delete multiple elements using del list_name[start:end].

### Lists and functions
- len(list_name) returns the number of elements in a list.
- max(list_name) returns the largest element in a list.
- min(list_name) returns the smallest element in a list.
- sum(list_name) returns the sum of all the elements in a list. Only works with numbers.

### Lists and strings
- You can use the split method to break a string into words and store them as a list of strings. The paremeter is a delimiter which is a character that marks the boundaries between words. By default its spaces.
- join can be used in a list with a delimiter to concatenate the elements of a list into a string.

### Objects and values
- To check whether two variables refer to the same object, you can use the is operator.
- An object has a value. Two objects can have the same value and are equivalent but not identical because they refer to different objects.

### Aliasing
- If you assign one variable to another, both variables refer to the same object. This association of a variable with an object is called a reference.
- An object with more than one reference has more than one name, so we say that the object is aliased.
- It is a good habit to avoid aliasing.
- It is not a problem for immutable objects like strings.

### List arguments
- When you pass a list to a function. the function gets a reference of the list. If the function modifies the list, the caller sees the change.

### Glossary
- element: one of the values in a list
- equivalent: having the same value
- identitical: having the same value and being the same object
- object: something a variable can refer to. An object has a type and a value
