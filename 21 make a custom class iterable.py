# Make a custom class iterable
from time import sleep
# Custom iterable class that counts down to zero
class Countdown:
    def __init__(self,start):
        self.start = start
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            current = self.current
            self.current -= 1
            return current

def main():
    # Countdown from 3 to zero
    for i in Countdown(3):
        print(i)
        sleep(0.3)
    print("Boom!")

if __name__ == '__main__':
    main()
