class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Creating an instance of Multiplier
double = Multiplier(2)

# Testing with callable()
print("Is 'double' callable?", callable(double))  # True

# Using the object like a function
result = double(10)
print("double(10) =", result)
