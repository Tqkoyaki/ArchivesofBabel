# Tuples, Lists, Aliasing, Mutability, and Cloning
- Tuples are an ordered sequence of elements and you can mix types
- Cannot change the elements of a tuple meaning they are immutable
- Represented by parentheses
- `te = () # empty tuple`
- Adding tuples together creates a new tuple with the elements of both
- ("mit", ) is a tuple with one element. The comma is necessary
- You can slice the tuple and get its length but you cannot change any of its elements
- `x = y` and `x = y` doesnt work for swapping, you need a temporary variable. In python you can do x, y = y, x to do the same thing.
- Tuples also let you return multiple values from a function.