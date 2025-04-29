# 3. Public Variables and Methods
Assignment:
Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class. #

class Car:
    def __init__(self,brand : str):
        self.brand = brand
    
    def start(self):
        print("Starting the car!")

def main():
    # Create a BMW car
    car = Car("BMW")
    print(f"Car of brand {car.brand} created!")

    # Start the car
    car.start()

if __name__ == '__main__':
    main()