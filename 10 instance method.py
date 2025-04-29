class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # Instance method
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

# Creating an object of Dog
dog1 = Dog("Labrador", "Golden Retriever")

# Calling the instance method
dog1.bark()
