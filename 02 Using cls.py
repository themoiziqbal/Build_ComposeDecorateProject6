# 2. Using cls

Assignment:
Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count. #



class Counter:
    # Class variable to keep track of object count
    count = 0

    def __init__(self):
        # Increment the count each time an object is created
        Counter.count += 1

    # Class method to display the count
    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

# Creating objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Calling the class method to display count
Counter.display_count()
