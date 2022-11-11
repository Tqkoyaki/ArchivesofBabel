### Dictionaries
- A dictionary is like a list but the indices can be (almost) any type. They are maps of keys to values.
- To create a empty dictionary, use `{}` or `dict()`.
- To add a value do `dict_name[key] = value`.
- You can create a dictionary with values using `dict_name = {key1: value1, key2: value2}` as well.
- The order of the key value pairs is unpredictable in a dict.
- To get an item from a dictionary, use `dict_name[key]`.
- If an item doesn't exist, you get a `KeyError`.
- You can use the `in` operator to check if a key is in a dictionary. You can use `len` to get the number of key value pairs in a dictionary.
- You can get a list of values using `dict_name.values()`.
- For lists in operator uses a linear search algorithm so the longer the list, the longer it takes. For dictionaries, the in operator uses a hash table so it takes a constant time.
- You can use `dict_name.get(key, default)` to get a value from a dictionary. If the key doesn't exist, it returns the default value.

### Looping and dictionaries
- The for in loop iterates over the keys of a dictionary.
- You can get the keys in a dict using `dict_name.keys()`.
- string.translate is a string method that takes a fromstr, tostr, and deletestr. It replaces chars from fromstr with chars from tostr in the same position and deletes all chars in deletestr.
- You can get punctuation from string.punctuation by importing the string class.

### Debugging
- Scale down the input if possible and gradually increase it correctly errors on the way.
- Check summaries and types to make sure the right type of value is being used.
- Write self-checks to make sure your code is doing what you think it is doing.
- Print the errors out pretty to reduce time debugging.

### Glossary
- hashtable: the algorithm used to implement Python dictionaries.
- hash function: a function used by a hashtable to compute the location for a key.
- histogram: a set of counters or frequencies.
- implementation: a way of performing a computation.
- item: another name for a key-value pair.
- lookup: a dictionary operation that takes a key and finds the corresponding value.
- nested loops: loops that appear in the body of another loop. The inner loop runs to completion each time the outer loop executes once.