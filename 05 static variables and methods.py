# Static variables and methods
from random import randint
class MathUtils:
    @staticmethod
    def add(a,b):
        return a + b
    
def main():
    # Get results of adding two random numbers
    a : int = randint(0,1000)
    b : int = randint(0,1000)

    result : int = MathUtils.add(a,b)

    # Print the result
    print(f"{a} + {b} = {result}")

if __name__ == '__main__':
    main()
