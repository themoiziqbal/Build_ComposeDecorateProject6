class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    # Getter
    @property
    def price(self):
        print("Getting price...")
        return self._price

    # Setter
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price can't be negative!")
        else:
            print("Setting price...")
            self._price = value

    # Deleter
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Creating an object
p = Product(100)

# Accessing the price (getter)
print(p.price)

# Setting a new price (setter)
p.price = 150
print(p.price)

# Trying to set a negative price
p.price = -50

# Deleting the price (deleter)
del p.price

# Accessing after deletion will raise an error
try:
    print(p.price)
except AttributeError as e:
    print("Error:", e)
