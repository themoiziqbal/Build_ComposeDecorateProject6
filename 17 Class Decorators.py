# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Applying the class decorator
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Creating an instance of Person
p = Person("Alice")

# Calling the dynamically added greet() method
print(p.greet())
