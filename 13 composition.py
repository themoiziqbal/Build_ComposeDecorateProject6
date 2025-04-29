# Composition
# It is when a class contains objects from another class

from random import choice

# Engine class
class Engine:
    def __init__(self):
        pass
    # Tell that it is ok
    def check(self):
        return choice(["OK","Not OK"])

# Car class
class Car:
    def __init__(self,name):
        self.name = name
        self.engine = Engine()

    def status(self):
        print(f"Car Name: {self.name}\nEngine status: {self.engine.check()}")

def main():
    car = Car("Toyota")
    car.status()

if __name__ == '__main__':
    main()