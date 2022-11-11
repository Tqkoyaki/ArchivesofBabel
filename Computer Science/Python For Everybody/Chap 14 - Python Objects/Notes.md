### Managing Larger Programs
- The four basic programming patterns are sequential code, conditional code (if statement), repetitive code (loops), and the use of store and reuse (functions).
- There are also data structures that can be used to store and organize data.
- Object-oriented programming is a way to arrange your code into pieces so its easier to understand.
- Python provides a number of built-in objects like list.
- One way to think about OOP is that our program is seperated into multiple "zones" and they have well defined interactions with the outside world (inputs and outputs) and the other zones within the program.
- The advantage is OOP is that complexity can be hidden, you dont need to know how the libraries work, you just need to know how to use them.
- You can ignore the details of other objects and focus on the object you are working on.

### Python Objects
- An object can contain a number of functions called methods and a number of variables called attributes.
- We use the `class` keyword to define a new class. It is followed by the name of the class and a colon.
```python
class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()
an.party()
PartyAnimal.party(an)
```
- Each method looks like a function and starts with the def keyword. Methods also have a special first parameter called `self`.
- Attributes are variables made in the class definition.
- The ckass is a template for creating objects like a cookie cutter and objects using the class are like cookies.
- To create an object or instance of a class, we use the class name followed by parentheses.
- You can call a method on an object by using the dot notation.
- You can also access the attributes of an object using the dot notation.
- Another way to call a method is to use the class name dot the method name followed by an instance of the class in parentheses.
- dir() is a built-in function that returns a list of the attributes and methods of an object.
- When contrusting a class, you can use the `__init__` method to initialize the attributes of an object. It lets you setup deafult values for the attributes. This is the constructor.
- When an object is destroyed, the `__del__` method is called. It causes everything in the object to be destroyed.
  
### Multiple Instances and Inheritance
- You can create multiple instances of a class and each will have its own copy of the attributes and methods.
-  You can create a new class than inherits from an existing class by putting the name of the existing class in parentheses after the new class name. The new class is called a subclass and the existing class is called a superclass. The subclass inherits all the attributes and methods of the superclass.
- __getitem__ and __setitem__ are special methods that are called when you use the square brackets to get or set an item in a list.

### Glossary
- Child class: A new class that inherits from an existing class.
- Parent class: The class from which a child class inherits.